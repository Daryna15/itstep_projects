'''
try:
    age = int(input("Enter your age"))
    print("Your age is:", age)
    print(10/0)

except ValueError:
    print("Enter your age in numbers not letters")
except ZeroDivisionError:
    print("You can't divine by zero")
except:
    print("Something went wrong")

print("Everything alright")
'''
'''
try:
    candies = 20
    friends = int(input("Enter number of friends"))
    print("Quantity of candies for each friend is:", candies//friends)

except Exception as error:
    print(error)
'''

def check_score(score):
    if score < 1 or score > 12:
        raise ValueError("Score must be between 1 and 12")
    print("Your score is:", score)
    year_score = 100*score//12
    print("Your year score is:", year_score)



check_score(11)
check_score(6)

