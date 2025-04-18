def perceptron(x,weights):
    pre_y = weights[0]
    for i in range(len(x)):
        pre_y += x[i] * weights[i + 1] * x[i]
    return 1 if pre_y >= 0 else 0

x = [1,0]
weights = [-0.5, 1.0, 1.0]
print(perceptron(x,weights)) 