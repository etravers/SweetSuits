from app.cardFunctions.cardFunctions import CardFunctions
import unittest


class TestCardFunctions(unittest.TestCase):

    def test_shuffle(self):
        cards = ['D3', 'SQ', 'HA', 'D9', 'CK', 'CJ', 'S2']
        shuffled_cards = CardFunctions.shuffle(self=self, cards=cards)
        assert(cards != shuffled_cards)

    def test_draw_top_card(self):
        cards = ['D3', 'SQ', 'HA', 'D9', 'CK', 'CJ', 'S2']
        top_card = CardFunctions.draw_top_card(self=self, cards=cards)
        assert(top_card == 'S2')

    def test_distribute_cards_to_players(self):
        cards = ['DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
                 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK']

        player_hands, remaining_cards = CardFunctions.distribute_cards_to_players(self=self, cards=cards,
                                                                                  start_hand_count=6, player_count=2)

        player_one_hand = player_hands[0]
        expected_hand = ['SK', 'SJ', 'S9', 'S7', 'S5', 'S3']
        expected_remaining = ['DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'SA']

        assert(player_one_hand == expected_hand)
        assert(remaining_cards == expected_remaining)


if __name__ == '__main__':
    unittest.main()
