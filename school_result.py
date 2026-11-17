#WAP to Take Marks of Each Subject As Input And Print The Total Marks Obtained & Percentage.
first=int(input("Enter The Marks in 1st Subject :- "))
seceond=int(input("Enter The Marks in 2nd Subject :- "))
third=int(input("Enter The Marks in 3rd Subject :- "))
fourth=int(input("Enter The Marks in 4th Subject :- "))
fifth=int(input("Enter The Marks in 5th Subject :- "))
total=(first+seceond+third+fourth+fifth)
percentage=(total/5)
print(f"The Total Obtained Marks is {total} & percentage is {percentage}%.")