l_1 = input() 
l_2 = input()

l_1 = l_1.split(" ")
l_2 = l_2.split(" ")

g = "h"
s = "h"

if l_1[0] == l_2[0] or l_2[0] >= l_1[0]:

    g = "m"

else :
    g = "n"

if l_1[1] == l_2[1] or l_2[1] >= l_1[1]:

    s = "m"

else :
    s = "n"

if s == "m" and g == "m":
    print("yes")

else:
    print("no")




