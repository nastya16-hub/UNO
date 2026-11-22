from game.deck import Deck
from game.player import Player
from game.rules import can_play_card, check_winner, get_next_player_index
from game.special_cards import apply_special_card

class Game:
    def __init__(self, player_names):

        # Создаём колоду
        self.deck = Deck()

        # Создаём игроков
        self.players = [Player(name) for name in player_names]

        # Определяем количество игроков
        self.players_count = len(self.players)

        # Индекс текущего игрока
        self.current_player_index = 0

        # Направление игры
        self.direction = 1

        # Верхняя карта на столе
        self.top_card = None

        # Текущий цвет игры
        self.current_color = None

        # Победитель
        self.winner = None

        # Дополнительный ход
        self.extra_turn = False

        # Начинаем игру
        self.start_game()

    # Начало игры
    def start_game(self):

        # Раздаём каждому игроку по 7 карт
        for player in self.players:
            player.draw_cards(self.deck, 7)

        # Выкладываем первую карту на стол
        self.top_card = self.deck.draw_card()

        if self.top_card is not None:
            self.current_color = self.top_card.color

    # Получение текущего игрока
    def get_current_player(self):
        return self.players[self.current_player_index]

    # Взятие карты
    def draw_card(self):

        player = self.get_current_player()

        card = self.deck.draw_card()

        if card is not None:
            player.add_card(card)

        return card

    # Выкладывание карты
    def play_card(self, card_index, target_player_index=None):

        player = self.get_current_player()

        # Проверяем правильность индекса карты
        if card_index < 0 or card_index >= len(player.hand):
            return False

        card = player.hand[card_index]

        # Проверяем, можно ли выложить карту
        if not can_play_card(card, self.top_card, self.current_color):
            return False

        # Убираем карту из руки игрока
        played_card = player.play_card(card_index)

        # Кладём карту на стол
        self.top_card = played_card

        # Обновляем текущий цвет
        if played_card.color != "black":
            self.current_color = played_card.color

        # Обрабатываем новые специальные карты
        if played_card.value in ["steal_card", "swap_hands", "double_turn"]:

            target_player = None

            if target_player_index is not None:
                if 0 <= target_player_index < self.players_count:
                    target_player = self.players[target_player_index]

            result = apply_special_card(
                played_card,
                player,
                target_player
            )

            if played_card.value == "double_turn":
                self.extra_turn = True

        # Проверяем победителя
        self.winner = check_winner(self.players)

        # Если дополнительного хода нет, переключаем игрока
        if not self.extra_turn and self.winner is None:
            self.next_turn()

        return True

    # Переход к следующему игроку
    def next_turn(self):

        self.current_player_index = get_next_player_index(
            self.current_player_index,
            self.players_count,
            self.direction
        )

    # Проверка наличия победителя
    def check_game_over(self):

        self.winner = check_winner(self.players)

        return self.winner is not None

    # Получение информации об игре
    def get_game_info(self):

        return {
            "current_player": self.get_current_player().name,
            "top_card": str(self.top_card),
            "current_color": self.current_color,
            "players": {
                player.name: player.card_count()
                for player in self.players
            },
            "winner": self.winner.name if self.winner else None
        }