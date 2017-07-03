from collections import defaultdict


class BasePlayer:

    def find_set(self, cards):
        raise NotImplementedError

    def _is_set(self, cards):
        if len(cards) != 3:
            return False
        dimensions = len(cards[0].values)
        return not any(
            sum(c.values[i] for c in cards) % 3 for i in range(dimensions)
        )


class StupidPlayer(BasePlayer):

    def find_set(self, cards):
        for i in range(len(cards)):
            for j in range(len(cards)):
                for k in range(len(cards)):
                    if i == j or j == k or i == k:
                        continue
                    candidate = [cards[i], cards[j], cards[k]]
                    if self._is_set(candidate):
                        return candidate
        return None


class NaivePlayer(BasePlayer):

    def find_set(self, cards):
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                for k in range(j + 1, len(cards)):
                    candidate = [cards[i], cards[j], cards[k]]
                    if self._is_set(candidate):
                        return candidate
        return None


class Jason(BasePlayer):

    def find_set(self, cards):
        value_to_cards = defaultdict(list)
        for card in cards:
            value_to_cards[card.values[0]].append(card)

        # Look for sets where all cards have the same attribute 0.
        for value in [0, 1, 2]:
            found_set = self._naive_find_set(value_to_cards[value])
            if found_set is not None:
                return found_set

        # Look for sets where all cards have different attribute 0.
        for card0 in value_to_cards[0]:
            for card1 in value_to_cards[1]:
                for card2 in value_to_cards[2]:
                    candidate = [card0, card1, card2]
                    if self._is_set(candidate):
                        return candidate
        return None

    def _naive_find_set(self, cards):
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                for k in range(j + 1, len(cards)):
                    candidate = [cards[i], cards[j], cards[k]]
                    if self._is_set(candidate):
                        return candidate
        return None
