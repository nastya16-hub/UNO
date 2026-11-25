import pygame

from interface.buttons import Button

class GameScreen:

    def __init__(self, screen, game):

        # Игровое окно
        self.screen = screen

        # Объект игры
        self.game = game

        # Размеры экрана
        self.width = screen.get_width()
        self.height = screen.get_height()

        # Шрифты
        self.title_font = pygame.font.SysFont("arial", 36, bold=True)
        self.font = pygame.font.SysFont("arial", 24)
        self.card_font = pygame.font.SysFont("arial", 20, bold=True)

        # Цвета
        self.background_color = (35, 40, 65)
        self.text_color = (255, 255, 255)

        # Кнопка взятия карты
        self.draw_button = Button(
            self.width - 250,
            self.height - 100,
            200,
            60,
            "Взять карту",
            self.font
        )

        # Кнопка возврата в меню
        self.menu_button = Button(
            30,
            30,
            180,
            50,
            "В меню",
            self.font
        )

        # Прямоугольники карт игрока
        self.card_rects = []

    # Отображение игрового экрана
    def draw(self):

        # Очищаем экран
        self.screen.fill(self.background_color)

        # Получаем текущего игрока
        current_player = self.game.get_current_player()

        # Заголовок
        title = self.title_font.render(
            "UNO",
            True,
            self.text_color
        )

        self.screen.blit(title, (self.width // 2 - 40, 30))

        # Информация о текущем игроке
        player_text = self.font.render(
            f"Ход игрока: {current_player.name}",
            True,
            self.text_color
        )

        self.screen.blit(player_text, (30, 110))

        # Отображение верхней карты
        self.draw_top_card()

        # Отображение количества карт игроков
        self.draw_players_info()

        # Отображение карт текущего игрока
        self.draw_player_hand()

        # Отображение кнопок
        self.draw_button.draw(self.screen)
        self.menu_button.draw(self.screen)

    # Отображение верхней карты на столе
    def draw_top_card(self):

        if self.game.top_card is None:
            return

        card = self.game.top_card

        colors = {
            "red": (220, 50, 50),
            "blue": (50, 90, 220),
            "green": (40, 160, 80),
            "yellow": (230, 200, 40),
            "black": (30, 30, 30)
        }

        card_color = colors.get(card.color, (100, 100, 100))

        card_rect = pygame.Rect(
            self.width // 2 - 50,
            self.height // 2 - 100,
            100,
            150
        )

        pygame.draw.rect(
            self.screen,
            card_color,
            card_rect,
            border_radius=12
        )

        card_text = self.card_font.render(
            str(card.value),
            True,
            self.text_color
        )

        text_rect = card_text.get_rect(
            center=card_rect.center
        )

        self.screen.blit(card_text, text_rect)

        label = self.font.render(
            "Карта на столе",
            True,
            self.text_color
        )

        self.screen.blit(
            label,
            (self.width // 2 - 75, self.height // 2 + 65)
        )

    # Отображение информации об игроках
    def draw_players_info(self):

        y = 180

        for player in self.game.players:

            player_text = self.font.render(
                f"{player.name}: {player.card_count()} карт",
                True,
                self.text_color
            )

            self.screen.blit(player_text, (30, y))

            y += 35

    # Отображение карт текущего игрока
    def draw_player_hand(self):

        player = self.game.get_current_player()

        self.card_rects = []

        card_width = 70
        card_height = 105
        card_spacing = 15

        hand = player.hand

        total_width = (
            len(hand) * (card_width + card_spacing) - card_spacing
        )

        start_x = max(
            20,(self.width - total_width) // 2
        )

        y = self.height - card_height - 30

        colors = {
            "red": (220, 50, 50),
            "blue": (50, 90, 220),
            "green": (40, 160, 80),
            "yellow": (230, 200, 40),
            "black": (30, 30, 30)
        }

        for index, card in enumerate(hand):

            x = start_x + index * (card_width + card_spacing)

            card_rect = pygame.Rect(
                x,
                y,
                card_width,
                card_height
            )

            self.card_rects.append(card_rect)

            card_color = colors.get(
                card.color,
                (100, 100, 100)
            )

            pygame.draw.rect(
                self.screen,
                card_color,
                card_rect,
                border_radius=8
            )

            card_text = self.card_font.render(
                str(card.value),
                True,
                self.text_color
            )

            text_rect = card_text.get_rect(
                center=card_rect.center
            )

            self.screen.blit(card_text, text_rect)

    # Обработка действий игрока
    def handle_event(self, event):

        # Нажатие на кнопку возврата в меню
        if self.menu_button.is_clicked(event):
            return "menu"

        # Нажатие на кнопку взятия карты
        if self.draw_button.is_clicked(event):

            self.game.draw_card()
            self.game.next_turn()

            return "draw"

        # Проверяем нажатие на карты игрока
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                for index, card_rect in enumerate(self.card_rects):

                    if card_rect.collidepoint(event.pos):

                        if self.game.play_card(index):
                            return "played"

        return None