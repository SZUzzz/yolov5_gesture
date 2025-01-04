import cv2

# 视频文件路径
video_path = '/home/zz/yolov5/runs/detect/exp/2024_11_10_16:00:07.mp4'

# 创建视频捕获对象
cap = cv2.VideoCapture(video_path)

# 检查视频是否打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()

while True:
    # 逐帧读取视频
    ret, frame = cap.read()

    # 如果成功读取帧，显示图像
    if ret:
        cv2.imshow('Video', frame)

        # 按 'q' 键退出播放
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放视频捕获对象并关闭窗口
cap.release()
cv2.destroyAllWindows()
