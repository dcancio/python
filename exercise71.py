# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
    for line in fh:
        may = line.rstrip()
        print may.upper()

except:
    print "File cannnot be find"
