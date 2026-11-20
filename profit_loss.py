#WAP to Take COST & SELL Price as Input And Print That There is Profit or Loss.
costing=float(input("Enter The Cost Price in Rupees :- "))
selling=float(input("Enter The Selling Price in Rupees :- "))
if costing>selling :
    loss=float(costing-selling)
    print(f"You Made a Loss Of {loss} Rupees.")
elif costing<selling :
    profit=float(selling-costing)
    print(f"You Made a Profit of {profit} Rupees.")
else : print("You Did Not Make Any Profit or Loss.")