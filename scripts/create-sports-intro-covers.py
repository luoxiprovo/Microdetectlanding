"""Render the introductory measurement-chain covers. Usage: python script.py /path/to/NotoSansSC.ttf"""
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
font_path = sys.argv[1]

def draw_cover(lang):
    image = Image.new('RGB', (1672, 941), '#071726')
    d = ImageDraw.Draw(image)
    def text(x,y,value,size,color='#eaf5fa'):
        d.text((x,y),value,font=ImageFont.truetype(font_path,size),fill=color)
    text(90,65,'MICRODETECT  /  SPORTS RADAR  /  01',27,'#55dfce')
    if lang == 'en':
        text(90,145,'What is millimeter-wave radar?',61)
        text(90,240,'From reflections to useful sports measurements',32,'#a7bdcb')
        labels=['SIGNALS','DETECTIONS','TRACKS','COACHING METRIC']
        sub=['Returning reflections','Select the target','Connect observations','Validate the meaning']
        footer='Measurement chain • Conceptual diagram • Not experimental data'
    else:
        text(90,145,'什么是毫米波雷达？',72)
        text(90,250,'从反射信号到有意义的体育测量',38,'#a7bdcb')
        labels=['信号','检测','轨迹','训练指标']
        sub=['接收目标反射','筛选相关目标','关联连续观测','验证指标含义']
        footer='测量链路 · 概念示意图 · 非实验数据'
    for i in range(4):
        x=90+i*395
        d.rounded_rectangle((x,405,x+305,735),radius=24,outline='#2e6576',width=2,fill='#102b3d')
        text(x+25,425,f'0{i+1}',28,'#55dfce')
        text(x+25,610,labels[i],22 if lang=='en' else 35)
        text(x+25,673,sub[i],19 if lang=='en' else 25,'#a7bdcb')
        if i==0:
            for k in range(3):
                d.arc((x+60+k*20,487-k*15,x+170+k*20,560+k*15),-60,60,fill='#55dfce',width=4)
        elif i==1:
            for dx,dy in [(65,525),(90,535),(120,513),(150,540),(175,515),(220,550)]:
                d.ellipse((x+dx-5,dy-5,x+dx+5,dy+5),fill='#55dfce')
        elif i==2:
            pts=[(x+40,560),(x+100,535),(x+155,525),(x+210,500),(x+260,490)]
            d.line(pts,fill='#55dfce',width=4)
            for a,b in pts:d.ellipse((a-5,b-5,a+5,b+5),fill='#55dfce')
        else:
            for k,h in enumerate([25,45,60,80]):
                d.rounded_rectangle((x+65+k*40,570-h,x+87+k*40,570),radius=4,fill='#55dfce')
        if i<3:
            d.line((x+322,565,x+368,565),fill='#55dfce',width=3)
            d.polygon([(x+368,565),(x+357,558),(x+357,572)],fill='#55dfce')
    text(90,831,footer,24,'#a7bdcb')
    name=('en-' if lang=='en' else '')+'what-is-mmwave-radar-in-sports.png'
    image.save(root/'public/insights'/name)

for language in ['en','zh']:draw_cover(language)
