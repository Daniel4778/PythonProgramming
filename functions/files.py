
#f = open("inputFile1", 'r')
#f = open("inputFile1", "rt")
#f = open("inputFile1", "at")

#f = open("inputFile", "wt")
#f.write("adding another line to input file")
#print(f.read())
g = open("inputFile1", "w")
g.write("Daniel Paddock")
g = open("inputFile1", "r")
# g.write("Daniel Paddock")
print(g.read())
