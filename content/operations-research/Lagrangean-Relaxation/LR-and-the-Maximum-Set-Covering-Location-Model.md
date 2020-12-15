---
title: "LR and the Maximum Set Covering Location Model"
author: "Hadir Garcia-Castro"
date: 2018-12-02T22:18:54.713
type: technical_note
draft: false
---
# Summary: Chapter 4 - Covering Problems
## Lagrangian Relaxation: An Optimization-Based Heuristic Algorithm for Solving the Maximum Covering Location Model
*Reference:* [Daskin, M.S., 2013. Network and discrete location: models, algorithms, and applications. John Wiley & Sons, New Jersey, 2nd edition.](https://daskin.engin.umich.edu/network-discrete-location/)


The Lagrangian Relaxation (LR) provides an upper bound on the value of the objective function. Daskin1986 associates it with a substitution algorithm and obtains better results.

The LR is an approach to solving difficult problems like MIP problems. In this chapter, the author uses it to solve a maximization problem, the steps are called the *Subgradient Optimization*:

1. Relax one or more constraints. The relaxed problem should be solved easily for fixed values of the lagrange multipliers $\pi_i$.
2. Solve the resulting relaxed problem to find the optimal values of the original decision variables, but in the relaxed problem.
3. Use the values of the decision variables to find a feasible solution to the original problem. It is easily. Just update the lower bound on the best feasible solution known for the problem.
4. Use the solution obtained in #2 to compute an upper bound on the best value of the objective function.
5. Examinate the solution in #2 to determine which of the relaxed constraints are violated. Modify the lagrange multipliers to obtain less likely violated results on the subsequent iteration.

For each new lagrangian multiplicator, return to #2.

### The formulation of the problem

#### Inputs
Parameter | Description
:---      | :---
$h_i$     | demand at node $i\in I$
$P$       | number of facilities to locate
$a_{ij}$  | equal to $1$, if candidate $j \in J$ can cover demands at node $i \in I$<br>equal to $0$, if not

#### Decision variables
Variable | Description
:---     | :---
$Z_i$    | equal to $1$, if node $i \in I$ is covered <br>equal to $0$, if not
$X_j$    | equal to $1$, if we locate a facility at candidate site $j \in J$ <br>equal to $0$, if not

#### Objective function
$$
max \quad \sum_{i\in I} h_i Z_i
$$
#### Subject to

[c1]
$$
Z_i \leq \sum_{j\in J} a_{ij} X_j \quad \forall\ i\in I
$$
[c2]
$$
\sum_{j\in J} X_j \leq P
$$
[c3]
$$
X_j\in\{0,1\} \quad \forall\ j\in J
$$
[c4]
$$
Z_i\in\{0,1\} \quad \forall\ i\in I
$$

The constraint [c1] is the complicated one, because the association of the two variables $X_j$ and $Z_i$.

**[NOTE]** Other kind of problems may not have the same performace after relaxing constraints that link decision variables. Many problems have multiple relaxations to be made and many needs to be tested to determine which performs best.

### The formulation of the relaxed problem
Objective function
$$
min_{\pi} \quad max_{X,Z} \quad \sum_{i\in I} h_i Z_i + \sum_{i\in I}\pi_i \left(\sum_{j\in J} a_{ij} X_j - Z_i\right)
$$
Subject to

[c2]
$$
\sum_{j\in J} X_j \leq P
$$
[c3]
$$
X_j\in\{0,1\} \quad \forall\ j\in J
$$
[c4]
$$
Z_i\in\{0,1\} \quad \forall\ i\in I
$$

At this point it is necessay to maximize the objective function with respect to the decision variables $Z_i$ and $X_i$ and minimize with respect to the lagrangian variable $\pi_i$

*[NOTE]* The formulation must has a lagrangian multiplier for each of the relaxed constraints.

Since constraint [c1] applies to all values of $ i\in I$, the lagrangian multipliers $\pi_i$ must be indexed by $i\in I$

### After combining the $Z_i$ terms
Objective function
$$
min_{\pi} \quad max_{X,Z} \quad \sum_{i\in I} (h_i - \pi_i) Z_i + \sum_{j\in J}\left(\sum_{i\in I} a_{ij} \pi_i \right) X_j
$$
Subject to

[c2]
$$
\sum_{j\in J} X_j \leq P
$$
[c3]
$$
X_j\in\{0,1\} \quad \forall\ j\in J
$$
[c4]
$$
Z_i\in\{0,1\} \quad \forall\ i\in I
$$
[c5]
$$
\pi_i\geq 0 \quad \forall\ i\in I
$$

Since the relaxing constraint is an inequality, the lagrange multipliers $\pi_i$ are constrained to be nonnegative.

The optimal solution of the decision variables for the Lagrangian problem is greater or equal to the Lagrangian Objective Function for any other set of decision variables that satisfy the constraints, and it is greater or equal to the optimal solution of the original problem.

In this case, as the original problem must to be *maximized* the optimal solution of the Lagrangian problem is an upper bound of the original problem.

### Solving the relaxed problem
A solition of the problem is given by fixing the values of the lagrangian multipliers, and decomposing the problem for $Z_i$ and $X_j$.

The solution of $Z_i$ is: equal to $1$, if $h_i-\pi_i > 0$ and $0$, if not.

To solve $X_j$, needs to find the $P$ largest coefficients of $X_j$, that is the value of $\sum_{i \in I} a_{ij} \pi_i$, where $\pi_i$ is equal to the demand $h_i$ and $a_ij$ is a given input.

As the problem is all integer, the optimal solution found by solve the Lagrangia problem, will no be better then the one found by solving the LP of the relaxation.

### Finding a feasible solution and a lower bound
As the values of $Z_i$ and $X_j$ found from solving the subproblems are not likely feasible for the original problem.
They likely violate the relaxed constraint. 
It is easily to find a feasible solution by finding the total demand that is covered by the $P$ sites whose $X_j = 1$
LEt be $LB^n$ the lower bound of the iteration $n$, then take the largest one to be the best lower bound.

### Finding an upper bound
The values of the $\pi_i$ give an upper bound on the solution to the original problem.
The values of the upper bound need not decrese from iteration to iteration, but must not increase.
The best upper bound is the smallest.

### Updating the lagrange multipliers
The methods used to update the $\pi_i$ is the subgradient optimization.

The basic idea is:
> For fixed values of the decision variables, $Z_i$ and $X_j$ we want to find values of $\pi_i$ that minimize the lagrangian function.

Begin by compute the stepsize:
$$
t^n = \frac{\alpha^n(U^n-LB)}{\sum_{i\in I}\left\{\left(\sum_{j\in J}a_{ij} X_j^n\right)-Z_i^n\right\}^2}
$$
The denominator is the square of the difference between the number of times node $i$ is covered for each variable $X_j$ and $Z_i$.
Usually $\alpha^1 = 2$.

This stepsize will updates the $\piì$ by:
$$
\pi_i^{n+1} = max\left\{0,\pi_i^n - t^n \left(\sum_{j\in J}a_{ij}X_j^n-Z_i^n\right)\right\}
$$
Note that, if $\sum_{j\in J}a_{ij}X_j^n > Z_i^n$, then $\pi_i^n$ will be decrease, and the reverse case $\sum_{j\in J}a_{ij}X_j^n < Z_i^n$ will increase $\pi_i^n$

### Modifying the constant $\alpha^n$
The value of $\alpha^n$ is reduced by the half if the upper bound $U^n$ has not decreased in a given number of consecutive iterations.
Often 4 consecutive iterations without decreasing it. However it can be more or less according to the problem.

### Termination
The algorithm terminates when one of the conditions is true:
1. The limit number of iterations is reached.
2. The $LB = U^n$ or is close enough to it.
3. The $\alpha^n$ becomes small. For very small values of $\alpha^n$ the $\pi_i$ changes will be very small, and such small chages are not likely to help solve the problem.

### Example

Lagrangean relaxation for the MSCLM in Julia


```julia
# Inputs
cov_distance = 10
nnodes = 6
h = [10,8,22,18,7,55] # demand
distance= [
    # A  B  C  D  E   F
    [ 0  8 15 10 99 99] # A
    [ 8  0 12  7 16 99] # B
    [15 12  0 99  9 11] # C
    [10  7 99  0 11 17] # D
    [99 16  9 11  0 13] # E
    [99 99 11 17 13  0] # F
]

function a(i,j)
   if distance[i,j] <= cov_distance
        return 1
    else
        return 0
    end
end

function append_sort!(list,value1,value2)
    newlist = vcat(list, [value1 value2])
    sortslices(newlist, dims=1)   
    return newlist
end;
```


```julia
# Iterated process
niter = 10

LB = Array{Int64}(undef,0,2)
UB = Array{Int64}(undef,0,2)
π = 0

count_iter = 0
while count_iter < niter
    count_iter += 1
    
    
    
    
    
end
print("end")
```

    end
