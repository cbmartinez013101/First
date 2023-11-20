#This program determines if a student gets a great sudent honor award

gpa=3.0
ch=60

#gets students gpa and credit hours
sgpa=float(input('What is your GPA: '))
sch=int(input('How many credit hours do you have: '))

#determines if the student meets the requirements
if sgpa>=gpa and sch>ch:
    print('Congratulations you are being awarded the Great Student Honor Award!')
else:
    print('Sorry, you are not eligible yet but keep working hard, you will get there.')
