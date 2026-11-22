# Проверка, можно ли выложить карту
def can_play_card(card, top_card, current_color=None):

    # Универсальные карты можно выкладывать всегда
    if card.value in ["wild", "wild_draw_four"]:
        return True

    # Новые специальные карты можно выкладывать всегда
    if card.value in ["steal_card", "swap_hands", "double_turn"]:
        return True

    # Определяем текущий цвет игры
    if current_color is None:
        current_color = top_card.color

    # Проверяем совпадение цвета
    if card.color == current_color:
        return True

    # Проверяем совпадение значения карты
    if card.value == top_card.value:
        return True

    # Если ни одно условие не выполнено,
    # карту выкладывать нельзя
    return False

# Проверка окончания игры
def check_winner(players):

    for player in players:

        if len(player.hand) == 0:
            return player

    return None

# Получение индекса следующего игрока
def get_next_player_index(current_index, players_count, direction=1):

    next_index = current_index + direction

    # Если вышли за границы списка игроков
    if next_index >= players_count:
        next_index = 0

    elif next_index < 0:
        next_index = players_count - 1

    return next_index

# Проверка, есть ли у игрока подходящие карты
def has_playable_cards(player, top_card, current_color=None):

    for card in player.hand:

        if can_play_card(card, top_card, current_color):
            return True

    return False