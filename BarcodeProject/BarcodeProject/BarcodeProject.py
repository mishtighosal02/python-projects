
from optparse import Option
from barcode.ean import EAN13
from barcode.writer import ImageWriter

num_of_barcodes = int(input("How many barcodes are required? "))
numbers = range(num_of_barcodes)

for i in numbers:
    id = str(input("Give 12-digit numbers for your barcode id: "))
    my_code = EAN13(id,writer=ImageWriter())
    name = input("Enter barcode file name: ")
    my_code.save(name)