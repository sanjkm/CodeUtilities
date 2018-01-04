===========
FileDataObj
===========

FileDataObj provides functions that facilitate placing file data into a
suitable Python object, and doing the converse, i.e. outputting the data from
a Python object into a file. 

Typical usage for the package might look as follows:

from FileDataObj import filetoobj

infile = 'invoice_numbers.txt' # file containing invoice numbers
InvoiceNumList = filetoobj.filetolist (infile)

