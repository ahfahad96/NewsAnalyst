#!/usr/bin/env python
import _thread
import time
import datetime
def run():
    f = open('conf.txt','r')
    message = f.read()
    
    f.close()
    message=message.split('\n')
    print(message)
    i=0
    lists=[]
    while i < len(message)-1:
        try:
            t=__import__(message[i])
            #_thread.start_new_thread(t.run())

            lists.append(t.run())
            
        except Exception as e:
            print(str(e))
        i+=1
    
def waittill():
    """Wait to tommorow 00:00 am"""

    tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1), 
                         hour=23, minute=50, second=0)
    delta = tomorrow - datetime.datetime.now()
    time.sleep(delta.seconds)
    


def main():
    while (True):
        run()
        print('waiting for tomorrow')
        waittill()
        
main()

  
  
