import pygame

class Button:

    def __init__(self, x, y, width, height, text, font):

        # Положение и размеры кнопки
        self.rect = pygame.Rect(x, y, width, height)

        # Текст кнопки
        self.text = text

        # Шрифт
        self.font = font

        # Цвета кнопки
        self.color = (60, 90, 150)
        self.hover_color = (90, 130, 200)
        self.text_color = (255, 255, 255)

    # Отрисовка кнопки
    def draw(self, screen):

        # Получаем положение мыши
        mouse_pos = pygame.mouse.get_pos()

        # Проверяем, наведена ли мышь на кнопку
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        # Рисуем кнопку
        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )

        # Создаём текст
        text_surface = self.font.render(
            self.text,
            True,
            self.text_color
        )

        # Размещаем текст по центру кнопки
        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        # Отображаем текст
        screen.blit(text_surface, text_rect)

    # Проверка нажатия кнопки
    def is_clicked(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if self.rect.collidepoint(event.pos):
                    return True

        return False