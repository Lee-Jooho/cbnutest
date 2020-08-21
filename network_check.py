from training_trytry import *
from training_param_add import * # import numpy as np가 되어있음.
from WordInput import *


class network():
    
    def __init__(self):
        self.check = None
    
    def net_update(self,wi):
        voc_length = wi.inform['voc_length']
        voc_length_diff = wi.inform['voc_length_diff']
        if self.check is None:
            self.network = TwoLayerNet(input_size = voc_length,hidden_size = 2, output_size = voc_length)
            self.check = 1
        else:
            print("checking new words ~~ing~~ ")
            print("추가된 단어 수 " , voc_length_diff) #단어가 몇개가 추가되엇는지 내가 확인하기 위함.
            if voc_length_diff == 0:
                print("network is ready to use")
            else:
                print("adding words in vocabulary ~~ing~~ ")
                add_param = new_word_in_voc(self.network.params['W1'], self.network.params['W2'],voc_length_diff)
                add_param.make_new_params()
                for key in('W1','W2'):
                    self.network.params[key] = add_param.params[key]
            
                print("ready to use")
            
            