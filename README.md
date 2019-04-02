# Python ESCPOS extract binary to text from receipt printer

This repository is a python command-line version to extract text from
binary ESC/POS data. ESCPOS is a page description language that is commonly
used for receipt printing.

This tool is mainly to remove ESCPOS command from the printer binary file and 
to retain text only. Currently only tested on Python 3.x .

## Quick start - Esc2Txt

Download and execute the python script as follow:

```python
python main.py input_file output_file [--verbose (-v)]
```

```python
python main.py 00001.SPL 00001.txt
```

## Source of ESC command

The implementation of this esc2txt is mainly referring to EPSON & Star Micronics documentation.

- [Epson Printer Documentation](https://files.support.epson.com/pdf/general/escp2ref.pdf)
- [Star Micro Documentation] (www.starmicronics.com/support/mannualfolder/escpos_cm_en.pdf)


## NOTE

Not all commands are supported. Most common and primary command is in the list. Long instruction length command, especially print instruction on images , barcode or qrcode are not supported. Feel free to add on top of it.

Example on not supported instructon:

- 1B 28 42 nL nH k m s v1 v2 c BarCodeData
- 1B 26 00 n m [a0 a1 a2 d1 d2 ... dk]
- 1B 26 00 n m 0 [a 0 d1 d2 ... dk]
- 1B 2E c v h m nL nH d1 d2 ... dk
- 1B 26 00 n m [a d1 d2 ... dk]
- 1B 28 5E nL nH d1 ... dk
- 1B 4B nL nH d1 d2 ... dk
- 1B 4C nL nH d1 d2 ... dk
- 1B 59 nL nH d1 d2 ... dk
- 1B 5A nL nH d1 d2 ... dk
- 1B 2A m nL nH d1 ... dk
- 1B 5E m nL nH d1 ... dk
- 1B 2E 2 v h 1 0 0

Not supported command might remain in the text file after conversion. Might notice some printable ASCII character.

## Licensing

- [LICENSE.md](LICENSE.md)


