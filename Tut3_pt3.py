#This program uses field widths to display values aligned in columns.

num1=127.899
num2=3456.148
num3=3.776
num4=264.821
num5=88.081
num6=799.999

#Each number is displayed in a field of 10 spaces and rounded with
#2 decimal places

print(f'{num5:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num4:10.2f}{num6:10.2f}')
