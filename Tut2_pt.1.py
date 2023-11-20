#assign a value to the salary variable
salary=2500

#assign a value to the bonus variable
bonus=1200.0

#compute the total pay adding the salary and bonus and assign
#the result into the variable called pay
pay=salary+bonus

#print the pay as currency as a float value and currency formatting
print('Your pay is '+'${:,.2f}'.format(pay))
