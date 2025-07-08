import random


#program introduction
print(""" Welcome to lottery game! Guess numbers and if you guess correctly, you win $10 for each number guessed!""")
print("Guess five numbers from 1-100 and press enter after each number: ")

#user input
user_numbers = [int(input(" ")) for user in range(5)]

#list of random numbers between 1 and 100
winning_numbers = [random.randint(1,100) for win in range(5)]

#show user input and randomly generated numbers
print("You guessed: " , user_numbers)
print("The winning numbers are: ", winning_numbers)

#find the same numbers in both lists using the set() function
eval = set(user_numbers) & set(winning_numbers)

#count how many numbers were matching using len()
matching = len(eval)

#if matching numbers exist, multiply the len() by 10
if matching:
    winning_total = matching * 10
    print("Congratulations! You won $", winning_total)
else:
    print("You lost!")





    



