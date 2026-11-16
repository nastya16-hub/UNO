# Steal Card - кража случайной карты у соперника.
# Swap Hands - обмен всеми картами ссоперником.
# Double Turn - возможность сделать два хода подряд.

import random

# Кража случайной карты у другого игрока
def steal_card(current_player, target_player):
    if not target_player.hand:
        return None

    card_index = random.randrange(len(target_player.hand))

    stolen_card = target_player.hand.pop(card_index)

    current_player.add_card(stolen_card)

    return stolen_card

# Обмен всеми картами между двумя игроками
def swap_hands(player1, player2):
    player1.hand, player2.hand = player2.hand, player1.hand

# Дополнительный ход игрока
def double_turn():
    return 1

# Выполнение специальной карты
def apply_special_card(card, current_player, target_player=None):

    if card.value == "steal_card":
        if target_player is None:
            return None

        return steal_card(current_player, target_player)

    elif card.value == "swap_hands":
        if target_player is None:
            return False

        swap_hands(current_player, target_player)
        return True

    elif card.value == "double_turn":
        return double_turn()

    return None