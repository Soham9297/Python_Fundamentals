#from math import *

#my_num = 5
#print (my_num)
#print(sqrt(3.7))

""" name = input("Enter your Name : ")
age = input("Enter your age : ")
print ("Hello " + name + " !" + "You are "+ age) """


#CALCULATOR 

""" NUM1 = input("Enter the number =")
NUM2 = input("Enter the 2nd number=")

result =  float(NUM1) + float(NUM2)

print(result) """

#mad Libs 

""" color = input("Enter color:")
plural_noun = input("Enter plural noun:")
celebrity = input("Enter celebrity:")

print("Roses are "+ color)
print(plural_noun +" are blue")
print("I love "+ celebrity) """

#List

""" friends = ["Kevin","Bryan","Abdc","Emma","Oscar"]
lucky_numbers = [3,5,6,7,11]
friends.insert(1,"Kelly")
#friends.extend(lucky_numbers)
friends.pop()
print (friends.index("Kevin"))
print (friends)
friends.sort()
print(friends) """


#Tuples

""" coordinates = [(4,5),(9,10),(13,15)]

print(coordinates[1]) """

#Differece between List and Tuples 

#Functions

""" def  say_hi(name , age):
    print("Hello "+ name + " You are "+ str(age))
    

say_hi("Soham",26)
say_hi("Anurag",54) """

""" def cube(num):
    op = num*num*num 
    return op


print(cube (15)) """



# If statements

""" def max_num (num1,num2,num3):
    if num1 >=num2 and num1 >=num3:
        return num1
    elif num2 >=num1 and num2 >=num1:
        return num2
    else :
        return num3


max_num(12,15,18) """

# Calculator

# num1 = float(input ("Enter first number :"))
# op = input ("Enter operator: ")
# num2 = float(input ("Enter first number :"))

# if op == "+" :
#    print (num1 + num2)
# elif op == "-":
#    print(num1 - num2)
# elif op == "-":
#    print(num1 * num2)
# elif op == "/":
#    print(num1 / num2)
# else :
#    print("Invalid Operator")


#Dictionary
# monthconversion ={
#     "Jan": "January",
#     "Feb": "February"
# }

# print (monthconversion.get("Mar","Not a Valid Key"))

#While loop
# i = 1
# while i < 30:
#   print ("Hello ...!!!!")
#   i += 1

# print ("Done")

# Guessing game

# secret_word = "Giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guess = False


# while guess != secret_word and not(out_of_guess):
#     if guess_count< guess_limit:
#       guess = input ("Enter guess :")
#       guess_count +=1
#     else:
#       out_of_guess = True


# if out_of_guess:
#     print ("You loose, out of guesses")
# else :
#     print ("You win!!")


from pickle import TRUE


Secret_word = "Horse"
guess= ""

count = 0
limit = 4
end_chance = False

while guess != Secret_word and not (end_chance):
    if count <limit:
        guess =input ("Enter word")
        count += 1
else:
    print ("Success")

 
    