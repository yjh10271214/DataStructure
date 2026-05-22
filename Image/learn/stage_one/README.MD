1.yuv格式,可以按比例来储存，按需选择格式，将人眼最敏感的y分量无损保留下来，uv就是按需来，batyer pattern的格式也是有两个g也是因为人眼最敏感

2.opencv里面用的是bgr格式记得转换[start:end:step] [::-1]倒序读取

3.sensor上接收到的数据是一个像素只有一个颜色通过滤光片，RGGB，BGGR，GRBG， GBRG，得到的元数据是带mosiac的，所以需要demosiac,
raw8,raw10,raw12:元数据的存储大小，8就是一个像素8bit也就是一字节，10就是10bit但是是两个字节6bit不使用，12类似

带宽:resolution