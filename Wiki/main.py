from requests import get
from lxml import etree
from sys import exit
import GUI

class Command:
    def __init__(self,comm):
        self.comm = comm
    def Run(self,topic = "主页"):
        if(self.comm == "exit"):
            exit()
        if(self.comm == GUI.Init().enter.get()):
            global link,text
            self.topic = topic
            print("======waiting======")
            read = Get(self.topic)
            link,text = read.uploading()
            print("======finished======")
        if(self.comm == "show"):
            try:
                Show(link,text).Show_on_GUI()
                return link,text
            except NameError:
                print("no get")
        if(self.comm == "save"):
            save = Save(self.link,self.text)

class Get:
    def __init__(self,topic,language = "zh"):
        self.topic = topic
        self.url = f"https://zh.wikipedia.org/zh-cn/" + self.topic
        self.html = None
        self.content = None
        self.link = None
        self.text = ""
    def uploading(self):
        self.html = get(self.url).text
        etree_html = etree.HTML(self.html)
        self.content = etree_html.xpath("//*[@class=\"mw-body-content\"]/div//text()")
        self.link = etree_html.xpath("//*[@class=\"mw-body-content\"]/div/*//a//text()")
        for str in self.content:
            if not (str[0] == "[" and str[-1] == "]"):
                self.text += str
        self.text.replace("\n\n","\n")
        return self.link, self.text

class Show:
    def __init__(self,link,text):
        self.link = link
        self.text = text
    def Show_on_terminal(self):
        print(self.link)
        print(self.text)
    def Show_on_GUI(self):
        GUI.Fun().Search(self.link,self.text)
        # return self.link,self.text

class Save:
    def __init__(self,link,text):
        self.link = link
        self.text = text
        
if __name__ == "__main__":
    while(True):
        # Command(input()).Run()
        GUI.Init().LOOP()
