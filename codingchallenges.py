
# task1 coding practice 


seven = 7 
precise = "09388641"
eight = 8 
temperature = 6 
length = 5
width = 1.55
area = width * length 
print (area)


i , j = 5, 10 
i, j = j , i 
print ( "i = ", i , "j = ", j)

first_place_winner, second_place_winner = 98 , 93
first_place_winner, second_place_winner = second_place_winner, first_place_winner
print("first place winner = ", first_place_winner, "second place winner = ", second_place_winner)


best_value , second_best_value = 18, 13
best_value, second_best_value = second_best_value, best_value
print("best value is ", best_value, "second best value is ", second_best_value)

matric_age = 23
grad_age = matric_age * 4
print("grad age is ", grad_age)



verbal_score = 88
math_score = 46
overall_score = verbal_score + math_score
print(overall_score)

taxable_purchase = 3.50
tax_free_purchases = 6.75
total_amount = taxable_purchase + tax_free_purchases
print(total_amount)

ending_time = 7.30 
start_time = 4.65
overall_time = ending_time - start_time
print(overall_time)


value_1 = 12
value_2 = 40 

def average (value_1, value_2):
    avg = value_1 + value_2 / 2
    return avg
print(average(value_1, value_2))

price = 2.49
total_number = 40 
total_price = price * total_number 
print(total_price)





# task 2 boolean and conditional statements 


number2 = input("please write your number here: ")
number2 = int(number2)
if number2 /2 and number2 < 5:
    print("number is divisible by 2 and greater than 5")
elif number2 /2 or number2 < 5:
    print("number is divisible by 2 or greater than 5")
else:
    print("numer is not divisible by 2 and not greater than 5")


    
leap_year = input("please enter a year: ")
leap_year = int(leap_year)
if leap_year / 4 == 0 and leap_year / 100 != 0:
    print("it is a leap year!")
elif leap_year / 400 == 0:
    print("it is a leap year!")
else:
    print('not a leap year :/')




import random 

number_1 = random.randint(0, 100) 
number_2 = random.randint(0, 100)

sum = input(f"what is {number_1 } + {number_2 } ?")
sum = int(sum)

if sum == number_1 + number_2:
    print("Well done!")

elif sum != number_1 + number2:
    print("Sorry, try another time")




# WEEK 2  CODING CHALLENGES 


def calculate_area(width, height):
    width = input("Width of area: ")
    height = input("Height of area: ")
    int(width, height)
    area = width * height 
    return area 
