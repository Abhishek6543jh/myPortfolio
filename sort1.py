def min_steps_to_overlap(M, N, pos1, dir1, pos2, dir2):
    def will_overlap(pos1, pos2, dir1, dir2):
        # Calculate relative positions after one step
        new_pos1 = [pos1[0] + dir1[0], pos1[1] + dir1[1]]
        new_pos2 = [pos2[0] + dir2[0], pos2[1] + dir2[1]]

        # Check if the relative positions match
        return new_pos1 == new_pos2

    # Check if the balls are already overlapping
    if pos1 == pos2:
        return 0

    # Simulate until they overlap or a large number of steps are taken
    for steps in range(1, M * N + 1):
        # Check if the balls will overlap after the next step
        if will_overlap(pos1, pos2, dir1, dir2):
            return steps

        # Update positions after one step
        pos1 = [pos1[0] + dir1[0], pos1[1] + dir1[1]]
        pos2 = [pos2[0] + dir2[0], pos2[1] + dir2[1]]

        # Update directions if the balls hit a wall
        if pos1[0] == 0 or pos1[0] == M - 1:
            dir1[0] *= -1
        if pos1[1] == 0 or pos1[1] == N - 1:
            dir1[1] *= -1

        if pos2[0] == 0 or pos2[0] == M - 1:
            dir2[0] *= -1
        if pos2[1] == 0 or pos2[1] == N - 1:
            dir2[1] *= -1

    return "Never"

# Input
M, N = map(int, input().strip().split())
pos1 = list(map(int, input().strip().split()))
dir1 = list(map(int, input().strip().split()))
pos2 = list(map(int, input().strip().split()))
dir2 = list(map(int, input().strip().split()))

# Output
result = min_steps_to_overlap(M, N, pos1, dir1, pos2, dir2)
print(result)
