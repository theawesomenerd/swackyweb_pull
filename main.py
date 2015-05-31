from browser import document,window,timer,alert,html
texts = ["LOL", "Swacky"]
repeat = 0
def flashText():
    global repeat
    document['title'].set_text(texts[repeat])
    repeat += 1
    if repeat >= len(texts):
        repeat = 0
        
print('got here',dir(document['title']) ) #,document['title'].value)
timer.set_interval(flashText,1000)
#document['title'].set_text("hello Everyboody this written in python, I hope it will work, LOL")