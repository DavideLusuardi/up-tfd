from unified_planning.io import PDDLReader
from unified_planning.shortcuts import *
import pytest


def test_matchcellar():
    domain_filename = 'pddl/matchcellar/domain.pddl'
    problem_filename = 'pddl/matchcellar/problem.pddl'
    reader = PDDLReader()
    problem = reader.parse_problem(domain_filename, problem_filename)

    with OneshotPlanner(name='tfd', problem_kind=problem.kind) as planner:
        assert(planner is not None)
        plan = planner.solve(problem).plan
        assert(plan is not None)
        assert(len(plan.timed_actions) == 6)
