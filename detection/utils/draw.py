import numpy as np
import cv2
import colorsys
import random
from PIL import Image,ImageDraw,ImageFont
SHIPCLASSES=[
    '__background__',
                'passenger ship',#1
                    'ore carrier',#2
                    'general cargo ship',#3
                    'fishing boat',#4
                    'Sail boat',#5
                    'Kayak',#6
                    'flying bird',#flying bird/plane #7
                    'vessel',#vessel/ship #8
                    'Buoy',#9
                    'Ferry',#10
                    'container ship',#11
                    'Other',#12
                    'Boat',#13
                    'Speed boat',#14
                    'bulk cargo carrier',#15

]
SHIPCLASSES_CHINESE=[
    '背景',
    '客船',#1
    '运砂船',#2
    '杂货船',#3
    '渔船',#4
    '帆船',#5
    '皮艇',#6
    '飞行物',#flying bird/plane #7
    '大型轮船',#vessel/ship #8
    '浮标',#9
    '渡船',#10
    '集装箱船',#11
    '其他',#12
    '小船',#13
    '快艇',#14
    '散货船',#15

]
def ncolors(num_color):
    hsv_tuples = [(x / num_color, 1., 1.)
                  for x in range(num_color)]
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(
        map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
            colors))
    colors = [c[::-1] for c in colors]
    return colors



class mydraw(object):
    def __init__(self,CLASSES=SHIPCLASSES_CHINESE):
        # self.fontScale = 20.  # 2
        self.thiness = 2  # 2
        self.textSize=42
        self.fontStyle = ImageFont.truetype(font='C:/Windows/Fonts/simhei.ttf', size=self.textSize,encoding='utf-8')
        self.classes=CLASSES
        self.colors=ncolors(len(CLASSES))
    def draw(self,im ,dets):
        imt=self.write_detection_batch(im, dets, CLASSES=self.classes, colors=self.colors)
        return imt

    def write(self,name,im):
        return cv2.imwrite(name,im)

    def drawPIL(self,im, dets):
        '''
                add the bbox and text and background box
                '''
        colors=self.colors
        CLASS_NAMES=self.classes
        if len(np.array(colors).shape) < 2:
            colors = ncolors(len(CLASS_NAMES))
        font = self.fontStyle#ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 42)
        for i in range(len(dets)):
            rectangle_tmp = im.copy()
            #bbox = dets[i, :4].astype(np.int32)
            bbox = dets[i].box.astype(np.int32)
            class_ind = int(dets[i].class_id)
            # if class_ind == 7:
            #     continue
            # score = dets[i, -1]

            color = colors[class_ind]
            string = CLASS_NAMES[class_ind]
            _, _, text_width, text_height = font.getbbox(string)
            # text_size, baseline = cv2.getTextSize(string, fontFace, fontScale, thiness)
            text_origin = (bbox[0] - 1, bbox[1] - text_height)  # - text_size[1]
            ###########################################putText
            cv2.rectangle(rectangle_tmp, (text_origin[0] - 1, text_origin[1] - 1),
                          (text_origin[0] + text_width + 1, text_origin[1] + text_height + 1),
                          color, cv2.FILLED)
            cv2.addWeighted(im, 0.7, rectangle_tmp, 0.3, 0, im)
            im = cv2.rectangle(im, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
            img = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(img)
            draw.text(text_origin, string, font=font, fill=(0, 0, 0))
            im = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        return im


    def write_detection_batch(self, im, dets, CLASSES=SHIPCLASSES, colors=(0, 0, 255)):
        '''
        add the bbox and text and background box
        '''
        # inds = np.where(dets[:, -1] >= thresh)[0]
        # if len(inds) == 0:
        #     return im
        # colors=color
        if len(np.array(colors).shape) < 2:
            colors = ncolors(len(CLASSES))
        for i in range(len(dets)):
            bbox = dets[i].box.astype(np.int32)
            # score = dets[i, -1]
            rectangle_tmp = im.copy()
            # str1=CLASSES[class_inds[i]]
            # string = '%s' % (CLASSES[class_inds[i]].lower())
            string = '%s' % (CLASSES[dets[i].class_id]) if CLASSES else '%d' % (dets[i].class_id)
            fontFace = cv2.FONT_HERSHEY_COMPLEX  # cv2.FONT_HERSHEY_COMPLEX
            fontScale = 2.  # 2
            thiness = 2  # 2

            text_size, baseline = cv2.getTextSize(string, fontFace, fontScale, thiness)
            text_origin = (int(bbox[0] - 1), bbox[1])  # - text_size[1]
            # cv2.copyTo(im,dst=rectangle_tmp)

            cv2.rectangle(rectangle_tmp, (text_origin[0] - 1, text_origin[1] + 1),
                          (text_origin[0] + text_size[0], text_origin[1] - text_size[1] - 1),
                          colors[dets[i].class_id],
                          cv2.FILLED)

            cv2.addWeighted(im, 0.6, rectangle_tmp, 0.4, 0, im)  # 阴影部分
            im = cv2.rectangle(im, (bbox[0], bbox[1]), (bbox[2], bbox[3]), colors[dets[i].class_id], 3)  # 10
            cv2.putText(im, string, text_origin,
                        fontFace, fontScale, (0, 0, 0), thiness, lineType=-1, )
        return im