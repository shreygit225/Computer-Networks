# byte stuffing
str1 = input("Enter Data: ")
str2 = str1.replace("Esc","EscEsc")
str2 = str2.replace("Flag","EscFlag")
print("The dataframe looks like: FlagHead"+str2+"TailFlag") 
