---
title: "An MIP model for the TSP with gurobipy"
author: "Hadir Garcia-Castro"
date: 2018-10-22T16:32:58.713
description: "Math formulation and algorithms to solve the TSP."
type: technical_note
draft: false
---
# An MIP model for the TSP with gurobipy
This is the model for the TSP wrote in Python and using the Gurobi solver.
The model builds the optimal exact route between a set of cities.
It has as parameters:


```python
- `inst` an object of type Instance
- `soln` an object of type Solution

See the model:
```

## preliminaries

Loads the required packages:


```python
import os
from gurobipy import *
from datetime import datetime
```

Imports auxiliary objects:


```python
from util.classes import Instance, Solution
from util.util import mtx_distance
```

And the model...


```python
instance = Instance.load("lin105.tsp")
soln = Solution('TSP', 'MIP Solution')

n = instance.nnodes  # the number of cities in the problem.
distance = mtx_distance(instance.xlng, instance.ylat, scale=100)  # Distance btw (i,j)

print(n)
print(distance)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-fa6ea7e6eaa8> in <module>()
    ----> 1 instance = Instance.load("lin105.tsp")
          2 soln = Solution('TSP', 'MIP Solution')
          3 
          4 n = instance.nnodes  # the number of cities in the problem.
          5 distance = mtx_distance(instance.xlng, instance.ylat, scale=100)  # Distance btw (i,j)
    

    TypeError: load() missing 1 required positional argument: 'id'



```python
# Gurobi model for the TSP
try:
    # Initialize the Traveling Salesman Problem Model
    tsp = Model('TSP')
    tsp.params.LazyConstraints = 1
    #tsp.params.Threads = 4
    tsp.params.TimeLimit = 100
    # tsp.params.MIPGap = 0
    tsp.params.LogToConsole = 1

    # DECISION VARIABLES
    # -------------------------------------------------------
    # x[i, j] = binary variable,
    # equals to 1 if edge (i,j) is traversed, and 0 otherwise.
    x = {(i, j): tsp.addVar(
        lb=0.0,
        ub=1.0,
        obj=0.0,
        vtype=GRB.BINARY,
        name='x_{}_{}'.format(i, j))
        for i in range(n) for j in range(n)
    }
    # u[i, j] = integer variable, to avoid subtours.
    u = {(i, j): tsp.addVar(
        lb=0.0,
        ub=GRB.INFINITY,
        obj=0.0,
        vtype=GRB.CONTINUOUS,
        name='u_{}_{}'.format(i, j))
        for i in range(n) for j in range(n)
    }
    tsp.update()

    # Decision: 1 to include constraints, 0 otherwise
    cstr = {'1' : 1,
            '2' : 1,
            '3' : 1,
            '4' : 1,
            '5' : 1,
            '6' : 1,
            '7' : 1,
            '8' : 1}

    # CONSTRAINTS 1
    # -------------------------------------------------------
    if cstr['1']:
        # Ensures that the route starts at beginning customer.
        i = 0
        expr = LinExpr()
        for j in range(1, n):
            expr.addTerms(coeffs=[1.0], vars=[x[i, j]])

        tsp.addConstr(expr == 1, name='cstr1_{}'.format(i))

    # CONSTRAINTS 2
    # -------------------------------------------------------
    if cstr['2']:
        # Ensures that the route ends at beginning customer.
        j = 0
        expr = LinExpr()
        for i in range(1, n):
            expr.addTerms(coeffs=[1.0], vars=[x[i, j]])

        tsp.addConstr(expr == 1, name='cstr2_{}'.format(j))

    # CONSTRAINTS 3
    # ---------------------------------------------------
    if cstr['3']:
        # Ensures that customer 'j' is visited.
        for j in range(1, n):
            expr = LinExpr()
            for i in range(n):
                if i != j:
                    expr.addTerms(coeffs=[1.0], vars=[x[i, j]])

            tsp.addConstr(expr == 1, name='cstr3_{}'.format(j))

    # CONSTRAINTS 4
    # ---------------------------------------------------
    if cstr['4']:
        # Ensures that route exits customer 'j'.
        for i in range(1, n):
            expr = LinExpr()
            for j in range(n):
                if i != j:
                    expr.addTerms(coeffs=[1.0], vars=[x[i, j]])

            tsp.addConstr(expr == 1, name='cstr4_{}'.format(i))

    # CONSTRAINTS 5
    # ---------------------------------------------------
    if cstr['5']:
        # Eliminate subtours.
        for i in range(n):
            for j in range(n):
                expr = LinExpr()
                expr.addTerms(coeffs=[1.0, -(n - 1)], 
                              vars=[u[i, j], x[i, j]])
                tsp.addConstr(expr <= 0, name='cstr(5)_{}_{}'.format(i, j))

    # CONSTRAINTS 6
    # ---------------------------------------------------
    if cstr['6']:
        # Ensure s that ...
        i = 0
        expr = LinExpr()
        for j in range(1, n):
            expr.addTerms(coeffs=[1.0], vars=[u[i, j]])

        tsp.addConstr(expr == n - 1, name='cstr6_{}'.format(i))

    # CONSTRAINTS 7
    # ---------------------------------------------------
    if cstr['7']:
        # Ensures that ...
        for j in range(1, n):
            expr = LinExpr()
            for i in range(n):
                if i != j:
                    expr.addTerms(coeffs=[1.0, -1.0],
                                  vars=[u[i, j], u[j, i]])

            tsp.addConstr(expr == 1, name='cstr7_{}'.format(j))

    # CONSTRAINTS 8
    # ---------------------------------------------------
    if cstr['8']:
        # Ensures that ...
        for j in range(n):
            expr = LinExpr()
            expr.addTerms(coeffs=[1.0], vars=[x[j, j]])
            tsp.addConstr(expr <= 0, name='cstr8_{}'.format(j))

    tsp.update()

    # OBJECTIVE FUNCTION
    # -----------------------------------------------
    # Minimize the traveling costs for visiting each city.
    expr = LinExpr()
    for i in range(n):
        for j in range(n):
            # add open cost
            expr.addTerms(coeffs=distance[i][j], vars=x[i, j])

    tsp.setObjective(expr, sense=GRB.MINIMIZE)
    tsp.update()

    # Write the '.lp' model file
    path = os.path.abspath(r'./util/{date}_{id}_{name}.lp'.format(
        date=datetime.now().strftime('%Y%m%d_%H%M%S'),
        id=instance.id,
        name=instance.name))
    tsp.write(path)

    # Optimize model
    tsp.optimize()

    # Save problem's solution
    # -----------------------
    # build the TSP sequence route.
    sequence = []
    j0 = 0
    while len(sequence) < n:
        sequence.append(j0)
        for j1 in range(n):
            if int(x[j0, j1].x + 0.1) == 1:
                j0 = j1
                #sequence.append(j1)
                break
        # if len(sequence) == n:
        #     sequence.append(sequence[0])
    print(sequence)
    soln.status = tsp.status
    soln.sequence = sequence
    soln.cost_total = tsp.objVal
    soln.runtime = tsp.runtime
    soln.gap = tsp.MIPGap


except GurobiError:
    raise Exception('Error reported at Traveling Salesman Problem')
```

    Changed value of parameter LazyConstraints to 1
       Prev: 0  Min: 0  Max: 1  Default: 0
    Changed value of parameter TimeLimit to 100.0
       Prev: 1e+100  Min: 0.0  Max: 1e+100  Default: 1e+100
    Parameter LogToConsole unchanged
       Value: 1  Min: 0  Max: 1  Default: 1
    Optimize a model with 3 rows, 0 columns and 0 nonzeros
    Coefficient statistics:
      Matrix range     [0e+00, 0e+00]
      Objective range  [0e+00, 0e+00]
      Bounds range     [0e+00, 0e+00]
      RHS range        [1e+00, 1e+00]
    Presolve time: 0.32s
    
    Solved in 0 iterations and 0.32 seconds
    Infeasible model
    []
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-13-bd89780d5ad8> in <module>()
        179     soln.status = tsp.status
        180     soln.sequence = sequence
    --> 181     soln.cost_total = tsp.objVal
        182     soln.runtime = tsp.runtime
        183     soln.gap = tsp.MIPGap
    

    model.pxi in gurobipy.Model.__getattr__ (../../src/python/gurobipy.c:53450)()
    

    model.pxi in gurobipy.Model.getAttr (../../src/python/gurobipy.c:68468)()
    

    model.pxi in gurobipy.Model.__gettypedattr (../../src/python/gurobipy.c:106359)()
    

    AttributeError: b"Unable to retrieve attribute 'objVal'"


Running the model:


```python
mip_tsp(Instance)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-9-8d9d04ca7922> in <module>()
    ----> 1 mip_tsp(Instance)
    

    <ipython-input-8-4e374f0f04d7> in mip_tsp(instance)
         13     """
         14 
    ---> 15     n = instance.nnodes  # the number of cities in the problem.
         16     distance = mtx_distance(instance.xlng, instance.ylat, scale=100)  # Distance btw (i,j)
         17 
    

    AttributeError: type object 'Instance' has no attribute 'nnodes'

