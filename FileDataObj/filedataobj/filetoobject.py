# Collection of programs that takes a file containing data as input
# and returns a Python object containing that data,


# Program takes a file as input that contains text items on each
# line of the file
# All text items are placed into a list which is returned
# Each line of data comprises one element of the list

def filetolist (infile):
    datalist = []
    with open(infile, 'r') as f:
        for line in f:
           datalist.append((line.rstrip('\n')).rstrip(' '))
    f.close()
    return datalist

# Program takes as input a text file with two pieces of text,
# separated by a delimiter, on each line.
# The first item of text will be mapped to the second item
# in a dictionary, which is returned at the end of the file

def filetodict (infile, delim):
    DataDict = {}
    with open(infile, 'r') as f:
        for line in f:
            x_line = (line.rstrip('\n')).split(delim)
            DataDict[x_line[0]] = x_line[1]
    f.close()
    return DataDict
