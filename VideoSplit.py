import cv2, sys, time


def start_split(filename):
    start = time.time()
    video = cv2.VideoCapture(filename)
    if not video:
        print("无法读取视频文件")
        sys.exit(1)

    count = 0
    while video.isOpened():
        print("\r正在处理第{0}帧图像".format(count), end="")
        ret, frame = video.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(gray, (8, 8))
        cv2.imwrite("./pic/" + str(count).zfill(5) + ".jpg", resize)
        count += 1

    video.release()

    end = time.time()
    print("\n处理完成,处理了{0}帧图像,用时{1}秒".format(count, end - start))
    return


if __name__ == "__main__":
    file = "ba10s.mp4"
    start_split(file)
