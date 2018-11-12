# -*- coding: utf-8 -*-
# ---------------------------------------
# AUTHOR: Hadir Garcia-Castro
# E-MAIL: hadir.garcia@usp.br
# DATE: March 24th, 2018 - May 13th, 2018
# Copyright (C) 2018, hadir.ga
# All rights reserved.
# MIT License (see LICENSE.lic for details)
# ---------------------------------------


from .util import read_file

class Instance(object):
    def __init__(self):
        """
        Empty Instance object.

        No Parameters.
        """
        self.id = -1
        self.name = 'null'  # string
        self.nnodes = 0  # int, Qty of nodes 'V'.
        self.ncities = 0  # int, Qty of cities 'I' to be visited.
        self.xlng = []  # list of int
        self.ylat = []  # list of int


    def load(self, name):
        """
        The instance data is loaded from the instance's id text file .

        Parameters
        ----------
        name : string
            It is the name ID of the instance to be processed.
        """
        self.id = id
        self.name = name
        _data = read_file(self.name)
        _row = 6  # the instance data starts at line 6
        self.nnodes = int(_data[3][1])  # Qty of nodes 'V'.
        self.ncities = int(_data[3][1])  # Qty of cities 'I' to be visited.
        self.xlng = [int(_data[_row + i][1]) for i in range(self.nnodes)]
        self.ylat = [int(_data[_row + i][2]) for i in range(self.nnodes)]


class Solution(object):

    def __init__(self, problem_name, soln_type):
        """
        Empty Solution object with especific 'name' and 'soln_type' values.

        Parameters
        ----------
        problem_name: str
            The problem's name solved in this solution.
        soln_type: str
            It can be an 'Exact Solution' or a 'Heuristic Solution'.
        """
        self.name = problem_name
        self.category = soln_type  # Exact or heuristics
        self.status = 'null'  # code
        self.sequence = []  # list
        self.cost_total = 0  # ObjVal in GUROBI
        self.runtime = 0  # time spent to find the solution
        self.gap = 99.99

    def print_results(self):
        """
        parameter
            solution: class
        """
        print('Name:', self.name)
        print('Category:', self.category)
        print('Status:', self.status)
        print('Runtime:', round(int(self.runtime * 10000)/10000, 5))
        print('GAP:', self.gap)
        print('Total Cost:', self.cost_total)
        print('Sequence:', self.sequence)




#EOF
