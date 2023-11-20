#Midterm Exam
#Prepared by: Christian Martinez
#Date: Oct. 5, 2023
#Due Date: Oct. 7, 2023

#Prints the phone menu. The variable 'phones' below holds a list of three
#items, that are separted by a column

phones={"1 Galaxy Z": 1100,
        "2 iPhone 15": 1000,
        "3 Samsung S20": 1300}

print("-----------------Phones-----------------")
print("----------------------------------------")

#Displays the phone menu within 15 spaces to align the data
#the loop below will the 3 phones
for key, value in phones.items():
    print(f"{key:15}:${value:.2f}")

print("----------------------------------------")
print("----------------------------------------")

#Allows program to restart if there is an invaild input
while True:
#Prompts user to input the phone they want and makes sure it is valid
    product=input("Enter the corrisponding number to \n"
       "the phone you wish to purchase: ")
    if product in ['1','2','3']:
#Prompts the user for how many they want
        Quan=int(input("\n Enter the number you wish to purchase: "))
#Decision sturcture detrimes the total price
        if product == '1':
            Total=(Quan * 1100)*1.07
            print(f'You ordered {Quan} Galaxy Z phones. Your total \n with tax is ${Total:,.2f}')
            print('\nThank you')
            x=input('\npress enter to continue \n')
        elif product == '2':
            Total=(Quan * 1000)*1.07
            print(f'You ordered {Quan} Galaxy Z phones. Your total \n with tax is ${Total:,.2f}')
            print('\nThank you')
            x=input('\npress enter to continue \n')
        else:
            Total=(Quan * 1300)*1.07
            print(f'You ordered {Quan} Galaxy Z phones. Your total \n with tax is ${Total:,.2f}')
            print('\nThank you')
            x=input('\npress enter to continue \n')
    else:
        print("\nInvaild phone try again \n")
        continue
