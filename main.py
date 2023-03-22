import random
#variables
findPass = True
Time = 0
dev = False
real_pass = input("Enter a 12 digit password:")
Dev = input("Do you want to see dev logs? y/n:")
if Dev == 'y':
    Dev = True
else:
    Dev = False
        

print('We Are trying to find your password!')

#code
while findPass == True:
    ran_pass = str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))
    Time += .01
    if Dev == True:
        print("Password Lenght = "+ str(len(ran_pass)))
        print("""
        Tested | 
        """+ran_pass )
        
    if real_pass == int(ran_pass):
        print(' ')
        print('---------------------------')
        print('We found Your Password! Was it'+ ran_pass+'?' )
        print('---------------------------')
        print('It Took The Computer ' + Time + ' To find your password!')
        findPass = False
        
        break
