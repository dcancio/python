# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
    count = 0
    average = 0

    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        line = line.rstrip()
        pos_puntos = line.find(':')
        num_as_string = line[pos_puntos+2:]
        num = float(num_as_string)
        count = count + 1
        average = average + num

    print "Average spam confidence: " + str(average/count)
except:
    print "File cannot be find"
    #average_sum/count
