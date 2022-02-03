months_of_year = "x JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()
str1 = input().split("/"); str1[1] = int(str1[1]) 
dok = "*" * (19 + len(str1[0]))
print(dok + '\n' + "* " + "DATE: " + str1[0] + "." + months_of_year[str1[1]] + "." + str1[2] + " *" + '\n' + dok)
