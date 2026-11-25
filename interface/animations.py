import pygame

class CardAnimation:

    def __init__(self, card, start_pos, end_pos, duration=500):

        # Карта, которую нужно переместить
        self.card = card

        # Начальная позиция карты
        self.start_pos = start_pos

        # Конечная позиция карты
        self.end_pos = end_pos

        # Продолжительность анимации в миллисекундах
        self.duration = duration

        # Время, прошедшее с начала анимации
        self.elapsed_time = 0

        # Текущая позиция карты
        self.current_pos = start_pos

        # Состояние анимации
        self.finished = False

    # Обновление положения карты
    def update(self, delta_time):

        if self.finished:
            return

        # Увеличиваем прошедшее время
        self.elapsed_time += delta_time

        # Вычисляем прогресс анимации
        progress = min(
            self.elapsed_time / self.duration,
            1
        )

        # Вычисляем координату X
        x = self.start_pos[0] + (
            self.end_pos[0] - self.start_pos[0]
        ) * progress

        # Вычисляем координату Y
        y = self.start_pos[1] + (
            self.end_pos[1] - self.start_pos[1]
        ) * progress

        # Обновляем положение карты
        self.current_pos = (int(x), int(y))

        # Проверяем окончание анимации
        if progress >= 1:
            self.finished = True

    # Отображение движущейся карты
    def draw(self, screen, card_renderer):

        if not self.finished:

            card_renderer.draw_card(
                screen,
                self.card,
                self.current_pos[0],
                self.current_pos[1]
            )

    # Проверка окончания анимации
    def is_finished(self):

        return self.finished