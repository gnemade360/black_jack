Blackjack (also known as 21). In this implementation, the game will be played between a player and a computer dealer. 
Please note that this is a basic implementation and does not include all the rules and features you may find in a real casino game.

import random

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    total_value = 0
    num_aces = 0

    for card in hand:
        if card in ('J', 'Q', 'K'):
            total_value += 10
        elif card == 'A':
            num_aces += 1
            total_value += 11
        else:
            total_value += int(card)

    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

# Function to display the current state of the game
def display_game(player_hand, dealer_hand, player_value, dealer_value):
    print("\nYour hand:", player_hand, "Value:", player_value)
    print("Dealer's hand:", dealer_hand[0], "[?]")

# Function to handle player's turn
def player_turn(deck, player_hand, player_value):
    while True:
        action = input("\nDo you want to (H)it or (S)tand? ").upper()

        if action == 'H':
            new_card = deck.pop()
            player_hand.append(new_card)
            player_value = calculate_hand_value(player_hand)

            if player_value > 21:
                display_game(player_hand, dealer_hand, player_value, dealer_value)
                print("Busted! You lose.")
                return player_value

            display_game(player_hand, dealer_hand, player_value, dealer_value)

        elif action == 'S':
            break

    return player_value

# Function to handle dealer's turn
def dealer_turn(deck, dealer_hand, dealer_value):
    while dealer_value < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value(dealer_hand)

    return dealer_value

# Function to determine the winner
def determine_winner(player_value, dealer_value):
    if player_value > 21:
        return "Dealer"
    elif dealer_value > 21:
        return "Player"
    elif player_value > dealer_value:
        return "Player"
    elif dealer_value > player_value:
        return "Dealer"
    else:
        return "Tie"

# Main function to run the game
def blackjack_game():
    print("Welcome to Blackjack!")
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    # Deal initial hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # Display the game state
    display_game(player_hand, dealer_hand, player_value, dealer_value)

    # Player's turn
    player_value = player_turn(deck, player_hand, player_value)

    # Dealer's turn
    if player_value <= 21:
        dealer_value = dealer_turn(deck, dealer_hand, dealer_value)
        display_game(player_hand, dealer_hand, player_value, dealer_value)

        # Determine the winner
        winner = determine_winner(player_value, dealer_value)
        print("\nGame Over!")
        print("Winner:", winner)

# Start the game
if __name__ == "__main__":
    blackjack_game()
