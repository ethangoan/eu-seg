#!/usr/bin/env python3

## bisenetv2
cfg = dict(
    model_type='bisenetv2',
    model_config='bayes',
    var_step=200,
    momentum=0.9,
    n_cats=171,
    num_aux_heads=4,
    lr_start=1e-5,
    weight_decay=1e-4,
    warmup_iters=1000,
    max_iter=10000,
    dataset='CocoStuff',
    im_root='/home/ethan/exp_data/coco',
    train_im_anns='./datasets/coco/train.txt',
    val_im_anns='./datasets/coco/val.txt',
    scales=[0.75, 2.],
    cropsize=[640, 640],
    eval_crop=[640, 640],
    eval_scales=[0.5, 0.75, 1, 1.25, 1.5, 1.75],
    ims_per_gpu=2,
    eval_ims_per_gpu=1,
    use_fp16=True,
    use_sync_bn=True,
    respth='./res',
)
