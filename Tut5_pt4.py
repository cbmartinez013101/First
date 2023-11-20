#A while loop that computes sales comissions

counter=1

#When you run the program type in the number 2 for number of
#sales people, when promted, this will allow you to answer for
#two different sales people. Put in your own values and maybe
#.10 percent comission rate

salespeople=int(input("Enter in the number of sales people: "))

#Computes commission

while counter<=salespeople:
    sales=float(input(f'Enter the sales for salesperson {counter}: '))
    commrate=float(input('Enter in commission rate: '))

    commission= sales*commrate

    print(f'The comimission rate is ${commission:,.2f}.')

    #Increments the counter varibles by one
    counter= counter +1

                      
