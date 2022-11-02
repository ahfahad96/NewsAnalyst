import tool as to
import bs4 #this is beautiful soup
import re
import requests
import csv
import time
import _thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 

def extract_Dawnnews(filename):
    # +++your code here+++
    source =requests.get(filename)
    data_titles=[]
    data_content=[]


    soup = bs4.BeautifulSoup(source.text,"lxml")
    body=soup.body

    data=body.find_all('div',{'class': [re.compile('col-sm-11 col-12')]})

    #0re.compile('^company')
    #s=table.findAll('td')

    l1=[]
    links = []
    title=[]
    data2=data[0].find_all('div',{'class': [re.compile('tabs__pane active')]})
    data3=data2[0].find_all('h2')

    for i in range(len(data3)):

        a=( data3[i].find('a'))
        links.append(a['href'])


    for story in links:
        print("waqas")
        source=requests.get(story)
        print("check0")
        #print (source.status_code)
        if (source.status_code==403):
            while(source.status_code==403):
                time.sleep(1)
                print("403")
                source =requests.get(story)


        soup = bs4.BeautifulSoup(source.text,"lxml")
        body=soup.body
        try:
            print("check1")
            tt=( body.find_all('h2'))
            print (tt[1].text)
            t=tt[1]
            
            
            content=body.find_all('div',{'class': [re.compile('^story__content')]})
        #Fahad's

        #till here
            full=content[0].find_all('p')
            
            l1.append('   TITLE   ')
            l1.append(t.text)
            data_titles.append(t.text)
            l1.append('\n')
            stro=""
            #data_content.append(full.text)
            for i in range(len(full)):
                l1.append(full[i].text)
                stro=stro+full[i].text




            l1.append('\n')
            l1.append('-')
            l1.append('\n')
            data_content.append(stro)
            print('data written')
        except Exception as e:
            print('caught exception due to different sturcture')
        #print (stro)
        #l1.append(content[0].text)
    to.writecsv('Dawn_news',data_titles,data_content)
    #to.write('Dawn_news',l1)
    
    
    
    
def run():
    count=0
    while(count<20):
    	
        try:
            print(count,'count')
            to.write_log('log','scapping dawn')
            extract_Dawnnews('https://www.dawn.com/latest-news')
            #c=c+1
            to.write_log('log','scraped successfully Dawn')
            break
        except requests.ConnectionError as e:
            to.write_log('',"OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
        except requests.Timeout as e:
            to.write_log('',"OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            to.write_log('',"OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            to.write_log('',"Someone closed the program")
        count=count+1
