from gurobipy import *
import math

N = 6
px = [30,37,49,52,20,40]
py = [40,52,49,64,26,30]
d = [0,7,30,16,9,21]
V = 5

# Distance
c = {}
for i in range(N):
    for j in range(N):
        c[i,j] = math.sqrt((px[i]-px[j])*(px[i]-px[j]) + (py[i]-py[j])*(py[i]-py[j]))


try: 
    m = Model('name')

    # Variáveis de decisão
    x = {}
    for i in range(N):
        for j in range(N):
            for k in range(1,N):
                name = f"x_{i}_{j}_{k}"
                x[i,j,k] = m.addVar(0.0, 1.0, c[i,j], GRB.BINARY, name)


    #88888888888888888888888888888888888888888888
    #888        Subject to
    #88888888888888888888888888888888888888888888 

    # Constraint 02
    for j in range(1,N):
        expr = LinExpr()
        for i in range(N):
            if i != j:
                for k in range(1,N):
                    expr.addTerms(1.0, x[i,j,k])
        name = f"c02_{j}"
        m.addConstr(expr == 1, name)

    # Constraint 03
    for k in range(1,N):
        expr = LinExpr()
        for j in range(N):
            expr.addTerms(1.0, x[0,j,k])
        name = f"c03_{k}"
        m.addConstr(expr == 1, name)        
    
   # Constraint 04
    for k in range(1,N):
        expr = LinExpr()
        for i in range(N):
            expr.addTerms(1.0, x[i,0,k])
        name = f"c04_{k}"
        m.addConstr(expr == 1, name)   

    # Constraint 05...09
    
    m.optimize()
    m.update()

    for i in range(N):
        for j in range(N):
            for k in range(1,N):
                print(f"x[{i},{j},{k}] = ", x[i,j,k].x)

    print("Obj Value = ", m.ObjVal)
                
except GurobiError:
    print('Error reported at Compound Assignment Model')
