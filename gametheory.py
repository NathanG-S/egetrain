from functools import lru_cache


# 1 куча камней
def moves(h):
    return h + 1, h + 4, h * 5


@lru_cache(None)
def game(h):
    if h >= 68: return 'W'
    # if h > 60: return 'P1' запладка если есть ограничение в каком промежутке будет выигрыш
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'  # Меняем на any если первый ход пети неудачный
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 200):
    if game(s) == 'B2':
        print(s)
