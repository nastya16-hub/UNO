class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    # Добавление одной карты игроку
    def add_card(self, card):
        self.hand.append(card)
    # Добавление нескольких карт игроку
    def add_cards(self, cards):
        self.hand.extend(cards)
    # Взятие карт из колоды
    def draw_cards(self, deck, amount = 1):
        drawn_cards = []
        for _ in range(amount):
            card = deck.draw_card()
            if card is None: # Если колода закончилась
                break
            self.add_card(card)
            drawn_cards.append(card)
        return drawn_cards
    # Выкладывание карты из руки
    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None
    # Проверка, остались ли карты у игрока
    def has_cards(self):
        return len(self.hand) > 0
    # Количество карт на руке
    def card_count(self):
        return len(self.hand)
    # Получение всех карт игрока
    def get_hand(self):
        return self.hand
    # Отображение карт игрока
    def show_hand(self):
        print(f"\nКарты игрока {self.name}:")
        for index, card in enumerate(self.hand):
            print(f"{index + 1}. {card}")
    def __str__(self):
        return f"Игрок {self.name}, карт на руке: {len(self.hand)}"