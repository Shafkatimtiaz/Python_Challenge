#WAP to Take Two Integer As Input & Print That is 1st Integer is Divisible by 2nd or Not.
m=int(input("Enter The Divident:- "))
n=int(input("Enter The Divisor:- "))
if m%n==0 : print(f"Yes, {m} is Divisible by {n}.")
else : print(f"No, {m} is Not Divisible by {n}.")