'''
1. 가중치와 Bias 값을 
   임의로 설정해줍니다.

   Step01. 0이상 1미만의 임의의 값으로 정의된 
           4개의 가중치 값이 들어가있는 
           1차원 리스트를 정의해줍니다.
           
   Step02. Bias 값을 임의의 값으로 설정해줍니다.
'''
import numpy as np
def main():
    
    x = [1,2,3,4]
    
    w = np.random.rand(4) 
    b = np.random.uniform(-1,1) 
    
    output, y = perceptron(w,x,b)
    
    print('output: ', output)
    print('y: ', y)

'''
2. 신호의 총합과 그에 따른 결과 0 또는 1을
   반환하는 함수 perceptron을 완성합니다.
   
   Step01. 입력 받은 값과 Bias 값을 이용하여
           신호의 총합을 구합니다.
           
   Step02. 신호의 총합이 0 이상이면 1을, 
           그렇지 않으면 0을 반환하는 활성화 
           함수를 작성합니다.
'''

def perceptron(w, x, b):
    
    output = sum(w_i*x_i for w_i, x_i in zip(w, x)) + b 
    
    y = 1 if output >= 0 else 0
    
    return output, y

if __name__ == "__main__":
    main()