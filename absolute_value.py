#WAP to Take Any Integer As Input & Print The Absolute Value Of That Integer.
a=int(input("Enter Any Integer :- ")) 
if a<0 :
    b=a*(-1)
    print(f"The Absolute Value of {a} is {b}.")
else : print(f"The Absolute Value of {a} is {a}.")