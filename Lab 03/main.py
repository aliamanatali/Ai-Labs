import queue
from collections import deque

# Open file and read data

with open("Lab 03\input.txt", "r") as file:
    firstLine = file.readline().split(' ')

    # read numberOfState, numberOfActions, testCases count
    numberOfStates = int(firstLine[0])
    numberOfActions = int(firstLine[1])
    testCases = int(firstLine[2])

    file.readline()  # read space line

   # read state space from file
    stateSpace = list()
    for _ in range(numberOfStates):
        stateSpaceLine = file.readline()
        stateSpace.append(stateSpaceLine.strip('\n'))

    file.readline()  # read space line

    # read actions from file
    actionList = list()
    for _ in range(numberOfActions):
        actionList.append(file.readline().strip('\n'))  # read action

    file.readline()  # read space line

    # read the state space matrix
    stateMatrix = list()
    for _ in range(numberOfStates):
        line = ((file.readline().strip('\n')).split(' '))  # read state
        stateMatrix.append([int(state) for state in line])

    file.readline()  # read space line

    # test cases
    test_cases = list()
    for i in range(testCases):
        line = (file.readline().strip('\n')).split('\t')
        test_cases.append(
            (stateSpace.index(line[0]), stateSpace.index(line[1])))

class Node:
    def __init__(self, state, action, cost, parent):
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent


class Problem:
    def __init__(self, state_matrix, initial_state, goal):
        self.state_matrix = state_matrix
        self.initial_state = initial_state
        self.goal = goal

    def goal_test(self, state):
        return self.goal == state

    def actions(self, state):
        return self.state_matrix[state]


def child_node(problem, node, action):
    state_list = problem.state_matrix[node.state]
    new_state_index = state_list.index(action)
    return Node(state_list[new_state_index], state_list[state_list.index(action)], node.cost+1, node)


def insert(child, frontier):
    frontier.append(child)


def solution(node):
    path = []
    while node.parent != None:
        path.append(node.action)
        node = node.parent
    path.append(node.state)
    path.reverse()
    return path


def breadth_first_search(problem):
    node = Node(problem.initial_state, None, 0, None)

    if problem.goal_test(node.state):
        return solution(node)

    frontier = deque()
    frontier.append(node)
    explorer = set()

    while len(frontier) != 0:
        node = frontier.popleft()
        explorer.add(node.state)
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if child.state not in explorer and child not in frontier:
                if problem.goal_test(child.state):
                    return solution(child)
                insert(child, frontier)

    return "Failure"


def display_path(path):
    for i in path:
            print(f"{i}", end=" -> ")
    print("finish", end="")
    print('\n')

def main():

    for test_case in test_cases:
        print(f"Initial State: {test_case[0]}   Goal: {test_case[1]}")
        problem = Problem(stateMatrix, test_case[0], test_case[1])
        path = breadth_first_search(problem)
        if path == "Failure":
            print("Failure")
            return

        display_path(path)

main()
