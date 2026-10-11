
# search.py
# ---------
# Licensing Information: You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology, an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """Returns the start state for the search problem."""
        util.raiseNotDefined()

    def isGoalState(self, state):
        """Returns True if and only if the state is a valid goal state."""
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
        Returns a list of triples:
        (successor, action, stepCost).
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """Returns the total cost of a sequence of legal actions."""
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.
    For any other maze, the sequence will be incorrect.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST

    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """Search the deepest nodes in the search tree first."""

    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    visited = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if state in visited:
            continue

        if problem.isGoalState(state):
            return actions

        visited.add(state)

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                frontier.push((successor, actions + [action]))

    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    frontier = util.Queue()
    frontier.push((problem.getStartState(), []))
    visited = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if state in visited:
            continue

        if problem.isGoalState(state):
            return actions

        visited.add(state)

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                frontier.push((successor, actions + [action]))

    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    frontier = util.PriorityQueue()
    start = problem.getStartState()

    frontier.push((start, [], 0), 0)
    expanded = set()

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        if state in expanded:
            continue

        if problem.isGoalState(state):
            return actions

        expanded.add(state)

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in expanded:
                new_cost = cost + stepCost
                new_actions = actions + [action]

                frontier.push(
                    (successor, new_actions, new_cost),
                    new_cost
                )

    return []


def nullHeuristic(state, problem=None):
    """
    Estimates the cost from the current state to the nearest goal.
    This heuristic is trivial and always returns zero.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node with the lowest combined cost and heuristic first."""

    frontier = util.PriorityQueue()
    start = problem.getStartState()

    frontier.push(
        (start, [], 0),
        heuristic(start, problem)
    )

    expanded = set()

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        if state in expanded:
            continue

        if problem.isGoalState(state):
            return actions

        expanded.add(state)

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in expanded:
                new_cost = cost + stepCost
                new_actions = actions + [action]

                priority = new_cost + heuristic(successor, problem)

                frontier.push(
                    (successor, new_actions, new_cost),
                    priority
                )

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

