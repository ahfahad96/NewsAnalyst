#imports

import pandas as pd
from textblob import TextBlob
import csv
import time
import datetime
import os

now = datetime.date.today()
day_news=str(now)

class Sentiment_Analysis:
    def _init_(self):
        return
    
    def computeSentimentScoreTextblob(self,article):
        return (TextBlob(article).sentiment.polarity)
    

    def computeSentimentCategoryTextblob(self,score):
        return ['positive' if score > 0  else 'negative' if score < 0  else 'neutral' ]


    def retrieve_data(self,filename):
        arr_score=[]
        arr_label=[]
        filename='/home/ahfahad/FYPWORK/Iteration III/Clusters/clusters_'+day_news+'/clusters_label_'+day_news
        dataframe_news=pd.read_csv(filename+".csv")
        dataframe_news['Score']='default value'
        dataframe_news['Label']='default value'
        
        index=0
        while index<len(dataframe_news):
            if (dataframe_news['News_content'].iloc[index]!='-'):
                dataframe_news['Score'].iloc[index]=self.computeSentimentScoreTextblob(dataframe_news['News_content'].iloc[index])
                dataframe_news['Label'].iloc[index]=self.computeSentimentCategoryTextblob(dataframe_news['Score'].iloc[index])
                
            else:
                dataframe_news['Score'].iloc[index]="-"
                dataframe_news['Label'].iloc[index]="-"
            index+=1
        
        
        return dataframe_news
    
    def write_to_file(self,dataframe_news):
        file_name="/home/ahfahad/FYPWORK/Iteration III/Clusters/clusters_"+day_news+"/clusters_label_score_"+day_news
        index=0
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Title','News_content','Genre','Score','Label'])
            while index<len(dataframe_news):
                writer.writerow([dataframe_news['Title'].iloc[index],dataframe_news['News_content'].iloc[index],dataframe_news['Genre'].iloc[index],dataframe_news['Score'].iloc[index],dataframe_news['Label'].iloc[index]])
                index+=1
        
        print ("Sentiment Analysis Completed")
        return
    
    def files_update(self):
        filename='/home/ahfahad/FYPWORK/Iteration III/Clusters/clusters_'+day_news+'/clusters_label_score_'+day_news
        dataframe=pd.read_csv(filename+".csv")
        index=0

        size1=0
        size2=0
        size3=0
        size4=0
        size5=0
        size6=0
        arr_politics=[0,0,0,0]
        arr_entertainment=[0,0,0,0]
        arr_tech=[0,0,0,0]
        arr_sport=[0,0,0,0]
        arr_business=[0,0,0,0]
        arr_health=[0,0,0,0]
        while index<len(dataframe):
            if (dataframe['Genre'].iloc[index]=="['politics']"):
                if (dataframe['Label'].iloc[index]=="['positive']"):
                    arr_politics[0]+=1
                elif (dataframe['Label'].iloc[index]=="['negative']"):
                    arr_politics[1]+=1
                else:
                    arr_politics[2]+=1
                arr_politics[3]+=float(dataframe['Score'].iloc[index])
                size1+=1

            elif (dataframe['Genre'].iloc[index]=="['entertainment']"):
                if (dataframe['Label'].iloc[index]=="['positive']"):
                    arr_entertainment[0]+=1
                elif (dataframe['Label'].iloc[index]=="['negative']"):
                    arr_entertainment[1]+=1
                else:
                    arr_entertainment[2]+=1
                arr_entertainment[3]+=float(dataframe['Score'].iloc[index])
                size2+=1

            elif (dataframe['Genre'].iloc[index]=="['sport']"):
                if (dataframe['Label'].iloc[index]=="['positive']"):
                    arr_sport[0]+=1
                elif (dataframe['Label'].iloc[index]=="['negative']"):
                    arr_sport[1]+=1
                else:
                    arr_sport[2]+=1
                arr_sport[3]+=float(dataframe['Score'].iloc[index])
                size3+=1

            elif (dataframe['Genre'].iloc[index]=="['tech']"):
                if (dataframe['Label'].iloc[index]=="['positive']"):
                    arr_tech[0]+=1
                elif (dataframe['Label'].iloc[index]=="['negative']"):
                    arr_tech[1]+=1
                else:
                    arr_tech[2]+=1
                arr_tech[3]+=float(dataframe['Score'].iloc[index])
                size4+=1

            elif (dataframe['Genre'].iloc[index]=="['business']"):
                if (dataframe['Label'].iloc[index]=="['positive']"):
                    arr_business[0]+=1
                elif (dataframe['Label'].iloc[index]=="['negative']"):
                    arr_business[1]+=1
                else:
                    arr_business[2]+=1
                arr_business[3]+=float(dataframe['Score'].iloc[index])
                size5+=1

            elif (dataframe['Genre'].iloc[index]=="['Health']"):
                if (dataframe['Label'].iloc[index]=="['positive']"):
                    arr_health[0]+=1
                elif (dataframe['Label'].iloc[index]=="['negative']"):
                    arr_health[1]+=1
                else:
                    arr_health[2]+=1
                arr_health[3]+=float(dataframe['Score'].iloc[index])
                size6+=1

            index+=1
        arr_politics[3]/=size1
        arr_entertainment[3]/=size2
        arr_sport[3]/=size3
        arr_tech[3]/=size4
        arr_business[3]/=size5
        arr_health[3]/=size6
        
        return arr_politics,arr_entertainment,arr_tech,arr_sport,arr_business,arr_health
    
    def write_to_fileback(self,arr_p,arr_e,arr_t,arr_s,arr_b,arr_h):
        #/home/ahfahad/FYPWORK/Iteration III/Details
        file_name="/home/ahfahad/FYPWORK/Iteration III/Details/politics_detail"
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            #writer.writerow(['Date','Genre','Positives','Negatives','Neutrals','Score'])
            writer.writerow([day_news,'politics',str(arr_p[0]),str(arr_p[1]),str(arr_p[2]),str(arr_p[3])])
            
        file_name="/home/ahfahad/FYPWORK/Iteration III/Details/entertainment_detail"
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            #writer.writerow(['Date','Genre','Positives','Negatives','Neutrals','Score'])
            writer.writerow([day_news,'entertainment',str(arr_e[0]),str(arr_e[1]),str(arr_e[2]),str(arr_e[3])])
        
        file_name="/home/ahfahad/FYPWORK/Iteration III/Details/tech_detail"
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            #writer.writerow(['Date','Genre','Positives','Negatives','Neutrals','Score'])
            writer.writerow([day_news,'tech',str(arr_t[0]),str(arr_t[1]),str(arr_t[2]),str(arr_t[3])])
        
        file_name="/home/ahfahad/FYPWORK/Iteration III/Details/sport_detail"
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            #writer.writerow(['Date','Genre','Positives','Negatives','Neutrals','Score'])
            writer.writerow([day_news,'sport',str(arr_s[0]),str(arr_s[1]),str(arr_s[2]),str(arr_s[3])])
            
        file_name="/home/ahfahad/FYPWORK/Iteration III/Details/business_detail"
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            #writer.writerow(['Date','Genre','Positives','Negatives','Neutrals','Score'])
            writer.writerow([day_news,'business',str(arr_b[0]),str(arr_b[1]),str(arr_b[2]),str(arr_b[3])])
            
        file_name="/home/ahfahad/FYPWORK/Iteration III/Details/health_detail"
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            #writer.writerow(['Date','Genre','Positives','Negatives','Neutrals','Score'])
            writer.writerow([day_news,'health',str(arr_h[0]),str(arr_h[1]),str(arr_h[2]),str(arr_h[3])])
        
        return




def run():
	object_sentiment=Sentiment_Analysis()
	dataframe_news=object_sentiment.retrieve_data("clusters_label")
	object_sentiment.write_to_file(dataframe_news)
	arr_p,arr_e,arr_t,arr_s,arr_b,arr_h=object_sentiment.files_update()
	object_sentiment.write_to_fileback(arr_p,arr_e,arr_t,arr_s,arr_b,arr_h)

