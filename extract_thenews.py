import tool as to
import bs4 #this is beautiful soup
import re
import requests
import csv
import time
import _thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def extract_Thenews(filename):
    # +++your code here+++
    browser = webdriver.Firefox(executable_path="./geckodriver")
    count=0
    st=''
    data_titles=[]
    data_content=[]
    while(count<7):
        try:
            print (count)
            browser.get(filename)
            #print ('waqas')
            break
        except Exception as e:
            print('caught')
            to.write_log('',str(e))
        count=count+1

 
    time.sleep(1)
    if (count<7):
        print ('inif')
        elem = browser.find_element_by_tag_name("body")
        no_of_pagedowns = 3

        while no_of_pagedowns:
            content=elem.find_element_by_class_name('view-all').click()
            time.sleep(1)
            no_of_pagedowns-=1
        time.sleep(1)
        html =browser.page_source.encode('utf-8')
        soup = bs4.BeautifulSoup(html,"lxml")
        body=soup.body


        data=body.find_all('div',{'class': [re.compile('^writter-list-item latestNews')]})


        #re.compile('^company')
        #s=table.findAll('td')
        l1=[]
        links = []
        title=[]
        data2=data[0].find_all('div',{'class': [re.compile('^writter-list-item-story')]})


        for i in range(len(data2)):

            a=( data2[i].find('a'))

            links.append(a['href'])
        #print (links)   
        print ('starting')
        for story in links:
            count=0
            while count<10:
                try:
                    source =requests.get(story)
                    break
                except Exception as e:
                    print ('exception at sub stories')
                    to.write_log('',str(e))
                count=count+1
            #print (source.status_code)
            if count<9:
                soup = bs4.BeautifulSoup(source.text,"lxml")
                body=soup.body
                t=( body.find('h1'))
                content=body.find('div',{'class': [re.compile('story-detail')]})
                if (content is None):
                    print ('')
                else:
                    full=content.find_all('p')
                    l1.append('\n')
                    l1.append('   TITLE   ')
                    l1.append(t.text)
                    data_titles.append(t.text)
                    l1.append('\n')
                    stro=""
                    for i in range(len(full)):
                        l1.append(full[i].text)
                        stro=stro+full[i].text
                    l1.append('\n')
                    l1.append('-')
                    l1.append('\n')
                    data_content.append(stro)


        #to.write('thenews',l1)
        to.writecsv('thenews',data_titles,data_content)
        browser.quit()
        
        
def run():
    extract_Thenews('https://www.thenews.com.pk/latest-stories')
    
