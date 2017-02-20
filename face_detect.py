#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: hello.py

# In this tutorial, you will learn how to call Face ++ APIs and implement a
# simple App which could recognize a face image in 3 candidates.
# 在本教程中，您将了解到Face ++ API的基本调用方法，并实现一个简单的App，用以在3
# 张备选人脸图片中识别一个新的人脸图片。

# You need to register your App first, and enter you API key/secret.
# 您需要先注册一个App，并将得到的API key和API secret写在这里。
import json
API_KEY = '36e7381e85ae17ef531c776793643d09'
API_SECRET = 'QMzerR3sVLo407rJ45rYgCmUI9QEKjbX'
# Import system libraries and define helper functions
# 导入系统库并定义辅助函数
import time
from pprint import pformat
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

# First import the API class from the SDK
# 首先，导入SDK中的API类
from facepp import API

api = API(API_KEY, API_SECRET)

# Here are the person names and their face images
# 人名及其脸部图片
f= open('test_face_detect_out.json', 'w') 
face=[]
IMAGE_DIR ='https://pbs.twimg.com/profile_images/693820032048955392/s5e3iedX.jpg'

#IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'
# PERSONS = [
#     ('Jim Parsons', IMAGE_DIR + '1.jpg'),
#     ('Leonardo DiCaprio', IMAGE_DIR + '2.jpg'),
#     ('Andy Liu', IMAGE_DIR + '3.jpg')
# ]
# TARGET_IMAGE = IMAGE_DIR + '4.jpg'

# Step 1: Detect faces in the 3 pictures and find out their positions and
# attributes
# 步骤1：检测出三张输入图片中的Face，找出图片中Face的位置及属性
FACES = api.detection.detect(url = IMAGE_DIR)

# FACES = {name: api.detection.detect(url = url)
#         for name, url in PERSONS}

# for name, face in FACES.iteritems():
#     print_result(name, face)
print(FACES)
face.append(FACES)
json.dump(face,f,indent=4)

