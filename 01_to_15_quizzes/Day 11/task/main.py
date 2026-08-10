import random
from art import logo

card_values = {
    "A": 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
game_is_on = True
blackjack_threshold = 21

def get_value(v):
    return card_values[v]

def get_random_card():
    random_number = random.randint(0, len(cards) - 1)
    return cards[random_number]

def get_current_count(cards):
    count = 0
    for card in cards:
        count += card_values[card]
    if count > blackjack_threshold and 'A' in cards:
        count -= 10
    return count

consent = str(input('Do you want to play the Blackjack?'))
if consent.lower() == 'y':
    print(logo)
else:
    game_is_on = False

user_cards = [get_random_card(), get_random_card()]
computer_cards = [get_random_card(), get_random_card()]

def check_current_result():
    print(f'Your cards: {user_cards}. Value: {get_current_count(user_cards)}')
    print(f'Computer\'s first cards: {computer_cards[0:1]}')
    return get_current_count(user_cards) <= blackjack_threshold

def declare():
    user_score = get_current_count(user_cards)
    computer_score = get_current_count(computer_cards)
    user_diff = blackjack_threshold - user_score
    computer_diff = blackjack_threshold - computer_score
    print(f'Your cards: {user_cards}. Computer cards: {computer_cards}')
    print(f'Your score: {user_score}, computer score: {computer_score}')
    if computer_score > blackjack_threshold or user_score > blackjack_threshold:
        if computer_score > blackjack_threshold:
            print('User wins')
        else:
            print('Computer wins')
    elif user_diff == computer_diff:
        print('Draw')
    elif user_diff > computer_diff:
        print('Computer wins')
    else:
        print('User wins')


while game_is_on:
    can_go_further = check_current_result()
    if can_go_further:
        want_to_play = str(input('Type \'y\' to get another card or \'n\' to pass?'))
        if not want_to_play.lower() == 'y':
            declare()
            game_is_on = False
        else:
            user_cards.append(get_random_card())
    else:
        declare()
        game_is_on = False
