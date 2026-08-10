import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [{'title': 'Rock', 'emoji': rock},
           {'title': 'Paper', 'emoji': paper}, {
               'title': 'Scissors', 'emoji': scissors}]

user_pick = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if (user_pick > 2):
    print('Invalid input. Try again.')
    quit()
print('User picked: ' + options[user_pick]['title'])
print(options[user_pick]['emoji'])
computer_choice = random.randint(0, 2)
print('Computer picked: ' + options[computer_choice]['title'])
print(options[computer_choice]['emoji'])

if (user_pick == computer_choice):
    print('It\'s a draw')
elif ((user_pick == 0 and computer_choice == 2) or (user_pick == 1 and computer_choice == 0) or (
        user_pick == 2 and computer_choice == 1)):
    print('You Won!')
else:
    print('Computer Won!')
