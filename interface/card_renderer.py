import pygame

class CardRenderer:

    def __init__(self):

        # Цвета карт
        self.colors = {
            "red": (220, 50, 50),
            "blue": (50, 90, 220),
            "green": (40, 160, 80),
            "yellow": (230, 200, 40),
            "black": (30, 30, 30)
        }

        # Цвет текста
        self.text_color = (255, 255, 255)

        # Шрифт для карт
        self.font = pygame.font.SysFont("arial", 22, bold=True)

        # Шрифт для специальных карт
        self.special_font = pygame.font.SysFont("arial", 13, bold=True)

    # Отображение карты
    def draw_card(self, screen, card, x, y, width=80, height=120,
                  selected=False):

        # Создаём прямоугольник карты
        card_rect = pygame.Rect(x, y, width, height)

        # Получаем цвет карты
        card_color = self.colors.get(
            card.color,
            (100, 100, 100)
        )

        # Если карта выбрана, немного поднимаем её
        if selected:
            card_rect.y -= 15

        # Рисуем карту
        pygame.draw.rect(
            screen,
            card_color,
            card_rect,
            border_radius=10
        )

        # Рисуем внутреннюю рамку
        inner_rect = card_rect.inflate(-8, -8)

        pygame.draw.rect(
            screen,
            self.text_color,
            inner_rect,
            width=2,
            border_radius=8
        )

        # Получаем название карты
        card_name = str(card.value)

        # Выбираем шрифт в зависимости от типа карты
        if card.card_type == "special":
            font = self.special_font
        else:
            font = self.font

        # Создаём изображение текста
        text_surface = font.render(
            card_name,
            True,
            self.text_color
        )

        # Размещаем текст по центру карты
        text_rect = text_surface.get_rect(
            center=card_rect.center
        )

        screen.blit(text_surface, text_rect)

        return card_rect

    # Отображение рубашки карты
    def draw_card_back(self, screen, x, y, width=80, height=120):

        # Создаём прямоугольник карты
        card_rect = pygame.Rect(x, y, width, height)

        # Рисуем тёмно-синюю карту
        pygame.draw.rect(
            screen,
            (25, 35, 90),
            card_rect,
            border_radius=10
        )

        # Рисуем внутреннюю рамку
        inner_rect = card_rect.inflate(-8, -8)

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            inner_rect,
            width=2,
            border_radius=8
        )

        # Создаём надпись UNO
        text_surface = self.font.render(
            "UNO",
            True,
            (255, 255, 255)
        )

        # Размещаем надпись по центру
        text_rect = text_surface.get_rect(
            center=card_rect.center
        )

        screen.blit(text_surface, text_rect)

        return card_rect