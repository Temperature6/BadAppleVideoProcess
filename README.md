# Bad Apple视频处理程序

### 功能

​	用于处理《Bad Apple》视频到二进制格式以便各种屏幕播放《Bad Apple》视频

### 使用

​	Step1.打开“VideoProcess.py",

![1616910888425](C:\Users\15231\AppData\Roaming\Typora\typora-user-images\1616910888425.png)

​	将file后面的内容改为要分割的视频的文件路径

​	在函数的第二个传参中改想要的图片的大小



​	Step2.打开“ProcessVideo.py”，

​	![1616911051639](C:\Users\15231\AppData\Roaming\Typora\typora-user-images\1616911051639.png)

函数的第一个参数时VideoProcess.py处理完的图片的文件夹路径

第二个参数是文件路径列表，我们提供了list_file()函数用于列出文件

第三个参数是想要保存的文本文档路径（名称）