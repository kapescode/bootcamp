# with open("cat_list.txt", "a") as file:
#     #using w or w+ mode will OVERWRITE the current contents of the file, use the append ("a") function instead to add to the file contents
#     user_cat = input("What is your cats name? ")

#     file.write(f"\n{user_cat}")
#     m_cats = ["mitsy", "johno", "james", "doggy"]
#     # file.writelines(m_cats)

# #This for loop format allows for the inputs to be put into the correct format in the file, matching how the current list looks
#     for line in m_cats:
#         file.write(f"\n{line}")

#Manipulating the list - eg converting all the text into lower case

with open("cats2.txt", "w") as file:
    user_cat = input("What is your cats name? ")

    file.write(f"\n{user_cat}")
    m_cats = ["mitsy", "johno", "james", "doggy"]
    # file.writelines(m_cats)

#This for loop format allows for the inputs to be put into the correct format in the file, matching how the current list looks
    for line in m_cats:
        file.write(f"\n{line}")

        