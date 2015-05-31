from browser import document,window,timer,alert,html
texts = ["LOL", "Swacky"]
class FlashText:
    def __init__(self,time):
        self.repeat = 0
        self.time = time
        self.interval = timer.set_interval(self.flash,1000)
        
    def flash(self):
        document['title'].set_text(texts[self.repeat])
        self.repeat += 1
        if self.repeat >= len(texts):
            self.repeat = 0
        
flashText = FlashText(1000)        
#print('got here',dir(document['title']) ) #,document['title'].value)

#document['title'].set_text("hello Everyboody this written in python, I hope it will work, LOL")