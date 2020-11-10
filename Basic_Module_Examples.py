#!/usr/bin/env python3

# Testing inputs of multiple AD objects (shows that our implementation can handle arrays)
X = np.array([AD(1, 1), AD(2,1), AD(-1,1)])
y = np.array([AD(2, 0), AD(2, 0), AD(2, 0)])
f = np.sin(X**2 + 5)
print(len(f))
for solution in f:
    print(solution.val, solution.der)
    
x = AD(1, 1)
y = AD(2, 0)
f = np.sin(x**2 + y**3)
f.val
f.der

arr = [1,2,3]
output = []
num_var = 3
for i in range(num_var):
        for j in range(num_var):
            if i == j:
                output[i][j] = AD(arr[i], 1)
            else:
                output[i][j] = AD(arr[i], 0)