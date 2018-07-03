高级编程技术期末项目
# 词云生成器

## 依赖库
* wordcloud(词云)
* jieba(结巴分词)
* numpy
* pillow
* json
* Crypto
* beautiful-soup
* qdarkstyle
* pyqt5
* itchat

## 功能

1. 自定义词云：输入词云形状背景（可选），输入生成词云的文字；
2. 百度百科词云：输入关键字，自动爬取该词条的文字和图片，生成词云；
3. 网易云音乐热评：输入歌手名，自动爬去该歌手的头像及其歌曲中的热评，生成词云；
4. 辅助选项：可修改以下参数
    - 过滤词
    - 轮廓图片阈值（图片深度超过阈值部分作为词云绘制的位置）
    - 轮廓图片*[仅GUI模式可用]*
    - 步长（每种大小文字间的差别）*[仅GUI模式可用]*
    - 字体*[仅GUI模式可用]*
    - 背景色（底色为黑或白）*[仅微信模式可用]*
    - 轮廓or颜色（背景图作为词云轮廓还是文字颜色）*[仅微信模式可用]*

## 部署
- GUI模式：本地模式。此项目所有文件下载，并在项目根目录运行`GUI.py`

- 微信模式：将词云部署于个人公众号上。此项目下载后，在项目根目录运行`thechat.py`,运行后扫描二维码即可。当他人要使用时私聊发送`07624`获取词云功能（自己要用时发送给文件传输助手即可），接下来按照提示操作即可。

## 运行效果

![GUI模式](https://raw.githubusercontent.com/Skyraker2016/markdownpic/master/pycloud-demo-gui.png)

*GUI模式*

![微信模式](https://raw.githubusercontent.com/Skyraker2016/markdownpic/master/pycloud-demo-wx.jpg)
*微信模式*

## 分工
- [skyraker2016](https://github.com/Skyraker2016):词云封装，网易云热评爬虫，微信端接口

- [as953060314](https://github.com/as953060314):GUI设计

- [RealEasyin](https://github.com/RealEasyin):百度百科爬虫

- [Jhhhha](https://github.com/Jhhhha):GUI设计
