def top_clockwise(cube_state):
    #def change_colors
    # Rotate the top face clockwise
    new_state = cube_state[:]
    locations_matrix = []
    # Top face rotation
    for i in range(1, 4):
        locations_vector = []
        for j in range(1, 4):
            locations_vector.append((i, j))
        locations_matrix.append(locations_vector)
    # Take transpose of locations_matrix
    for i in range(3):
        for j in range(3):
            new_state[locations_matrix[j][2 - i][0] - 1 + (locations_matrix[j][2 - i][1] - 1) * 9] = cube_state[locations_matrix[i][j][0] - 1 + (locations_matrix[i][j][1] - 1) * 9]