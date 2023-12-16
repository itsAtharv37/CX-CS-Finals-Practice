# # Write a program to input a string and display the string in the reverse order

def rev(string):
    str_ = ""
    for i in string :
        str_ = i + str_
    return str_

string = str(input('enter string'))
print(string)
print(rev(string))
