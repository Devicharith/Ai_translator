from webvtt import WebVTT, Caption
import webvtt
from googletrans import Translator
translator = Translator()

def read_vtt(vtt,dic):
    for caption in vtt:
        dic[caption.start+' --> '+caption.end] = caption.text
    print(dic)

def trans(lan):
    dic = dict()
    vtt = webvtt.read(r'subs.vtt')
    read_vtt(vtt,dic)
    vtt1 = WebVTT()
    print("Translating text")
    for j,i in enumerate(dic.keys()):
        translation = translator.translate(dic[i],dest = lan)
        trans = translation.text
        theWord = trans.encode('utf-8').decode('utf-8')
        # creating another caption with a text
        caption = Caption(vtt[j].start, vtt[j].end, theWord)
        vtt1.captions.append(caption)
    vtt1.save('trans_sub')
