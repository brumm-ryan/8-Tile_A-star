import math
import heapq

import numpy as np

# same method as print_succ but doesn't print off the successors and returns them as a list


def get_succ(state):
    numpy_state = np.reshape(state, (3, 3))
    succ_list = []  # list of 3 x 3 states
    succ_1D_list = []  # list of 1 dimensional states
    x = 0
    y = 0
    succ = None
    # find where the current 0 is in state
    for i in range(3):
        for j in range(3):
            if numpy_state[i][j] == 0:
                x = i
                y = j
                break
    # check if 0 can slide down
    if 0 <= x + 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x + 1][y]
        succ[x + 1][y] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())
        # print(succ)
    # check if 0 can slide up
    if 0 <= x - 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x - 1][y]
        succ[x - 1][y] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())
        # print(succ)
    # check if 0 can slide right
    if 0 <= y + 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x][y + 1]
        succ[x][y + 1] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())
        # print(succ)
    # check if 0 can slide left
    if 0 <= y - 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x][y - 1]
        succ[x][y - 1] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())

    succ_1D_list.sort()
    return succ_1D_list


def print_succ(state):

    # prints off a list of successors

    numpy_state = np.reshape(state, (3, 3))
    succ_list = []  # list of 3 x 3 states
    succ_1D_list = []  # list of 1 dimensional states
    x = 0
    y = 0
    succ = None
    # find where the current 0 is in state
    for i in range(3):
        for j in range(3):
            if numpy_state[i][j] == 0:
                x = i
                y = j
                break
    # check if 0 can slide down
    if 0 <= x + 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x + 1][y]
        succ[x + 1][y] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())
        # print(succ)
    # check if 0 can slide up
    if 0 <= x - 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x - 1][y]
        succ[x - 1][y] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())
        # print(succ)
    # check if 0 can slide right
    if 0 <= y + 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x][y + 1]
        succ[x][y + 1] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())
        # print(succ)
    # check if 0 can slide left
    if 0 <= y - 1 < 3:
        succ = np.copy(numpy_state)
        temp = succ[x][y]
        succ[x][y] = succ[x][y - 1]
        succ[x][y - 1] = temp
        succ_list.append(succ)
        succ_1D_list.append(succ.flatten().tolist())

    succ_1D_list.sort()
    for arr in succ_1D_list:
        hValue = calculate_manhattan(arr)
        print(str(arr) + " h=" + str(hValue))
    return succ_1D_list


def calculate_manhattan(current):
    solution = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # reshape current state and solution to 3 x 3 arrays
    numpy_solution = np.reshape(solution, (3, 3))
    numpy_current = np.reshape(current, (3, 3))
    hValue = 0
    xCord = 0
    yCord = 0
    # iterate through all tiles 1-9 to find individual hValues
    for x in range(1, 9):
        # where int x should be is xCord and yCord
        xCord = (x - 1) % 3
        yCord = math.floor((x - 1) / 3)
        # find where int x is in current state
        for i in range(3):
            for j in range(3):
                if numpy_current[j][i] == x:
                    # take the manhattan difference and add to hValue
                    hValue += abs(i - xCord) + abs(j - yCord)
    return hValue


def solve(state):
    #  solves the 8-tile problem using A* algorithm
    pq = []
    # set to track if we've already visited this state
    s = set()
    # initialize parent state
    parentState = -1
    # the solution state we're searching for
    solution = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # find the initial hValue of the start state
    hValue = calculate_manhattan(state)
    # gValue tracks the number of moves we've made in the path
    gValue = 0
    # track all states that have been visited to later reconstruct path
    visited_states = list()
    # the final path to the solution
    path = list()
    stateInfo = None
    # heap push the starting state
    heapq.heappush(pq, (hValue + gValue, state, (gValue, hValue, parentState)))
    # until solution path is found continue iterating
    while True:
        # get highest priority (lowest h + g value) from queue
        stateInfo = heapq.heappop(pq)
        state = stateInfo[1]
        gValue = stateInfo[2][0]
        # add the current state to the list of states
        visited_states.append(stateInfo)
        # calculate parent state index to assign to successor states
        parentState = len(visited_states) - 1
        # get list of successor states
        # next_state_lists = print_succ(state)
        next_state_lists = get_succ(state)
        # add current state to set to track if we've visited it
        s.add(tuple(state))
        # if the current state is a solution state exit loop
        if np.array_equal(solution, state):
            break
        # iterate over each successor
        for states in next_state_lists:
            # calculate successor hvalues
            next_h_value = calculate_manhattan(states)
            # if state isn't visited add it to pq
            if tuple(states) not in s:
                heapq.heappush(pq, (next_h_value + gValue + 1, states, (gValue + 1, next_h_value, parentState)))
    # iterate up successful paths to get total path
    while parentState != -1:
        currentState = visited_states[parentState]
        path.append(currentState)
        parentState = currentState[2][2]
    # flip path since its backwards
    path.reverse()
    # print off state info for each state from start to finish
    for paths in path:
        print(str(paths[1]) + " h=" + str(paths[2][1]) + " moves: " + str(paths[2][0]))

