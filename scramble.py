import rotation

def scramble_cube(cube_state, moves):
    # Apply a series of moves to scramble the cube
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

    return cube_state