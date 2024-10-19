# with  open("example.txt", "r+") as file:
#     #Perform operaitons on file
#     # lines = file.read(10) #Reads the first 10 characters in the data in the file
#     lines = file.readline() #reads a line of data in the file
#             #file.readlines() reads all lines of data 

# #Looping through the file and performing operations on each line

# with open("example.txt", "r+") as file: 
#     for line in file:
#         #Reads each line of data in the file
#         print("The entire line is: " + line)
#         print("The first character of this line is: ", line[0])

#Build up all the linesof the text file into one large string called contents

contents = ""                           #store the contents
with open('example.txt', 'r+') as file: 
    for line in file:                   #iterate throught the lines
            contents = contents + line  #add contents of each line to the previous
    print(contents)                     #print content



