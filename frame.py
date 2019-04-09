import os
import glob
import cv2
from multiprocessing import Pool
def get_frame(files):
    for file in files:
        filedir=file.rsplit('.mp4',1)[0]
        filedir='pic/'+filedir
        if not os.path.exists(filedir):
            os.mkdir(filedir)
            print(file)
        cap=cv2.VideoCapture(file)
        fid=0
        success=1
        while(success):
            success,frame=cap.read()
            picname=filedir+'/'+str(fid)+'.jpg'
            cv2.imwrite(picname,frame)
            fid+=1
        cap.release()
if __name__=="__main__":
    train_files=glob.glob('./train/*/*.mp4')
    val_files=glob.glob('./val/*/*.mp4')
    l1=len(train_files)
    l2=len(val_files)
    pool=Pool(6)
    f=[train_files[0:l1/6],train_files[l1/6,l1/3],train_files[l1/3,l1/2],train_files[l1/2,l1*2/3],train_files[l1*2/3,l1],val_files]
    pool.map(get_frame,f)
    pool.close()
    pool.join()
