import numpy as np

# 1. `AND_gate` 함수를 구현하세요. 
def AND_gate(x1,x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    bias = -0.7
    y = np.sum(weight*x) + bias
    
    return Step_Function(y)

# 2. `OR_gate` 함수를 구현하세요.
def OR_gate(x1,x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    bias = -0.2
    y = np.sum(weight*x) + bias
    
    return Step_Function(y)

    
# 3. `NAND_gate` 함수를 구현하세요.
def NAND_gate(x1,x2):
    x = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    bias = 0.7
    y = np.sum(weight*x) + bias
    
    return Step_Function(y)

# 4. Step_Function 함수를 구현하세요.
def Step_Function(y):
    if y<=0:
        return 0
    else:
        return 1
    
# 5. 구현한 AND, OR, NAND gate 함수들을 활용하여 XOR_gate 함수를 구현하세요. 
def XOR_gate(x1, x2):
    s1 = OR_gate(x1,x2)
    s2 = NAND_gate(x1,x2)
    return AND_gate(s1,s2)    

def main():
    # NOR gate에 넣어줄 Input
    array = np.array([[0,0], [0,1], [1,0], [1,1]])
    
    # XOR gate를 만족하는지 출력하여 확인
    print('XOR Gate 출력')
    for x1, x2 in array:
        print('Input: ',x1, x2, ', Output: ', XOR_gate(x1, x2))


if __name__ == "__main__":
    main()