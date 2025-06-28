import random

#Global variables
def reset_game():
    global cards, dealer_hand, player_hand, dealer_first_card, dealer_second_card, player_first_card, player_second_card
    cards = ['♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K', '♣A',
             '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A',
             '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K', '♦A',
             '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K', '♠A']
    dealer_first_card = random.choice(cards)
    dealer_second_card = random.choice(cards)
    dealer_hand = [dealer_first_card, dealer_second_card]
    player_first_card = random.choice(cards)
    player_second_card = random.choice(cards)
    player_hand = [player_first_card, player_second_card]

#Start the App
def start():
    reset_game()
    menu = input('\nWould you like to start? Y/N: ')
    if menu.lower() == 'y':
       first_deal()
    elif menu.lower() == 'n':
       quit()
    else:
       print('\nInvalid Selection')
       start()

#Convert Face Cards to their respective blackjack values
def card_value(card):
   # Get the rank by removing the suit symbol
    rank = card[1:] if card[1] != '0' else card[1:]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)
    
def hand_total(hand):
    total = sum(card_value(card) for card in hand)
    # Adjust for Aces if total > 21
    aces = sum(1 for card in hand if card[1:] == 'A')
    while total > 21 and aces:
        total -= 10  # Count one Ace as 1 instead of 11
        aces -= 1
    return total

def first_deal():
   print(f'\nDealer: {dealer_first_card} ?')
   cards.remove(dealer_first_card)
   cards.remove(dealer_second_card)
   print('Player: ' + player_first_card, player_second_card)
   cards.remove(player_first_card)
   cards.remove(player_second_card)
   hit_or_stay()

def dealer_turn():
    print("\nDealer's turn:")
    print('Dealer hand:', dealer_hand)
    while hand_total(dealer_hand) < 17:
        card = random.choice(cards)
        dealer_hand.append(card)
        cards.remove(card)
        print('Dealer draws:', card)
        print('Dealer hand:', dealer_hand)
    print('Dealer total:', hand_total(dealer_hand))
    # Now compare hands
    if hand_total(dealer_hand) > 21:
        print('\nDealer busts! You win!')
    elif hand_total(player_hand) > hand_total(dealer_hand):
        print('\nYou Win!!!!')
    elif hand_total(player_hand) < hand_total(dealer_hand):
        print('\nYou Lose!')
    else:
        print('Push!')
    start()

def hit_or_stay():
   d = input('\nhit or stay?: ')
   if d.lower() == 'hit':
      player_third_card = random.choice(cards)
      player_hand.append(player_third_card)
      print(player_third_card)
      cards.remove(player_third_card)
      print(hand_total(player_hand))
      if hand_total(player_hand) < 21:
          hit_or_stay()
      elif hand_total(player_hand) == 21:
          print('\nYou Win!')
          start()
      else:
          print('\nBust!')
          start()
   elif d.lower() == 'stay':
       dealer_turn()
       if hand_total(player_hand) > hand_total(dealer_hand):
          print('\nYou Win!!!!')
          start()
       elif hand_total(player_hand) < hand_total(dealer_hand):
          print('\nYou Lose!')
          start()
       else:
          print('Push!')
          start()
   else:
       print('\nInvalid Selection!')
       hit_or_stay()
      
start()
