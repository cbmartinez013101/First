#Programer:Christian Martinez
#Updated:9/9/2023
#Purpose: Toy Order Form and Final cost computation

#Get toy name
ToyN=input('Enter toy name ')

#Get Unit Price
ToyP=float(input('Enter toy price '))

#Get Quanity Order
ToyQ=float(input('Enter Quanity '))

#Price before tax
ToyT=ToyP*ToyQ

#Price with Tax
ToyF=ToyT*1.07

#Print toy name with total price
print("The price of "+ToyN+ " is " + "${:,.2f}".format(ToyF))
           
           
