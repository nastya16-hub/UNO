# СОЗДАНИЕ ВСЕЙ КОЛОДЫ
import random
from game.card import Card, COLORS, SPECIAL_CARDS

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        # Создание обычных карт
        for color in COLORS:
            # Карта с нулём
            self.cards.append(Card(color, 0))

            # Карты от 1 до 9 (по две каждого значения)
            for value in range(1, 10):
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))

            # Обычные специальные карты
            for special in ["skip", "reverse", "draw_two"]:
                self.cards.append(Card(color, special, "special"))
                self.cards.append(Card(color, special, "special"))

        # Универсальные специальные карты
        for special in ["wild", "wild_draw_four"]:
            for _ in range(4):
                self.cards.append(Card("black", special, "special"))

        # Новые специальные карты
        for special in ["steal_card", "swap_hands", "double_turn"]:
            for _ in range(2):
                self.cards.append(Card("black", special, "special"))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None

        return self.cards.pop()

    def remaining_cards(self):
        return len(self.cards)

    def __str__(self):
        return f"Колода содержит {len(self.cards)} карт"