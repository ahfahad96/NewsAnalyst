 
import tool as to
import bs4 #this is beautiful soup
import re
import requests
import csv

import _thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
def extract_Tribunenews(filename):
    
    # +++your code here+++
        source =requests.get(filename)
        soup = bs4.BeautifulSoup(source.text,"lxml")
        body=soup.body

        data_titles=[]
        data_content=[]
        
        data=body.find_all('div',{'class': [re.compile('^span-16 primary')]})
        l1=[]
        links = []
        title=[]
        data2=data[0].find_all('div',{'class': [re.compile('^story cat-0 group-0')]})


        for i in range(len(data2)):

            a=( data2[i].find('a'))

            links.append(a['href'])
        #print (links)   
        print ('starting')
        for story in links:
            try:

                source =requests.get(story)
                soup = bs4.BeautifulSoup(source.text,"lxml")
                body=soup.body
                t=( body.find('h1'))
                content=body.find_all('div',{'class': [re.compile('^clearfix story-content read-full')]})
                full=content[0].find_all('p')
                print(t.text)
                l1.append('   TITLE   ')
                l1.append(t.text)
                data_titles.append(t.text)
                l1.append('\n')
                stro=""
                for i in range(len(full)):
                    if (i!=0):
                        l1.append(full[i].text)
                        stro=stro+full[i].text

                l1.append('\n')
                l1.append('-')
                l1.append('\n')
                data_content.append(stro)
            except Exception as e:
                print ("eroor")
        #to.write('tribune',l1)
        to.writecsv('tribune',data_titles,data_content)
        
def run():
    count=0
    while(count<10):
        try:
            to.write_log('log','scapping tribune')
            extract_Tribunenews('https://www.tribune.com.pk/latest/')
            to.write_log('log','scraped successfully tribune')
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

