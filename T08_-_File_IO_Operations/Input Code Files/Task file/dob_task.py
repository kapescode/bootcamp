names = []          #create list for all names
DOBs = []           #create list for all DOB

with open ("DOB.txt", "r+") as file: #open file for reading 
    content = file.readlines() #read the document as a string in separate lines


    for line in content:
        string_split = line.split()             #split the strings 
        name = " ".join(string_split[:2])       #split the strings into the first 2 words (first name, surname).. perhaps there is a better  way to tell the code how to split the data, but this is what I went with
        DOB = " ".join(string_split[-3:])       #split the last 3 words (day, month, year) into separate strings

        names.append(name)                      #Keep adding names to the names section
        file.seek(0)                            #start from the top of the names each time 

        DOBs.append(DOB)                        #Keep adding DOBs to the DOB section
        file.seek(0)
        

print("Names \n")                               #print out the names section over eachother using for loop iteration
for name in names:
    print(name)

print("\nDate Of Birth:")                       #print out the DOB section over eachother using for loop iteration
for DOB in DOBs:
    print(DOB)