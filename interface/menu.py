import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen

        # Размеры экрана
        self.width = screen.get_width()
        self.height = screen.get_height()

        # Шрифты
        self.title_font = pygame.font.SysFont("arial", 64, bold=True)
        self.button_font = pygame.font.SysFont("arial", 32)

        # Цвета
        self.background_color = (35, 40, 65)
        self.button_color = (60, 90, 150)
        self.button_hover_color = (90, 130, 200)
        self.text_color = (255, 255, 255)

        # Создание кнопок
        button_width = 280
        button_height = 65

        center_x = self.width // 2
        start_y = self.height // 2 - 20

        self.buttons = {
            "start": pygame.Rect(
                center_x - button_width // 2,
                start_y,
                button_width,
                button_height
            ),

            "rules": pygame.Rect(
                center_x - button_width // 2,
                start_y + 90,
                button_width,
                button_height
            ),

            "quit": pygame.Rect(
                center_x - button_width // 2,
                start_y + 180,
                button_width,
                button_height
            )
        }

    # Отрисовка меню
    def draw(self):

        # Фон
        self.screen.fill(self.background_color)

        # Заголовок
        title = self.title_font.render("UNO", True, self.text_color)

        title_rect = title.get_rect(
            center=(self.width // 2, self.height // 4)
        )

        self.screen.blit(title, title_rect)

        # Названия кнопок
        button_names = {
            "start": "Начать игру",
            "rules": "Правила",
            "quit": "Выход"
        }

        mouse_pos = pygame.mouse.get_pos()

        # Отрисовка каждой кнопки
        for button_name, button_rect in self.buttons.items():

            # Проверяем, наведена ли мышь на кнопку
            if button_rect.collidepoint(mouse_pos):
                color = self.button_hover_color
            else:
                color = self.button_color

            # Рисуем кнопку
            pygame.draw.rect(
                self.screen,
                color,
                button_rect,
                border_radius=12
            )

            # Создаём текст кнопки
            text = self.button_font.render(
                button_names[button_name],
                True,
                self.text_color
            )

            # Размещаем текст по центру кнопки
            text_rect = text.get_rect(
                center=button_rect.center
            )

            self.screen.blit(text, text_rect)

    # Обработка нажатий мыши
    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                for button_name, button_rect in self.buttons.items():

                    if button_rect.collidepoint(event.pos):

                        return button_name

        return None