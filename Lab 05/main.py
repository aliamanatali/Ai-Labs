import random

class EightQueensState:
    def __init__(self, state):
        self.state = state
        self.value = self.calculate_attacking_pairs()

    def calculate_attacking_pairs(self):
        attacking_pairs = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if self.state[i] == self.state[j] or abs(self.state[i] - self.state[j]) == abs(i - j):
                    attacking_pairs += 1
        return attacking_pairs

    def generate_successors(self):
        successors = []
        for i in range(8):
            for j in range(1, 9):
                if j != self.state[i]:
                    successor_state = list(self.state)
                    successor_state[i] = j
                    successors.append(EightQueensState(successor_state))
        return successors

    def is_solution(self):
        return self.value == 0

    def print_state(self):
        for i in range(8):
            row = ['Q' if j == self.state[i] else '.' for j in range(1, 9)]
            print(' '.join(row))
        print()


# def hill_climbing():
#     current_state = EightQueensState([random.randint(1, 8) for _ in range(8)])
#     states_explored = [current_state.state]
#     iterations = 0

#     while iterations < 100:
#         neighbors = current_state.generate_successors()
#         best_neighbor = min(neighbors, key=lambda neighbor: neighbor.value)

#         if best_neighbor.value >= current_state.value:
#             return states_explored

#         current_state = best_neighbor
#         states_explored.append(current_state.state)
#         iterations += 1

#     return states_explored[:100]

def hill_climbing():
    current_state = EightQueensState([random.randint(1, 8) for _ in range(8)])
    best_state = current_state
    iterations = 0

    while iterations < 100:
        neighbors = current_state.generate_successors()
        best_neighbor = min(neighbors, key=lambda neighbor: neighbor.value)

        if best_neighbor.value >= current_state.value:
            return best_state.state

        current_state = best_neighbor
        if current_state.value < best_state.value:
            best_state = current_state
        iterations += 1

    return best_state.state
# Solve the 8-queens problem using hill climbing
# solution_states = hill_climbing()

# Check if a valid solution is found
# last_state = EightQueensState(solution_states[-1])


# if last_state.is_solution():
#     print("Valid solution found!")
# else:
#     print("Solution not found within 100 iterations.")
#TO find min collision
min_collision_state = hill_climbing()
min_collision_state_obj = EightQueensState(min_collision_state)
min_collision_state_obj.print_state()

# Print all explored states
# for state in solution_states:
#     current_state = EightQueensState(state)
#     current_state.print_state()
#     print('-' * 17)  # Separator between states