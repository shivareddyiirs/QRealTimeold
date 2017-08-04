from threading import Timer
import time
import signal
i=0
def say(word):
        global i
        i+=1
        if i <5:
                printsay(word,i,)
                t.run()
        else :
                t.cancel()
def printsay(word,i):
        time.sleep(10)
        print word,i
t= Timer(1,say,['hello'])
t.start()
while t.isAlive():
        print('waiting for thread to close')
        t.join(1)

print 'testing',t.isAlive()
print 'khatam'
