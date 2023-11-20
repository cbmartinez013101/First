# The program below uses an if....elseif...decision structure
# to determines a student letter grade base on their
# test score

score1=90
score2=80
score3=70
score4=60


testscore=int(input('Enter your test score value: '))



if testscore>=score1:
    print('Your grade is an A.')

elif testscore>=score2:
    print("Your grade is a B.")

elif testscore >= score3:
    print("Your grade is a C.")

elif testscore >= score4:
    print("Your grade is a D.")

else:
    print("Your grade is a F.")
