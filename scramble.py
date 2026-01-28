import rotation
import random

def scramble_cube(cube_state, moves_count):
    # Apply a series of moves to scramble the cube
    possible_moves = ['U', "U'", 'D', "D'", 'R', "R'", 'L', "L'", 'F', "F'", 'B', "B'"]
    moves = []
    for i in range(moves_count):
        # Randomly select a move
        move = random.choice(possible_moves)
        moves.append(move)
    for move in moves:
        if move == 'U':
            cube_state = rotation.top_clockwise(cube_state)
        elif move == "U'":
            cube_state = rotation.top_counter_clockwise(cube_state)
        elif move == 'D':
            cube_state = rotation.bottom_clockwise(cube_state)
        elif move == "D'":
            cube_state = rotation.bottom_counter_clockwise(cube_state)
        elif move == 'R':
            cube_state = rotation.right_clockwise(cube_state)
        elif move == "R'":
            cube_state = rotation.right_counter_clockwise(cube_state)
        elif move == 'L':
            cube_state = rotation.left_clockwise(cube_state)
        elif move == "L'":
            cube_state = rotation.left_counter_clockwise(cube_state)
        elif move == 'F':
            cube_state = rotation.front_clockwise(cube_state)
        elif move == "F'":
            cube_state = rotation.front_counter_clockwise(cube_state)
        elif move == 'B':
            cube_state = rotation.back_clockwise(cube_state)
        elif move == "B'":
            cube_state = rotation.back_counter_clockwise(cube_state)

    return { cube_state, moves }