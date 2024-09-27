dataset_info = dict(
    dataset_name='coco',
    paper_info=dict(
        author='Lin, Tsung-Yi and Maire, Michael and '
        'Belongie, Serge and Hays, James and '
        'Perona, Pietro and Ramanan, Deva and '
        r'Doll{\'a}r, Piotr and Zitnick, C Lawrence',
        title='Microsoft coco: Common objects in context',
        container='European conference on computer vision',
        year='2014',
        homepage='http://cocodataset.org/',
    ),
    keypoint_info={
        0:
        dict(
            name='left_fluke_tip',
            id=0,
            color=[0, 0, 255],
            type='upper',
            swap='right_fluke_tip'),
        1:
        dict(
            name='left_notch',
            id=1,
            color=[51, 153, 255],
            type='upper',
            swap='right_notch'),
        2:
        dict(
            name='center_notch',
            id=2,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        3:
        dict(
            name='right_notch',
            id=3,
            color=[51, 153, 255],
            type='upper',
            swap='left_notch'),
        4:
        dict(
            name='right_fluke_tip',
            id=4,
            color=[51, 153, 255],
            type='upper',
            swap='left_fluke_tip'),
        5:
        dict(
            name='right_fluke_leading',
            id=5,
            color=[0, 255, 0],
            type='upper',
            swap='left_fluke_leading'),
        6:
        dict(
            name='right_peduncle_or_water',
            id=6,
            color=[255, 128, 0],
            type='lower',
            swap='left_peduncle_or_water'),
        7:
        dict(
            name='center_peduncle_or_water',
            id=7,
            color=[0, 255, 0],
            type='lower',
            swap=''),
        8:
        dict(
            name='left_peduncle_or_water',
            id=8,
            color=[255, 128, 0],
            type='lower',
            swap='right_peduncle_or_water'),
        9:
        dict(
            name='left_fluke_leading',
            id=9,
            color=[0, 255, 0],
            type='upper',
            swap='right_fluke_leading')
    },
    skeleton_info={
        0:
        dict(link=('left_fluke_tip', 'left_notch'), id=0, color=[0, 255, 0]),
        1:
        dict(link=('left_notch', 'center_notch'), id=1, color=[0, 255, 0]),
        2:
        dict(link=('center_notch', 'right_notch'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('right_notch', 'right_fluke_tip'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('right_fluke_tip', 'right_fluke_leading'), id=4, color=[51, 153, 255]),
        5:
        dict(link=('right_fluke_leading', 'right_peduncle_or_water'), id=5, color=[51, 153, 255]),
        6:
        dict(link=('right_peduncle_or_water', 'center_peduncle_or_water'), id=6, color=[51, 153, 255]),
        7:
        dict(link=('center_peduncle_or_water', 'left_peduncle_or_water'), id=7, color=[51, 153, 255]),
        8:
        dict(link=('left_peduncle_or_water', 'left_fluke_leading'), id=8, color=[0, 255, 0]),
        9:
        dict(link=('left_fluke_leading', 'left_fluke_tip'), id=8, color=[0, 255, 0])
    },
    joint_weights=[
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1.
    ],
    sigmas=[
        0.025, 0.045, 0.045, 0.045, 0.025, 0.060, 0.085, 0.090, 0.085, 0.060
    ])
