import numpy as np


def taxicab_distance(p, q):
    """Return the taxicab distance between vectors p and q.
    Args:
    p, q: np.arrays with shape 1 x n
    """
    return np.sum(np.abs(p - q))


def compute_displacement(input, heading):
    """Return delta, the change in Cartesian coordinates and heading, the
    new heading, which result from the action described in input,
    given the current heading
    """
    heading_dict = {'N': 1, 'E': 2, 'S': 3, 'W': 0}
    unit_vectors_dict = {1: [0, 1], 2: [1, 0], 3: [0, -1], 0: [-1, 0]}
    turn_direction = input[0]
    if turn_direction == 'R':
        turn = 1
    elif turn_direction == 'L':
        turn = -1
    distance = int(input[1:])
    print heading
    new_heading = heading_dict[heading] + turn
    delta = distance * unit_vectors_dict[new_heading]
    return np.array(delta), new_heading

def form_vector(input):
    """Return vector v, resulting from applying the sequence of inputs in
    input
    Returns:
    v: two dimensional np.array
    """
    hdg = 'N'
    position = np.array([0, 0])
    for i in input:
        delta, hdg  = compute_displacement(i, hdg)
        position += delta
    return position


input = 'R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3'

input = input.split(', ')
easter_bunny_position = form_vector(input)
landing_position = np.array([0, 0])
print taxicab_distance(landing_position, easter_bunny_position)
