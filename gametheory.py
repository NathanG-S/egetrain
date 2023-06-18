from functools import lru_cache

# 1 куча камней
def moves(h):
    return h + 1, h *2


@lru_cache(None)
def game(h):
    if h >= 153: return 'W'
    # if h > 60: return 'P1' запладка если есть ограничение в каком промежутке будет выигрыш
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'  # Меняем на any если первый ход пети неудачный и ваня выиграл первым ходом. 19 номер
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 200):
    if game(s) == 'B2':
        print(s)



# 2 кучи камней

def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 77: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 200):
    h = 8, s
    if game(h) == 'B1':
        print(s)
