import numpy as np

file_path = '/home/ssw/code/dataset/h36m/annots.npz'
a = np.load(file_path, allow_pickle=True)['annots']

print('ok')