#The purpose of this application is to create order form app for the Customer
#Processing Center

class Customer:
#Defines class charaterristics
    def __init__(self, custid, fname, lname, totalbill):
        self.custid=custid
        self.fname=fname
        self.lname=lname
        self.totalbill= float(totalbill)
#Creates the full name of the customer by defining first and last name
    def fullname (self):
        return('{},{}'.format(self.lname, self.fname))
#Calculates the final price for the customer
    def finalprice(self):
        return self.totalbill*1.07
#Gives Customer Info
cust1= Customer(1234,'Bill','Jones',100.00)
cust2= Customer(2345,'Sue', 'Smith',50.00)
cust3= Customer(3456,'Dave', 'Day', 1000.00)
cust4= Customer(4567,'Christian', 'Martinez',750.00)
#Prints out desired statements
print(f'{cust1.custid} {cust1.fullname()} ${cust1.finalprice():,.2f}') 
print(f'{cust2.custid} {cust2.fullname()} ${cust2.finalprice():,.2f}')
print(f'{cust3.custid} {cust3.fullname()} ${cust3.finalprice():,.2f}')
print(f'{cust4.custid} {cust4.fullname()} ${cust4.finalprice():,.2f}')
