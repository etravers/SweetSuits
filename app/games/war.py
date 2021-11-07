from app.configManager.configManager import ConfigManager
from app.cardFunctions.cardFunctions import CardFunctions


class War:
    """
    STEPS IN WAR:
    1 -- Shuffle all cards
    2 -- Distribute all cards amongst 2 players
    3 -- Draw top card from each player's hand
    4 -- Compare cards (the player with the higher valued card collects both cards and puts aside in another stack)
    5 -- If there is a tie, draw three cards from each player's hand and compare the third; winner takes all cards
    6 -- There is a winner when one player has all of the cards or if one player resigns
    """

    def determine_card_value(self, card: str):
        card_value = card[2:]
        if card_value == 'A':
            card_value = 1
        elif card_value == 'J':
            card_value = 11
        elif card_value == 'Q':
            card_value = 12
        elif card_value == 'K':
            card_value = 13
        else:
            card_value = int(card_value)

        return card_value

    def compare_cards(self, player_one_card: str, player_two_card: str, player_one_win_stack: [],
                      player_two_win_stack: [], player_one_hand: [], player_two_hand: [], played_cards: [],
                      win_stack: []):
        player_one_card_value = self.determine_card_value(player_one_card)
        player_two_card_value = self.determine_card_value(player_two_card)
        played_cards.append(player_one_card)
        played_cards.append(player_two_card)
        if player_one_card_value > player_two_card_value:
            player_one_win_stack.append(player_one_card)
            player_one_win_stack.append(player_two_card)
            win_stack = player_one_win_stack
        elif player_two_card_value > player_one_card_value:
            player_two_win_stack.append(player_one_card)
            player_two_win_stack.append(player_two_card)
            win_stack = player_two_win_stack
        elif player_two_card_value == player_one_card_value:
            self.determine_tie_winner(player_one_hand=player_one_hand, player_two_hand=player_two_hand,
                                      played_cards=played_cards, player_one_win_stack=player_one_win_stack,
                                      player_two_win_stack=player_two_win_stack)

    def determine_tie_winner(self, player_one_hand: [], player_two_hand: [], played_cards: [], player_one_win_stack: [],
                             player_two_win_stack: [], win_stack: []):
        counter = 0
        while counter != 2:
            played_cards.append(player_one_hand.pop())
            played_cards.append(player_two_hand.pop())
            counter += 1

        player_one_card = player_one_hand.pop()
        player_two_card = player_two_hand.pop()
        self.compare_cards(player_one_card=player_one_card, player_two_card=player_two_card,
                           player_one_win_stack=player_one_win_stack, player_two_win_stack=player_two_win_stack,
                           player_one_hand=player_one_hand, player_two_hand=player_two_hand, played_cards=played_cards)
        self.move_cards_to_win_stack(win_stack=win_stack, played_cards=played_cards)

    def move_cards_to_win_stack(self, win_stack: [], played_cards: []):
        pass

    def play_round(self, player_one_hand: [], player_two_hand: []):
        played_cards = []
        win_stack = []
        pass

    def play_game(self):
        cards = CardFunctions.shuffle(ConfigManager.CARDS)
        player_hands, card_pile = CardFunctions.distribute_cards_to_players(self=self, cards=cards,
                                                                            start_hand_count=26, player_count=2)
        player_one_hand = player_hands[0]
        player_two_hand = player_hands[1]
        player_one_win_stack = []
        player_two_win_stack = []

        while len(player_one_hand) != 52 or len(player_two_hand) != 52:
            self.play_round(player_one_hand=player_one_hand, player_two_hand=player_two_hand)

        if len(player_one_hand) != 52:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
