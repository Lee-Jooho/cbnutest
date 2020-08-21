import numpy as np

class new_word_in_voc:
    
    def __init__(self,w1,w2,num_add):
        self.params = {}
        self.params['W1'] = w1
        self.params['W2'] = w2
        self.num = num_add # 단어장에 추가된 단어의 수
        
    def make_new_params(self):
        sizeof_axis1 = np.size(self.params['W1'],axis = 1) # w1이 n*m이라고 할때  m 값
        # w1이 n*m 사이즈 일 경우 m 값만 알면됨 >> w1의 맨 아래에 1*m 추가 
        # w2의 맨 오른쪽에 m*1 추가
        
        adding_new_param0 = np.random.rand(1, sizeof_axis1)
        adding_new_param1 = np.random.rand(sizeof_axis1, 1)
        
        for i in range(self.num):
            self.params['W1'] = np.append(self.params['W1'],adding_new_param0,axis=0)
            self.params['W2'] = np.append(self.params['W2'],adding_new_param1,axis=1)
        