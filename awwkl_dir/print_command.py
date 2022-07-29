import os

# === Adjust these variables ===
config_name = 'faster_rcnn_r101_fpn_1x_bird_10shot'
iter_num = 130
# ==============================

dataset = 'manhole' if 'manhole' in config_name else 'bird'
config_file = os.path.join('awwkl_dir/configs/', dataset, config_name + '.py')
work_dir = os.path.join('work_dirs/', config_name)
weights_file = os.path.join(work_dir, f'epoch_{iter_num}.pth')
show_dir = os.path.join(work_dir, f'epoch_{iter_num}')

train_cmd = []
train_cmd.append('python tools/train.py')
train_cmd.append(config_file)
print('---')
print(' '.join(train_cmd))
print('---')

test_cmd = []
test_cmd.append('python')
test_cmd.append('tools/test.py')
test_cmd.append(config_file)
test_cmd.append(weights_file)
test_cmd.append('--eval bbox')
test_cmd.append('--show --show-dir')
test_cmd.append(show_dir)
test_cmd.append('--work-dir')
test_cmd.append(show_dir)
print(' '.join(test_cmd))
