import math
import random
import time

import basic_players


class Card:

    # n should be in [0, 3 ^ dimensions).
    def __init__(self, n, dimensions):
        self.values = [math.floor(n / (3 ** i)) % 3 for i in range(dimensions)]


class Game:

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.helper = basic_players.Jason()

    def run(self, player):
        card_numbers = list(range(3 ** self.dimensions))
        random.shuffle(card_numbers)
        visible_cards = []
        done = False
        success = True
        player_time = 0
        while True:
            while len(visible_cards) < 12 or not self._has_set(visible_cards):
                if not card_numbers:
                    done = True
                    break
                for i in range(3):
                    visible_cards.append(
                        Card(card_numbers.pop(), self.dimensions))
            if done:
                break
            start = time.time()
            found_set = player.find_set(visible_cards)
            end = time.time()
            if not self._is_set(found_set):
                success = False
            for card in found_set:
                visible_cards.remove(card)
            player_time += end - start
        return player_time if success else None

    def _has_set(self, cards):
        return self.helper.find_set(cards) is not None

    def _is_set(self, cards):
        return not any(
            sum(c.values[i] for c in cards) % 3 for i in range(self.dimensions)
        )
