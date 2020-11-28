# 谁会带钥匙出门？ 
[Gayhub地址][1]

材料清单
----


rasberrypi 伊拉克战损无保护壳版 *1
PS3®Eye 快递摔坏版 *1
夏科内存卡 32G白嫖版 *1
(还没到货) 一路继变器 *1
电机？ *1

----------

##前期准备
###安装照相软件
```
sudo apt-get install fswebcam
sudo apt-get install mplayer
```
###下载[百度人脸识别SDK][2]
解压
    cd
    python setup.py install
##开始
####初始化
```
from aip import AipFace
""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
```
----------


  [1]: https://github.com/ridesun/openthefxxkdoor
  [2]: http://ai.baidu.com/ai-doc/FACE/ek37c1qiz
