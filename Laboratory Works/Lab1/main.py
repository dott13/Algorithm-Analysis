import numpy as np
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from decimal import Decimal, getcontext, Context, ROUND_HALF_EVEN
import sys

def execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Recursion
def fib_recursion(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)

#Itterative
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Dynamic programming
def fib_dynamic(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

#Binet formula
def fib_binet(n):
    ctx = Context(prec = 60, rounding =ROUND_HALF_EVEN)
    phi = Decimal((1 + Decimal(5**(1/2))))
    phi2 = Decimal((1 - Decimal(5**(1/2))))

    return int((ctx.power(phi, Decimal(n)) - ctx.power(phi2,Decimal(n))) / (2**n * Decimal(5**(1/2))))

# Array
def fib_array(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i - 1] + data[i - 2])
    return data[n - 1]

#Matrix
def fib_matrix(n):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    M = [[1, 1], [1, 0]]
    for i in range(2, n + 1):
        multiply(F, M)

MOD = 1000000007
table = PrettyTable()
sys.setrecursionlimit(10**6)  

list = [1, 5, 10, 15, 20, 25, 30]
big_list = [501, 600, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 8000, 10000, 12500, 15000, 100000]

execution_func = {'Recursive': fib_recursion, 'Iterative': fib_iterative, 'Dynamic': fib_dynamic, 'Binet': fib_binet, 'Array': fib_array, 'Matrix': fib_matrix}
execution_times = {'Recursive': [], 'Iterative': [], 'Dynamic': [], 'Binet': [], 'Array' : [], 'Matrix': []}

name = 'Recursive'


for n in list:
    _,timee = execution_time(execution_func[name], n)
    execution_times[name].append(timee)

plt.plot(list, execution_times[name], label=name, marker='o')

plt.xlabel('Number')
plt.ylabel('Execution Time (sec)')
plt.title(f'{name} Fibonacci Algorithms')
plt.legend()
plt.show()

table.field_names = ["Number", "Execution Time (sec)"]
for n, exec_time in zip(list, execution_times[name]):
    table.add_row([n, exec_time])

# Print the table
print(table)