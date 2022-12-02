import random

while True:
    print('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
    user_choice = input()
    if user_choice in '12':
        break
    else:
        print("Incorrect format.")
        continue

count = 0
n = 0
while count != 5:
    if user_choice == '1':
        level_description = '(simple operations with numbers 2-9)'
        a = random.randint(2, 9)
        operand = random.choice('+-*')
        b = random.randint(2, 9)
        result = {'+': a + b, '-': a - b, '*': a * b}.get(operand)
        print(f'{a} {operand} {b}')

        running = True
        while running:
            try:
                user_solution = int(input())
                running = False
            except ValueError:
                print("Incorrect format.")
                continue
            if user_solution == result:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
        count += 1
    else:
        level_description = '(integral squares 11-29)'
        a = random.randint(11, 29)
        result = a ** 2
        print(f'{a}')

        running = True
        while running:
            try:
                user_solution = int(input())
                running = False
            except ValueError:
                print("Incorrect format.")
                continue
            if user_solution == result:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
        count += 1
print(f"Your mark is {n}/5. Would you like to save the result?"
      f" Enter yes or no.")
save_results = input()
possible_choices = ['yes', 'YES', 'y', 'Yes']
if save_results in possible_choices:
    user_name = input("What is your name?\n")
    with open('results.txt', 'a') as file:
        file.write(f'{user_name}: {n}/5 in level'
                   f' {user_choice} {level_description}.\n')
        print('The results are saved in "results.txt".')

