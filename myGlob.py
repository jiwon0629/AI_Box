from glob import glob
train_img_list = glob('C:/Users/user/Desktop/box/yolov5/dataset/train/images/*.jpg')
test_img_list = glob('C:/Users/user/Desktop/box/yolov5/dataset/valid/images/*.jpg')
valid_img_list = glob('C:/Users/user/Desktop/box/yolov5/dataset/valid/images/*.jpg')
print(len(train_img_list), len(test_img_list), len(valid_img_list))

import yaml
with open('C:/Users/user/Desktop/box/yolov5/dataset/train.txt','w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('C:/Users/user/Desktop/box/yolov5/dataset/test.txt','w') as f:
    f.write('\n'.join(test_img_list) + '\n')
with open('C:/Users/user/Desktop/box/yolov5/dataset/val.txt','w') as f:
    f.write('\n'.join(valid_img_list) + '\n')