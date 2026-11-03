#Password input
password = input('Please input your password: ')
#Checking if password is within the right range (between 8 and 16 characters)
while len(password) < 8 or len(password) > 16:
    if len(password) < 8:
        print('Password too short!')
    elif len(password) > 16:
        print('Password too long!')
    password = input('Please input your password: ')
#Setting variables early so the program doesn't crash
score = 0
lowerExist = False
upperExist = False
numExist = False
#calculating score
for i in range(len(password)):
    if password[i].isalpha() == True:
        if password[i].isupper() == True:
            upperExist = True
        elif password[i].islower() == True:
            lowerExist = True
        score += 5
    else:
        if password.isnumeric() == True:
            numExist = True
        score += 10
if (lowerExist == True and upperExist == False and numExist == False) or (lowerExist == False and upperExist == True and numExist == False):
    finalScore = score - (3 * len(password))
elif lowerExist == False and upperExist == False and numExist == True:
    finalScore = score - (5 * len(password))
else:
    finalScore = score
if len(password) >= 10:
    finalScore += 20
if finalScore <= 20:
    rating = 'Very low'
elif finalScore >= 21 and finalScore <= 40:
    rating = 'Low'
elif finalScore >= 41 and finalScore <= 70:
    rating = 'Medium'
elif finalScore >= 71 and finalScore <= 80:
    rating = 'High'
else:
    rating = 'Very high'
#Outputting score and rating
print('Your password is rated ' + str(finalScore) + ', which is ' + rating + '!')
