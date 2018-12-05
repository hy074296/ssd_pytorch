import os.path as osp
sk = [ 15, 30, 60, 111, 162, 213, 264 ]
feature_map = [ 38, 19, 10, 5, 3, 1 ]
steps = [ 8, 16, 32, 64, 100, 300 ]
image_size = 300
aspect_ratios = [[2], [2, 3], [2, 3], [2, 3], [2], [2]]
MEANS = (104, 117, 123)
batch_size = 2
data_load_number_worker = 1
lr = 1e-3
momentum = 0.9
weight_decacy = 5e-4
gamma = 0.1
VOC_ROOT = osp.join('./', "VOCdevkit/")
dataset_root = VOC_ROOT