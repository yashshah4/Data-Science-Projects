'''
Auth:jayatilake.s
'''

import torch 

# check if CUDA is available
train_on_gpu = torch.cuda.is_available()

if not train_on_gpu:
    print('*** GPU NOT available...')
else:
    print('GPU Available...')