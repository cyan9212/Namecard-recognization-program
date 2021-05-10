from PIL import Image
from pytesseract import *
import configparser
from . import Image_Processing
from . import Data_Analysis
from . import SQL_Database
import os

config = configparser.ConfigParser()

config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')

def ocrToStr(fullPath, outTxtPath, fileName, lang='eng'):
    img = Image.open(fullPath)
    txtName = os.path.join(outTxtPath, fileName.split('.')[0])

    outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_spaces=1')

    print('+++ OCT Extract Result +++')
    print('Extract FileName ->>> : ', fileName, ' : <<<-')
    print('\n\n')

    print(outText)
    strToTxt(txtName, outText)

    info = Data_Analysis.extractInfo(outText)
    print(info)
    return info

def strToTxt(txtName, outText):
    with open(txtName + '.txt', 'w', encoding='utf-8') as f:
        f.write(outText)

def run():

    # text file 저장 경로
    outTxtPath = os.path.dirname(os.path.realpath(__file__)) + config['Path']['OcrTxtPath']
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__)) + config['Path']['OriImgPath']):
        for fname in files:
            fullName = os.path.join(root, fname)
            print(fullName)
            Image_Processing.auto_scan_image(fullName,fname)
            path = fullName.split('\orc_ori_image')
            info = ocrToStr(path[0]+'translated_image\\'+fname,outTxtPath,fname,'kor+eng')
            print(fname,info)
            SQL_Database.insert(fname,info)
            SQL_Database.select()

