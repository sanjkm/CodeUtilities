# Collection of programs that takes a Python object as input, and outputs
# the data in that object to a file

# Takes a list of data and appends it to file, separated by inputted delimiter
def listtofile (DataList, outfile, delim):
    with open(outfile, 'a') as f_out:
        index = 0
        for item in DataList:
            if index > 0:
                f_out.write(delim + item)
            else:
                f_out.write(item)
                index = 1
        if delim != '\n':
            f_out.write('\n')
    f_out.close()
