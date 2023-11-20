#Christian Martinez
#Program 3
#10/5/23
#The purpose of this program is to create a pricing app for Larry's
#Landscaping Business

#Display the landscaping menu

print('***************************************************************')
print('**                                                           **')
print("                 Larry's Landscaping Materials               **")
print('                                                             **')
print('Product and price per square foot:                           **')
print('                                                             **')
print('Seeds  $10                                                   **')
print('Mulch  $12                                                   **')
print('Gravel $14                                                   **')
print('Pavers $19                                                   **')
print('***************************************************************')
print("")
print("")

#While loop to handle invaild inputs from user
while True:

#prompt/ask the user to type in a single letter upper case product code
    product=input("Type in the single letter uppercase code for the product.\n"
              "S for seeds, M for mulch, G for Gravel, P for Pavers: ")

#if loop determines if first input is valid 
    if product in['S', 'M', 'G', 'P']:


#if loop determines the price of the product they ordered base on above 
        if product == 'S' :
            SF=float(input("How many square feet would you like: "))
            Price=(SF*10)*1.07
            print(f'You ordered {SF} feet of seeds for a total of $ {Price:,.2f}')
            exit()

        elif product == 'M':
            SF=float(input("How many square feet would you like: "))
            Price=(SF*12)*1.07
            print(f'You ordered {SF} feet of mulch for a total of $ {Price:,.2f}')
            exit()

        elif product == 'G':
            SF=float(input("How many square feet would you like: "))
            Price=(SF*14)*1.07
            print(f'You ordered {SF} feet of gravel for a total of $ {Price:,.2f}')
            exit()

        else:
            SF=float(input("How many square feet would you like: "))
            Price=(SF*19)*1.07
            print(f'You ordered {SF} feet of pavers for a total of $ {Price:,.2f}')

#Restarts the program if input was invalid
    else:
        print('\nInvaild input please enter S, M, G, P\n')
        continue 
    break
