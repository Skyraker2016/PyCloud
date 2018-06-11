# -*- coding: utf-8 -*-
#wordcloud生成中文词云

from wordcloud import WordCloud
import jieba
import jieba.analyse
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np


# 绘制词云
def draw_wordcloud( file_name, background="white", font="简约字体.ttf", masker=None, stopword=[], masker_val=0.5,w=1000,h=1000,maxsize=100,fontstep=2):
    #读入一个txt文件(尝试三种主流编码：utf-8, gbk, utf-16(unicode))
    try:
        comment_text = open(file_name,'r',encoding="utf-8").read()
    except:
        try:
            comment_text = open(file_name,'r',encoding="gbk").read()
        except:
            comment_text = open(file_name,'r',encoding="utf-16").read()

    # 进行分词
    cut_text = " ".join(jieba.cut(comment_text))

    # 读取背景
    if (masker):
        im = Image.open(masker).convert('L')
        ww, hh = im.size
        if ww > hh:
            hh = int(hh/ww*w)
            ww = w
        else:
            ww = int(ww/hh*h)
            hh = h
        im.resize((ww,hh))
        threshold  =  int(masker_val*255)
        table  =  []
        for  i  in  range( 256 ):
            if  i  <  threshold:
                table.append(0)
            else :
                table.append( 1 )
        #  convert to binary image by the table 
        bim  =  im.point(table, '1' )
        bim = bim.convert('RGB')
        # bim.save("masker.jpg")
        color_mask = np.array(bim)
        # print(color_mask)
    else:
        color_mask = None

    # 词云设置
    cloud = WordCloud(
        #设置字体
        font_path="ttf/"+font,
        #设置背景色
        background_color=background,
        #词云形状
        mask=color_mask,
        #词云大小
        width=w,
        height=h,
        #允许最大词汇量
        max_words=1000,
        #字体大小差距
        font_step=fontstep,
        #最大号字体
        max_font_size=maxsize,
        #过滤词
        stopwords=stopword
    )
    

    word_cloud = cloud.generate(cut_text) # 产生词云
    word_cloud.to_file("result.jpg") #保存图片
    #  显示词云图片



if __name__ == '__main__':

    draw_wordcloud("Gac.txt","white","简约字体.ttf","gatsby.jpg",maxsize=200,stopword=['我们','他们','一个','什么','已经','可是','然后'])