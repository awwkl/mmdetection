# The new config inherits a base config to highlight the necessary modification
_base_ = '../../configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('Manhole',)
data_root = 'awwkl_dir/data/manhole_5-shot/'
data = dict(
    samples_per_gpu=1,
    train=dict(
        img_prefix=data_root+'train/',
        classes=classes,
        ann_file=data_root+'train/annotation.json'),
    val=dict(
        img_prefix=data_root+'validate/',
        classes=classes,
        ann_file=data_root+'validate/annotation.json'),
    test=dict(
        img_prefix=data_root+'test/',
        classes=classes,
        ann_file=data_root+'test/annotation.json'))

# Use pre-trained model for better performance
load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

# Modify max number of epochs
runner = dict(
    max_epochs=900)
evaluation = dict(interval=10)
checkpoint_config = dict(interval=10)