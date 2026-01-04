import copy

def top_clockwise(cube_state):

    # Helper function to change colors during rotation
    def change_colors(colors):
        colors[5], colors[0], colors[4], colors[1] = colors[0], colors[4], colors[1], colors[5]
        return colors
    
    # Main function logic
    # Create a deep copy of cube_state to avoid mutating the original
    new_state = copy.deepcopy(cube_state)

    # Build the locations matrix for the pieces on top face
    locations_matrix = []
    for i in range(3, 0, -1):
        locations_vector = []
        for j in range(1, 4, 1):
            locations_vector.append(9*j - i)
        locations_matrix.append(locations_vector)

    # Create the rotation matrix by first transposing locations_matrix
    rotation_matrix = []
    for i in range(3):
        locations_vector = []
        for j in range(3):
            locations_vector.append(locations_matrix[j][i])
        rotation_matrix.append(locations_vector)

    # Complete the rotation matrix by swapping first and third columns
    for i in range(3):
        rotation_matrix[i][0], rotation_matrix[i][2] = rotation_matrix[i][2], rotation_matrix[i][0]

    # Update new_state based on rotation
    for i in range(3):
        for j in range(3):
            # Find new position of the piece at locations_matrix[i][j]
            new_i, new_j = None, None
            for m in range(3):
                for n in range(3):
                    if rotation_matrix[m][n] == locations_matrix[i][j]:
                        new_i, new_j = m, n

            # Update the piece's position by changing colors in new_state
            new_state[locations_matrix[new_i][new_j]]["colors"] = change_colors(cube_state[locations_matrix[i][j]]["colors"].copy())

    return new_state
