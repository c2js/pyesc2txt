#############################################
### Author: Joshua Hui
### Version : 1.0
### Extract text and remove ESC POS printer command Esc2Txt
### MIT License 
#############################################

import binascii
import argparse

import cmd

def main():
  parser = argparse.ArgumentParser(description="Remove ESC POS command from receipt printer (.SPL) generated file")
  parser.add_argument("input_file", help="input file with ESC command")
  parser.add_argument("output_file", help="output file with text")
  parser.add_argument("-v", "--verbose", help="print output to screen")
  args = parser.parse_args()
  parse(args.input_file, args.output_file, verbose=args.verbose)



def parse(ifile, ofile, verbose=False):

  curesc = cmd.escmap
  text = ""


  with open(ifile, 'rb') as fptr:
    while True:
      buf = fptr.read(1)
      if not buf:
        break

      key = binascii.hexlify(buf).upper()
      key = key.decode('ascii')
      data = curesc.get(key, None)


      if data != None:

        ### if is integer indicate end of the command instruction 
        ### and it gives how many bytes it require to complete the instruction  
        if isinstance(data, int):

          ###  no tailing command just continue to read
          if data == 0:
            curesc = cmd.escmap
            continue

          ###  negative value is for command end at null value (b '00' ) 
          elif data < 0:
            # read  until reach 00
            while True:
              is00 = fptr.read(1)
              if binascii.hexlify(is00) == b'00':
                if verbose: print ("found 00, break")
                break
            curesc = cmd.escmap #reset and start again
            continue

          ###  if bigger than 0, we read the n-bytes from stream 
          elif data > 0:
            _ = fptr.read(curesc[key])
            curesc = cmd.escmap
            continue

          ### it not support to reach here.
          else:
            print ("bug")

        # in the middle of command, need to read further
        else:
          #is function
          curesc = cmd.escmap[key]
          continue

      #  not found in the map, reset the map to root 
      else:
        curesc = cmd.escmap

      #  a character we want, store it
      text += buf.decode('utf-8')  #text += buf.decode('ascii')


  f = open(ofile, 'w+')
  f.write(text)
  f.close()

  if verbose:
    print ("=" * 20 )
    print (text)
    print ("=" * 20)

if __name__ == "__main__":
    main()