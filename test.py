# -*- coding: utf-8 -*-
from aip import AipFace
import urllib.request
#import RPi.GPIO as GPIO
import base64
import time
#import cv2
import os
import sys
import re
 
#百度人脸识别API账号信息
APP_ID = '23022384'
API_KEY = 'NgGQiBEtP4em22McjuPNx7Dt'
SECRET_KEY = 'L6GToAWAezhoUAEjWslbOcAEkM2qiCFF '
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
#图像编码方式
IMAGE_TYPE='BASE64'
#用户组信息
GROUP = '1'
'''
GPIO.setwarnings(False)
 
GPIO_IN_PIN22  = 22    # 按键控制
GPIO_OUT_PIN17 = 17    # 识别不通过 亮红灯
GPIO_OUT_PIN4  = 4     # 识别通过   打开继电器
GPIO_OUT_PIN24 = 24    # 识别通过   亮绿灯
GPIO_OUT_PIN18 = 18    # 工作指示灯灯
 
ledStatus = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_IN_PIN22,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_OUT_PIN17,GPIO.OUT)
GPIO.setup(GPIO_OUT_PIN4,GPIO.OUT)
GPIO.setup(GPIO_OUT_PIN18,GPIO.OUT)
GPIO.setup(GPIO_OUT_PIN24,GPIO.OUT)
'''
 
#定义一个摄像头对象
def getimage():
    getimage=os.system('''fswebcam  faceimage.jpg''')

 
#对图片的格式进行转换
def transimage():
    f = open('faceimage.jpg','rb')
    img = base64.b64encode(f.read())
    return img
 
    
 
#发送信息到微信上  
def sendmsg(name,main):
    url = "https://sc.ftqq.com/SCU128711T3b727d68a944569a04935bd0ab6fa9c25fb964d38774b.send?"
    urllib.request.urlopen(url + "text="+name+"&desp="+main)
#上传到百度api进行人脸检测
def go_api(image):
    result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP)
    if result['error_msg'] == 'SUCCESS':
        name = result['result']['user_list'][0]['user_id']
        score = result['result']['user_list'][0]['score']
        if score > 95:
            print("Welcome %s !" % name)
            sendmsg(name,'in!')
        else:
            print("Sorry...I don't know you !")
            name = 'Unknow'
            sendmsg("BadGay",name)
            return 0
        curren_time = time.asctime(time.localtime(time.time()))
        f = open('Log.txt','a')
        f.write("Person: " + name + "     " + "Time:" + str(curren_time)+'\n')
        f.close()
        return 1
    if result['error_msg'] == 'pic not has face':
        print('There is no face in image!')
        #time.sleep(4)
        return 0
    else:
        print(result['error_code']+' ' + result['error_code'])
        return 0
    
# 识别处理函数
#def manage():
getimage()
img = transimage()
res = go_api(img)
'''
    if(res == 1):
        GPIO.output(GPIO_OUT_PIN24,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_OUT_PIN24,GPIO.LOW)
        
        GPIO.output(GPIO_OUT_PIN4,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(GPIO_OUT_PIN4,GPIO.LOW)
                        
    else:
        GPIO.output(GPIO_OUT_PIN17,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_OUT_PIN17,GPIO.LOW)
        print('waite 3 seconds to do next')
'''
'''     
# 按键中断函数
def my_callback(channel):
    global ledStatus
    ledStatus = not ledStatus
    if ledStatus:
        #while True:
        manage()
            #if ledStatus == 0:
                #break          
    else:
        pass
    pass
 
 
# 给22引脚添加一个事件函数，触发条件是：捕获到GPIO.FALLING（下降沿）
GPIO.add_event_detect(GPIO_IN_PIN22,GPIO.FALLING, callback = my_callback,
                      bouncetime = 150)
 
if __name__ == '__main__':
    while True:
        try:
            GPIO.output(GPIO_OUT_PIN18,GPIO.HIGH)
            print("I'm working...")
            time.sleep(5)
            pass
        except: 
            GPIO.output(GPIO_OUT_PIN18,GPIO.LOW)
            GPIO.output(GPIO_OUT_PIN4,GPIO.LOW)
            break
            pass
        pass
'''
