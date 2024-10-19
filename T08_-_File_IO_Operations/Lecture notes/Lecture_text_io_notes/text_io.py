with open ("cat_list.txt", "r") as file:

    #    print(file)
#make sure files you want to edit are opened in VS code and in your current session editing (left tab)
#using the with code means you dont have to worry about closing the file manually
#anything we want to change in the file we should indent in the with statement

    content = file.readlines()
    print(content)

# We can make multiple read and readlines occur at the same time
# This requires file.seek(0) command to send the code reader back to the top of the file after running one read script, to run the other scripts for readline and readlines


with open ("cat_list.txt", "r") as file:
    content = file.read()
    print(content)

    file.seek(0)

    content = file.readline()
    print("\n")
    print(content)

    file.seek(0)

    content = file.readlines()
    print("\n")
    print(content)

#Can also read files with for loop command
with open ("cat_list.txt", "r") as file:
    for line in file.readlines():
        print(line)
