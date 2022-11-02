import pandas as pd
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import string
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import nltk
from nltk import word_tokenize,pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import csv
import pandas as pd
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.ensemble import AdaBoostClassifier
import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from imblearn.over_sampling import SMOTE
import nltk
from nltk.tokenize import ToktokTokenizer
import os
import time
import datetime

now = datetime.date.today()
day_news=str(now)

class Genre_classifier:
    def _init_(self):
        return
    
    def retrieve_data(self):
        dataframe=pd.read_csv('/home/ahfahad/FYPWORK/Iteration III/Main/bbc-text (1).csv')
        dataframe.head()
        print ("Training Dataset For Genres")
        return dataframe
    
    def remove_null(self,dataframe):
        dataframe =dataframe[pd.notnull(dataframe['text'])]
        #dataframe.info()
        return dataframe
    
    def play_columns(self,dataframe):
        columns = ['category', 'text']
        dataframe = dataframe[columns]
        dataframe.columns
        dataframe.columns = ['category', 'text']
        return dataframe
    
    def create_categories(self,dataframe):
        
        dataframe['category_id'] = dataframe['category'].factorize()[0]
        category_id_df = dataframe[['category', 'category_id']].drop_duplicates().sort_values('category_id')
        category_to_id = dict(category_id_df.values)
        id_to_category = dict(category_id_df[['category_id', 'category']].values)
        return dataframe,category_to_id
    
    def TfIdfComputed(self,dataframe):
    
        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

        features = tfidf.fit_transform(dataframe.text).toarray()
        labels = dataframe.category_id
        #features.shape
        
        return tfidf,features,labels
    
    def computing_Bigrams(self,frequencies,features,labels,category_to_id):
        N = 2
        for Product, category_id in sorted(category_to_id.items()):
            features_chi2 = chi2(features, labels == category_id)
            indices = np.argsort(features_chi2[0])
            feature_names = np.array(tfidf.get_feature_names())[indices]
            unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
            bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
            #print("# '{}':".format(Product))
            #print("  . Most correlated unigrams:\n       . {}".format('\n       . '.join(unigrams[-N:])))
            #print("  . Most correlated bigrams:\n       . {}".format('\n       . '.join(bigrams[-N:])))
            
    def train_and_test(self,dataframe):
        X_train, X_test, y_train, y_test = train_test_split(dataframe['text'], dataframe['category'], random_state = 0)
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(X_train)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

        clf = LinearSVC().fit(X_train_tfidf, y_train)
        
        #print("Genre Predicted : batsman : ",clf.predict(count_vect.transform(["Died"])))
        return clf,count_vect
        
    def develop_graph(self,dataframe):
        
        fig = plt.figure(figsize=(8,6))
        dataframe.groupby('category').text.count().plot.bar(ylim=0)
        plt.show()
        
    #def predict_label(self,clf):
     #   print("Genre Predicted : ",clf.predict(count_vect.transform(["Pneumonia to kill nearly 11m children by 2030, study warns"])))
      

    def predict_labels(self,clf,count_vect,filename):
        arr_newstitles=[]
        arr_newscontent=[]
        arr_labels=[]
        filename="/home/ahfahad/FYPWORK/Iteration III/Clusters/clusters_"+day_news+"/cluster_"+day_news
        with open(filename+'.csv', mode='r') as csv_file:
            csv_reader=csv.DictReader(csv_file)
            line_count=0
            for row in csv_reader:
                if line_count==0:
                    line_count+=1
                arr_newstitles.append(row["Title"])
                arr_newscontent.append(row["News_content"])
                line_count+=1
        
        index=0
        while index<len(arr_newscontent):
            if (arr_newscontent[index]!='-'):
                var=clf.predict(count_vect.transform([arr_newscontent[index]]))
                arr_labels.append(var)
            else:
                arr_labels.append("-")
            index+=1
        
        
        return arr_newstitles,arr_newscontent,arr_labels
    
    def write_labels(self,arr_titles,arr_content,arr_labels):
        file_name="/home/ahfahad/FYPWORK/Iteration III/Clusters/clusters_"+day_news+"/clusters_label_"+day_news
        index=0
        with open(file_name+'.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Title','News_content','Genre'])
            while index<len(arr_titles):
                writer.writerow([arr_titles[index],arr_content[index],arr_labels[index]])
                index+=1
        print ("Classified Into Different Genres")
        return
        
    def calculate(self,dataframe):
        ind=0
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        count6=0
        while ind<len(dataframe):
            if (dataframe['category'].iloc[ind]=='tech'):
                count1+=1
            elif (dataframe['category'].iloc[ind]=='entertainment'):
                count2+=1
            elif (dataframe['category'].iloc[ind]=='business'):
                count3+=1    
            elif (dataframe['category'].iloc[ind]=='sport'):
                count4+=1
            elif (dataframe['category'].iloc[ind]=='politics'):
                count5+=1
            elif (dataframe['category'].iloc[ind]=='Health'):
                count6+=1
            ind+=1
        print (count1,count2,count3,count4,count5,count6)
        
        return
    
    
    def sampling(self,dataframe):
        count_class_0, count_class_1,count_class_2,count_class_3,count_class_4,count_class_5 = dataframe.category.value_counts()
        
        # Divide by class
        df_class_0 = dataframe[dataframe['category'] == 'sport']
        df_class_1 = dataframe[dataframe['category'] == 'business']
        df_class_2 = dataframe[dataframe['category'] == 'politics']
        df_class_3 = dataframe[dataframe['category'] == 'tech']
        df_class_4 = dataframe[dataframe['category'] == 'entertainment']
        df_class_5 = dataframe[dataframe['category'] == 'Health']
        
        df_class_1_over = df_class_1.sample(count_class_0, replace=True)
        df_class_2_over = df_class_2.sample(count_class_0, replace=True)
        df_class_3_over = df_class_3.sample(count_class_0, replace=True)
        df_class_4_over = df_class_4.sample(count_class_0, replace=True)
        df_class_5_over = df_class_5.sample(count_class_0, replace=True)
        df_test_over = pd.concat([df_class_0, df_class_1_over,df_class_2_over,df_class_3_over,df_class_4_over,df_class_5_over], axis=0)
        
        return df_test_over

    



def run():
	object_Genre=Genre_classifier()
	df=object_Genre.retrieve_data()

	df=object_Genre.sampling(df)

	df=object_Genre.play_columns(df)
	df,ctd=object_Genre.create_categories(df)
	frequencies,features1,labels1=object_Genre.TfIdfComputed(df)
	#object_Genre.computing_Bigrams(frequencies,features1,labels1,ctd)

	cumulative_freq,count_vect=object_Genre.train_and_test(df)
	arr_titles,arr_content,arr_labels=object_Genre.predict_labels(cumulative_freq,count_vect,"clusters.csv")

	object_Genre.write_labels(arr_titles,arr_content,arr_labels)
	#object_Genre.predict_label(cumulative_freq)
	#object_Genre.develop_graph(df)
