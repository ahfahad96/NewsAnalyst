
import time
import datetime
import os
import csv


def writecsv(filename,data1,data2):

    now = datetime.date.today()
    d='NEWS OF'
    newpath = r'/home/ahfahad/FYPWORK/Iteration III/Data/news_of_' 
    a=str(now)
    newpath=newpath+a
    date=filename+str(now)
    date=date+".csv"

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    os.chdir(newpath)
    with open(date,mode='w') as csv_file:
        fieldnames=['Title','News_content']
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        i=0
        j=0
        print ("size 1: ",(len(data1)))
        print ("size 2: ",(len(data2)))
        for i in range(len(data1)):
            writer.writerow({'Title':data1[i],'News_content':data2[i]})




def write(filename,data):
    now = datetime.date.today()
    d='NEWS OF'
    newpath = r'/home/ahfahad/FYPWORK/Iteration III/Data/news_of_' 
    a=str(now)
    newpath=newpath+a
    date=filename+str(now)

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    os.chdir(newpath)
    filee = open(date,'a') 
    for word in data:
        filee.write(word)

    filee.close()
    
    
    
def write_log(filename,data):
    now = datetime.date.today()
    d='NEWS OF'
    newpath = r'/home/ahfahad/FYPWORK/Iteration III/Data/news_of_' 
    a=str(now)
    newpath=newpath+a
    filename='log_of '
    date=filename+str(now)

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    os.chdir(newpath)
    file1 = open(date,'a')
    file1.write('\n')
    for word in data:
        file1.write(word)


    file1.close()

