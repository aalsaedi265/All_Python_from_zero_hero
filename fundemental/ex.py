# x= [1,2,3,4]
# print(len(x))

from curses.ascii import isdigit


lst= ['touchMe', 'Sebsatain', 'heroHero', 'yuri alpha', 'Aura']

first_slice = lst[::-1]
# second_slice = first_slice[:y]
# third_slice = second_slice[x:]
last_slice = first_slice[::1]



strings=['touchMe', 'Sebsatain', 'heroHero', 'yuri alpha', 'Aura']

arr=[]
# for idx in  range(1,len(strings)):
#     print(strings[idx])

# people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

# result = sorted(people, key=people.get)
# print(result)

import random

start = input('Enter the start of the range: ')
while not start.isdigit():
    print('Please enter a valid number.')
    start = input('Enter the start of the range: ')

end = input('Enter the end of the range: ')
while not end.isdigit() or int(end) < int(start):
    print('Please enter a valid number.')
    end = input('Enter the end of the range: ')

random_number = random.randint(int(start), int(end))

guess = None
attempts = 0

while guess != random_number:
    guessed_number = input("Guess a number: ")
    if not guessed_number.isdigit():
        print("Please enter a valid number.")
        continue
    
    attempts += 1
    guess = int(guessed_number)

suffix = ""
if attempts > 1:
    suffix = "s"

print(f'You guessed the number in {attempts} attempt{suffix}')