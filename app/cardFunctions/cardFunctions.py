import random


class CardFunctions:

    def shuffle(self, cards: []):
        shuffled_cards = []
        while cards:
            rand_num = random.randint(0, len(cards) - 1)
            shuffled_cards.append(cards[rand_num])
            cards.remove(cards[rand_num])

        return shuffled_cards

    def draw_top_card(self, cards: []):
        return cards.pop()

    def distribute_cards_to_players(self, cards: [], start_hand_count: int, player_count: int):
        player_hands = []

        # initialize an empty hand for each player
        counter = 0
        while counter != player_count:
            player_hands.append([])
            counter += 1

        # distribute a card to each hand until the last hand has reached the starting hand count
        player_index = player_count
        while len(player_hands[player_count - 1]) != start_hand_count:
            card = cards.pop()
            player_hands[player_count - player_index].append(card)
            if player_index == 1:
                player_index = player_count
            else:
                player_index -= 1

        # return the player hands and the remaining cards
        return player_hands, cards


