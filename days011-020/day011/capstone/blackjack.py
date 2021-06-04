import os
import random

import art


def deal():
    """Return a random single card from the infinite deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def get_score(cards):
    """Returns the score for a given list of cards.
    A Blackjack will have a score of 0.
    All other list of cards are calculated with the
    sum of the cards, with the 11 being switched to
    1 if the score goes over 21"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def result(player_score, dealer_score):
    """Return a string with a message for the player
    that represents the final result of the game"""
    if player_score > 21:
        return "You went over. You lose!"
    if player_score == dealer_score:
        return "Draw!"
    if player_score == 0:
        return "You got Blackjack! You win!"
    if dealer_score == 0:
        return "Dealer got Blackjack! You lose!"
    if dealer_score > 21:
        return "Dealer went over. You win!"
    if player_score > dealer_score:
        return "You win!"
    return "You lose!"


def deal_start():
    """Return the deal of the first two mandatory cards"""
    cards = []
    for _ in range(2):
        cards.append(deal())
    return cards


def deal_dealer(player_score):
    """Return all the cards for the dealer"""
    cards = deal_start()
    if get_score(cards) == 0:
        return cards

    while get_score(cards) < 17:
        cards.append(deal())

    return cards


def info(player_cards, player_score, dealer_first_card):
    """Display info about the player cards and the first card of
    the dealer. Return if the user will want to draw another card"""
    print(f'Your cards: {player_cards}, current score: {player_score}')
    print(f"Computer's first card: {dealer_first_card}")
    return input("Type 'a' to get another card: ").lower() == 'a'


def final_info(player_cards, player_score, dealer_cards, dealer_score):
    """Display info about the final setup of player and dealer hands"""

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(result(player_score, dealer_score))


def blackjack():
    """Is a complete game of blackjack. Recursively
     starts another game if the user wants to"""
    print(art.logo)
    player_cards = deal_start()
    player_score = get_score(player_cards)

    if player_score == 0:
        dealer_cards = deal_start()
    else:
        dealer_cards = deal_dealer()
    dealer_score = get_score(dealer_cards)

    if dealer_score != 0 and player_score != 0:
        draw_again = info(player_cards, player_score, dealer_cards[0])
        while draw_again:
            print()
            player_cards.append(deal())
            player_score = get_score(player_cards)
            if player_score >= 21:
                draw_again = False
            else:
                draw_again = info(player_cards, player_score, dealer_cards[0])

    final_info(player_cards, player_score, dealer_cards, dealer_score)

    if input("Type 'a' to play again: ").lower() == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()


blackjack()
