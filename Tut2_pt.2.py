#This program gets an items' orginal price and calculates its sale price
#with a 20% discount

#Get the items original price, you will type in 100 when prompted
original_price=float(input("Enter the items' original price "))

#Compute 20% discount
discount=original_price*.2

#Calculate sale price
sale_price=original_price-discount

#Display items' sale price
print("Your pay is "+ "${:,.2f}".format(sale_price))
