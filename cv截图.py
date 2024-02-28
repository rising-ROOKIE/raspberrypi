import cv2
camera = cv2.VideoCapture(0) #打开摄像头(只有一个摄像头则编号为0，若有2个则依次为0,1)
cv2.namedWindow('Video Cam', cv2.WINDOW_NORMAL) #创建窗口"Video Cam"
i=0
while cv2.waitKey(1)!=27: #esc键 持续间隔1ms等待按键,若有按键跳出循环
      success, frame =camera.read() #读取摄像头数据
      cv2.imshow('Video Cam', frame) # 显示在窗口"Video Cam"上
      if cv2.waitKey(1)==32: #空格键存图像
         i=i+1
         cv2.imwrite(str(i)+".jpg",frame) #存图像
camera.release() #断开摄像头
cv2.destroyAllWindows() #释放所有窗口