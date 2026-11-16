#WAP to Take Principle Value,Rate of Interest & Time Period As Input And Print Simple Interest & Total Amount Return After That Time.
principle=float(input("Enter The Principle Value(Rupees):- "))
rate=float(input("Enter The Rate of Interest(%) :- "))
time=float(input("Enter The Time Period(Years) :-"))
si=(principle*rate*time)/100
total=(si+principle)
print(f"The Simple Interest is {si} Rupees only.\nThe Total Amount After {time} Year is {total} Rupees only.")