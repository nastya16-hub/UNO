#СОЗДАНИЕ ОТДЕЛЬНЫХ КАРТ
class Card:
    def __init__(self, color, value, card_type="normal"):
        self.color = color # цвет карты
        self.value = value # значение карты
        self.card_type = card_type # тип карты

    def __str__(self):
        return f"{self.color} {self.value}"

    def __repr__(self):
        return f"Card({self.color}, {self.value})"

    def is_special(self):
        return self.card_type != "normal"

    def get_info(self):
        return {
            "color": self.color,
            "value": self.value,
            "type": self.card_type
        }

# Доступные цвета карт
COLORS = ["red", "blue", "green", "yellow"]

# Специальные карты
SPECIAL_CARDS = [
    "skip",              # Пропуск хода
    "reverse",           # Изменение направления
    "draw_two",          # Взять две карты
    "wild",              # Смена цвета
    "wild_draw_four",    # Смена цвета + четыре карты
    "steal_card",        # Кража случайной карты
    "swap_hands",        # Обмен всеми картами
    "double_turn"        # Двойной ход
]