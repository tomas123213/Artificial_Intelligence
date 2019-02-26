from Project1.utils.framework import Puzzle
from copy import deepcopy

SIZE = 5

LIGHTSOUT = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1]
]


class Lightsout(Puzzle):

    # Constructor
    def __init__(self, grid=LIGHTSOUT):
        self.grid = grid

    # Games are equal if grids are equal
    def __eq__(self, other):
        return self.grid == other

    # Hash the grid
    def __hash__(self):
        return hash(str(self.grid))

    # Heuristic compare makes this easy
    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    # Game is done when our conflicts equal 0
    def solved(self):
        return self.heuristic() == 0

    # The tiles that are 1's (light up) are a conflict.
    def heuristic(self):
        conflicts = 0
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c] == 1:
                    conflicts += 1

        return conflicts

    # Every coordinate is a possible move
    def moves(self):
        moves = list()

        for r in range(SIZE):
            for c in range(SIZE):
                moves.append((r, c))

        return moves

    def neighbor(self, move):
        # Get the row number and column number from the move
        (dr, dc) = move

        # Deep copy a new grid
        new_grid = deepcopy(self.grid)

        # Update the new grid with new move
        self.switch(new_grid, dr, dc)

        # Pass the new grid with a new object
        return Lightsout(new_grid)

    # Function to make the appropriate move
    # It changes the clicked spot and its neighbors
    # 0 ^= 1  turns a 0 into a 1
    # 1 ^= 1 turns a 1 into a 0
    @staticmethod
    def switch(new_grid, dr, dc):

        # The new move is somewhere in the middle rows
        if 0 < dr < SIZE - 1:
            # We are in the middle columns
            if 0 < dc < SIZE - 1:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch the value above
                new_grid[dr - 1][dc] ^= 1
                # Switch the value below
                new_grid[dr + 1][dc] ^= 1
                # Switch the value to the left
                new_grid[dr][dc - 1] ^= 1
                # Switch the value to the right
                new_grid[dr][dc + 1] ^= 1

            # We are in the first column but not corners
            elif dc == 0:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch the value above
                new_grid[dr - 1][dc] ^= 1
                # Switch the value below
                new_grid[dr + 1][dc] ^= 1
                # Switch the value to the right
                new_grid[dr][dc + 1] ^= 1

            # We are in the last column but not corners
            elif dc == SIZE - 1:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch the value to the left
                new_grid[dr][dc - 1] ^= 1
                # Switch the value above
                new_grid[dr - 1][dc] ^= 1
                # Switch the value below
                new_grid[dr + 1][dc] ^= 1

        # We are in the first row only
        elif dr == 0:
            # We are in the top left corner
            if dc == 0:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch the value to the right
                new_grid[dr][dc + 1] ^= 1
                # Switch the value below it
                new_grid[dr + 1][dc] ^= 1

            # We are in the top right corner
            elif dc == SIZE - 1:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                #  Switch the value to the left
                new_grid[dr][dc - 1] ^= 1
                # Switch the value below it
                new_grid[dr + 1][dc] ^= 1

            # We are in first row but not corners
            elif 0 < dc < SIZE - 1:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch value to the left
                new_grid[dr][dc - 1] ^= 1
                # Switch value to the right
                new_grid[dr][dc + 1] ^= 1
                # Switch value under it
                new_grid[dr + 1][dc] ^= 1

        # We are in the last row only
        elif dr == SIZE - 1:
            # We are in the bottom left corner
            if dc == 0:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Change the value above it
                new_grid[dr - 1][dc] ^= 1
                # Change the value to the right of it
                new_grid[dr][dc + 1] ^= 1

            # We are in the bottom right corner
            elif dc == SIZE - 1:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch the value above it
                new_grid[dr - 1][dc] ^= 1
                # Switch the value to the left of it
                new_grid[dr][dc - 1] ^= 1

            # We are in the last row but not corners
            elif 0 < dc < SIZE - 1:
                # Switch the current value
                new_grid[dr][dc] ^= 1
                # Switch the value to the left
                new_grid[dr][dc - 1] ^= 1
                # Switch the value to the right
                new_grid[dr][dc + 1] ^= 1
                # Switch the value above
                new_grid[dr - 1][dc] ^= 1

    # Display the board every turn
    def display(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if self.grid[r][c] == 0:
                    print("□", end='')
                elif self.grid[r][c] == 1:
                    print("▣", end='')
            print()
        print()
