#coding=utf-8
import os
import shutil
#https://blog.csdn.net/qikaihuting/article/details/72667740

#folder_capacity = 10000

def copy_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    count = 0
    for item in os.listdir(src_dir):
        abs_item = os.path.join(src_dir, item)
        dst_name = os.path.join(dest_dir, item)
        if os.path.exists(abs_item):
            count +=1
            shutil.copy(abs_item,dst_name)
            
        if count >= 20000:
            break
    print("done")
    return 0
        
def move_file(src_dir,target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
#    count = 0
    for item in os.listdir(src_dir):
        #print(item.split('.')[0])
        int_value = int(item.split('.')[0])
        if int_value%30 == 0:
            #print(int_value)
            src_name = os.path.join(src_dir,item)
   
            target_name = os.path.join(target_dir,item)
#        count +=1
            shutil.move(src_name,target_name)
 
        
#        if count>=20000:
#            break
 
if __name__ =='__main__':
    move_file('E:/semantic_segmentation/models-master/research/deeplab/datasets/yaogan_ADE20K/ADE20K/ADEChallengeData2016/images/training','E:/semantic_segmentation/models-master/research/deeplab/datasets/yaogan_ADE20K/ADE20K/ADEChallengeData2016/images/validation')
