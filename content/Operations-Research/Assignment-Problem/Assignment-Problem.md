---
title: "MIP for the Scheduling Problem"
author: "Hadir Garcia-Castro"
date: 2018-11-27T22:40:26.556
type: technical_note
draft: false
---
# MIP for the Scheduling Problem
We shows a MIP formulation and an example with optimal solution using the Gurobi solver for the Scheduling Problem.

Reference: Luh1990

## Decision variables
Variable      | Type    | Description
:---          | :---    | :---
$\delta_{ik}$ | Binary  | Equals to $1$ if job $i$ is active at time $k$
$B_i$         | Integer | Begining time of job $i$
$C_i$         | Integer | Completion time of job $i$
$T_i$         | Integer | Tardines of job $i$ equals $max\{0, C_i-D_i\}$


## Parameters
Parameter | Type    |Description
:---      | :---    | :---    
$D_i$     | Integer | Due date of job $i$
$K$       | Integer | Horizon under considerations, with $k$ indices
$M_k$     | Integer | Number of machines available at time $k$, with $k = 1,2,...,k$
$N$       | Integer | Number of jobs
$t_i$     | Integer | Time required from the resource by job $i$
$w_i$     | Integer | Weight/importance of job $i$

$$Min\ J \equiv \sum_i w_i Ti$$

[c1]
$$\sum_i \delta_{ik} \leq M_k, \quad k=1,2,...,K$$

[c2]
$$
C_i - B_i + 1 = t_i, \quad i=1,2,...,N
$$

## Example instance


```julia
module JSP

using DelimitedFiles: readdlm

mutable struct Instance
    author::String
    id::Int64
    name::String
    njobs::Int64
    khorizon::Int64
    nmachines::Int64
    timereq::Vector{Int64}
    due::Vector{Int64}
    weight::Vector{Int64}
    
    function Instance(author::String,id::Int64=1)
        filename::String = get_instance_name(author, id)
        instance::Instance = new(author, id, filename)
        load_data!(instance)
        return instance
    end
end


function get_instance_name(author::String, id::Int64)
    author_instances = Dict{String, Vector{String}}(
        "Luh1990" => [
            "example1.sp",
            "",
        ]
    )
    return author_instances[author][id]
end


function read_file(author::String, filename::String)
    readdlm("instances/$author/$filename")
end


function load_data!(P::Instance)
    data = read_file(P.author, P.name)
    P.njobs = data[1,2]
    P.khorizon = data[2,2]
    P.nmachines = data[3,2]
    P.timereq = zeros(Int64, P.njobs)
    P.due = zeros(Int64, P.njobs)
    P.weight = zeros(Int64, P.njobs)

    for i in 1:P.njobs
        line = 4 + i
        P.timereq[i] = data[line,1]
        P.due[i] = data[line,2]
        P.weight[i] = data[line,3]
    end
    Nothing
end
end # module
```

    WARNING: replacing module JSP.
    




    Main.JSP




```julia
using JuMP, Gurobi

P = JSP.Instance("Luh1990")
println(P)
try
    env = Gurobi.Env()

    solver = GurobiSolver(
        env,
        Presolve=0,
        TimeLimit=60,
        #IterationLimit=100,
        #MIPGap=0.00,
        #OutputFlag=0,
        LogToConsole=1,
        #LogFile=""
    )

    jsp = Model(solver=solver)
    
    @variables jsp begin
        𝛿[i=1:P.njobs,k=1:P.khorizon], Bin
        B[i=1:P.njobs] >= 0, Int
        C[i=1:P.njobs] >= 0, Int
        T[i=1:P.njobs] >= 0, Int
    end
    
    @objective(
        jsp,
        Min,
        sum(P.weight[i] * T[i] for i=1:P.njobs)
    )
    
    @constraint(
        jsp,
        c1[k=1:P.khorizon],
        sum(𝛿[i,k] for i=1:P.njobs) <= P.nmachines
    )
    
    @constraint(
        jsp,
        c2[i=1:P.njobs],
        C[i] - B[i] + 1  == P.timereq[i]
    )
    
    @constraint(
        jsp,
        c3[i=1:P.njobs],
        T[i] <= C[i] - P.due[i] 
    )
    
    println(jsp)
    
    status = solve(jsp)
    
    println("Optimal objective: ",getobjectivevalue(jsp))
    println("𝛿 = ", getvalue(𝛿))
    println("B = ", getvalue(B))
    println("C = ", getvalue(C))
    println("T = ", getvalue(T))

catch
    error("Error generating model.")
end
```

    Main.JSP.Instance("Luh1990", 1, "example1.sp", 12, 19, 2, [3, 1, 3, 2, 4, 4, 1, 3, 3, 3, 2, 4], [6, 5, 7, 9, 8, 8, 12, 11, 6, 6, 14, 12], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    Academic license - for non-commercial use only
    Min 2 T[1] + 2 T[2] + 2 T[3] + 2 T[4] + 2 T[5] + 2 T[6] + 2 T[7] + 2 T[8] + 2 T[9] + 2 T[10] + 2 T[11] + 2 T[12]
    Subject to
     𝛿[1,1] + 𝛿[2,1] + 𝛿[3,1] + 𝛿[4,1] + 𝛿[5,1] + 𝛿[6,1] + 𝛿[7,1] + 𝛿[8,1] + 𝛿[9,1] + 𝛿[10,1] + 𝛿[11,1] + 𝛿[12,1] <= 2
     𝛿[1,2] + 𝛿[2,2] + 𝛿[3,2] + 𝛿[4,2] + 𝛿[5,2] + 𝛿[6,2] + 𝛿[7,2] + 𝛿[8,2] + 𝛿[9,2] + 𝛿[10,2] + 𝛿[11,2] + 𝛿[12,2] <= 2
     𝛿[1,3] + 𝛿[2,3] + 𝛿[3,3] + 𝛿[4,3] + 𝛿[5,3] + 𝛿[6,3] + 𝛿[7,3] + 𝛿[8,3] + 𝛿[9,3] + 𝛿[10,3] + 𝛿[11,3] + 𝛿[12,3] <= 2
     𝛿[1,4] + 𝛿[2,4] + 𝛿[3,4] + 𝛿[4,4] + 𝛿[5,4] + 𝛿[6,4] + 𝛿[7,4] + 𝛿[8,4] + 𝛿[9,4] + 𝛿[10,4] + 𝛿[11,4] + 𝛿[12,4] <= 2
     𝛿[1,5] + 𝛿[2,5] + 𝛿[3,5] + 𝛿[4,5] + 𝛿[5,5] + 𝛿[6,5] + 𝛿[7,5] + 𝛿[8,5] + 𝛿[9,5] + 𝛿[10,5] + 𝛿[11,5] + 𝛿[12,5] <= 2
     𝛿[1,6] + 𝛿[2,6] + 𝛿[3,6] + 𝛿[4,6] + 𝛿[5,6] + 𝛿[6,6] + 𝛿[7,6] + 𝛿[8,6] + 𝛿[9,6] + 𝛿[10,6] + 𝛿[11,6] + 𝛿[12,6] <= 2
     𝛿[1,7] + 𝛿[2,7] + 𝛿[3,7] + 𝛿[4,7] + 𝛿[5,7] + 𝛿[6,7] + 𝛿[7,7] + 𝛿[8,7] + 𝛿[9,7] + 𝛿[10,7] + 𝛿[11,7] + 𝛿[12,7] <= 2
     𝛿[1,8] + 𝛿[2,8] + 𝛿[3,8] + 𝛿[4,8] + 𝛿[5,8] + 𝛿[6,8] + 𝛿[7,8] + 𝛿[8,8] + 𝛿[9,8] + 𝛿[10,8] + 𝛿[11,8] + 𝛿[12,8] <= 2
     𝛿[1,9] + 𝛿[2,9] + 𝛿[3,9] + 𝛿[4,9] + 𝛿[5,9] + 𝛿[6,9] + 𝛿[7,9] + 𝛿[8,9] + 𝛿[9,9] + 𝛿[10,9] + 𝛿[11,9] + 𝛿[12,9] <= 2
     𝛿[1,10] + 𝛿[2,10] + 𝛿[3,10] + 𝛿[4,10] + 𝛿[5,10] + 𝛿[6,10] + 𝛿[7,10] + 𝛿[8,10] + 𝛿[9,10] + 𝛿[10,10] + 𝛿[11,10] + 𝛿[12,10] <= 2
     𝛿[1,11] + 𝛿[2,11] + 𝛿[3,11] + 𝛿[4,11] + 𝛿[5,11] + 𝛿[6,11] + 𝛿[7,11] + 𝛿[8,11] + 𝛿[9,11] + 𝛿[10,11] + 𝛿[11,11] + 𝛿[12,11] <= 2
     𝛿[1,12] + 𝛿[2,12] + 𝛿[3,12] + 𝛿[4,12] + 𝛿[5,12] + 𝛿[6,12] + 𝛿[7,12] + 𝛿[8,12] + 𝛿[9,12] + 𝛿[10,12] + 𝛿[11,12] + 𝛿[12,12] <= 2
     𝛿[1,13] + 𝛿[2,13] + 𝛿[3,13] + 𝛿[4,13] + 𝛿[5,13] + 𝛿[6,13] + 𝛿[7,13] + 𝛿[8,13] + 𝛿[9,13] + 𝛿[10,13] + 𝛿[11,13] + 𝛿[12,13] <= 2
     𝛿[1,14] + 𝛿[2,14] + 𝛿[3,14] + 𝛿[4,14] + 𝛿[5,14] + 𝛿[6,14] + 𝛿[7,14] + 𝛿[8,14] + 𝛿[9,14] + 𝛿[10,14] + 𝛿[11,14] + 𝛿[12,14] <= 2
     𝛿[1,15] + 𝛿[2,15] + 𝛿[3,15] + 𝛿[4,15] + 𝛿[5,15] + 𝛿[6,15] + 𝛿[7,15] + 𝛿[8,15] + 𝛿[9,15] + 𝛿[10,15] + 𝛿[11,15] + 𝛿[12,15] <= 2
     𝛿[1,16] + 𝛿[2,16] + 𝛿[3,16] + 𝛿[4,16] + 𝛿[5,16] + 𝛿[6,16] + 𝛿[7,16] + 𝛿[8,16] + 𝛿[9,16] + 𝛿[10,16] + 𝛿[11,16] + 𝛿[12,16] <= 2
     𝛿[1,17] + 𝛿[2,17] + 𝛿[3,17] + 𝛿[4,17] + 𝛿[5,17] + 𝛿[6,17] + 𝛿[7,17] + 𝛿[8,17] + 𝛿[9,17] + 𝛿[10,17] + 𝛿[11,17] + 𝛿[12,17] <= 2
     𝛿[1,18] + 𝛿[2,18] + 𝛿[3,18] + 𝛿[4,18] + 𝛿[5,18] + 𝛿[6,18] + 𝛿[7,18] + 𝛿[8,18] + 𝛿[9,18] + 𝛿[10,18] + 𝛿[11,18] + 𝛿[12,18] <= 2
     𝛿[1,19] + 𝛿[2,19] + 𝛿[3,19] + 𝛿[4,19] + 𝛿[5,19] + 𝛿[6,19] + 𝛿[7,19] + 𝛿[8,19] + 𝛿[9,19] + 𝛿[10,19] + 𝛿[11,19] + 𝛿[12,19] <= 2
     C[1] - B[1] == 2
     C[2] - B[2] == 0
     C[3] - B[3] == 2
     C[4] - B[4] == 1
     C[5] - B[5] == 3
     C[6] - B[6] == 3
     C[7] - B[7] == 0
     C[8] - B[8] == 2
     C[9] - B[9] == 2
     C[10] - B[10] == 2
     C[11] - B[11] == 1
     C[12] - B[12] == 3
     T[1] - C[1] <= -6
     T[2] - C[2] <= -5
     T[3] - C[3] <= -7
     T[4] - C[4] <= -9
     T[5] - C[5] <= -8
     T[6] - C[6] <= -8
     T[7] - C[7] <= -12
     T[8] - C[8] <= -11
     T[9] - C[9] <= -6
     T[10] - C[10] <= -6
     T[11] - C[11] <= -14
     T[12] - C[12] <= -12
     𝛿[i,k] in {0,1} for all i in {1,2,..,11,12}, k in {1,2,..,18,19}
     B[i] >= 0, integer, for all i in {1,2,..,11,12}
     C[i] >= 0, integer, for all i in {1,2,..,11,12}
     T[i] >= 0, integer, for all i in {1,2,..,11,12}
    
    Optimize a model with 43 rows, 264 columns and 276 nonzeros
    Variable types: 0 continuous, 264 integer (228 binary)
    Coefficient statistics:
      Matrix range     [1e+00, 1e+00]
      Objective range  [2e+00, 2e+00]
      Bounds range     [1e+00, 1e+00]
      RHS range        [1e+00, 1e+01]
    Found heuristic solution: objective 0.0000000
    
    Explored 0 nodes (0 simplex iterations) in 0.00 seconds
    Thread count was 1 (of 8 available processors)
    
    Solution count 1: 0 
    
    Optimal solution found (tolerance 1.00e-04)
    Best objective 0.000000000000e+00, best bound 0.000000000000e+00, gap 0.0000%
    Optimal objective: 0.0
    𝛿 = [0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0; 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0]
    B = [4.0, 5.0, 5.0, 8.0, 5.0, 5.0, 12.0, 9.0, 4.0, 4.0, 13.0, 9.0]
    C = [6.0, 5.0, 7.0, 9.0, 8.0, 8.0, 12.0, 11.0, 6.0, 6.0, 14.0, 12.0]
    T = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    


```julia
?JSP.Instance
```




No documentation found.

# Summary

```
mutable struct Main.JSP.Instance <: Any
```

# Fields

```
author    :: String
id        :: Int64
name      :: String
njobs     :: Int64
khorizon  :: Int64
nmachines :: Int64
timereq   :: Array{Int64,1}
due       :: Array{Int64,1}
weight    :: Array{Int64,1}
```



