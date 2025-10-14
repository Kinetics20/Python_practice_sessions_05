from typing import Any


class ChessCoordinate:
    _interned: dict[Any, Any] = {}

    def __new__(cls, file, rank):
        key = (file, rank)

        if key not in cls._interned:
            self = super().__new__(cls)
            self._file = file
            self._rank = rank
            cls._interned[key] = self

        return cls._interned[key]

    # def __init__(self, file, rank):
    #     # print(f'id(self) = {id(self)}')
    #     self._file = file
    #     self._rank = rank

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f'{self.file}{self.rank}'

    def __repr__(self):
        return f'{type(self).__name__}(file={self.file}, rank={self.rank})'


def starting_board():
    return {
        # ♔ White figures
        'white_king': ChessCoordinate('e', 1),
        'white_queen': ChessCoordinate('d', 1),
        'white_rook_1': ChessCoordinate('a', 1),
        'white_rook_2': ChessCoordinate('h', 1),
        'white_bishop_1': ChessCoordinate('c', 1),
        'white_bishop_2': ChessCoordinate('f', 1),
        'white_knight_1': ChessCoordinate('b', 1),
        'white_knight_2': ChessCoordinate('g', 1),
        'white_pawn_a': ChessCoordinate('a', 2),
        'white_pawn_b': ChessCoordinate('b', 2),
        'white_pawn_c': ChessCoordinate('c', 2),
        'white_pawn_d': ChessCoordinate('d', 2),
        'white_pawn_e': ChessCoordinate('e', 2),
        'white_pawn_f': ChessCoordinate('f', 2),
        'white_pawn_g': ChessCoordinate('g', 2),
        'white_pawn_h': ChessCoordinate('h', 2),

        # ♚ Black figures
        'black_king': ChessCoordinate('e', 8),
        'black_queen': ChessCoordinate('d', 8),
        'black_rook_1': ChessCoordinate('a', 8),
        'black_rook_2': ChessCoordinate('h', 8),
        'black_bishop_1': ChessCoordinate('c', 8),
        'black_bishop_2': ChessCoordinate('f', 8),
        'black_knight_1': ChessCoordinate('b', 8),
        'black_knight_2': ChessCoordinate('g', 8),
        'black_pawn_a': ChessCoordinate('a', 7),
        'black_pawn_b': ChessCoordinate('b', 7),
        'black_pawn_c': ChessCoordinate('c', 7),
        'black_pawn_d': ChessCoordinate('d', 7),
        'black_pawn_e': ChessCoordinate('e', 7),
        'black_pawn_f': ChessCoordinate('f', 7),
        'black_pawn_g': ChessCoordinate('g', 7),
        'black_pawn_h': ChessCoordinate('h', 7),
    }


def main():
    import tracemalloc
    tracemalloc.start()

    boards = [starting_board() for _ in range(10000)]

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_kb = peak / 10 ** 3
    print(f'{peak_kb:.0f} kB')


if __name__ == '__main__':
    main()
