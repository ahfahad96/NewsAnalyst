#from here
#globals
#model code

#from here
#globals
#model code

import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import datetime
import string
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
from gensim.models.doc2vec import Doc2Vec
import time
import datetime
import os

data_newstitles=[]
data_newscontent=[]
data_newstitles=[]
data_newscontent=[]
tagged_data_titles=[]
tagged_data_content=[]

#now = datetime.datetime.now()
now = datetime.date.today()
day_news=str(now)


def retrieve_Data(name_of_file):
    with open(name_of_file, mode='r') as csv_file:
            csv_reader=csv.DictReader(csv_file)
            line_count=0
            for row in csv_reader:
                if line_count==0:
                    line_count+=1
                #print(row["Title"]," = ",row["News_content"])
                data_newstitles.append(row["Title"])
                data_newscontent.append(row["News_content"])
                line_count+=1
            print(f'Processed {line_count} lines.')

def write_Data_back():
    with open(day_news+'.csv', mode='w') as csv_file:
        fieldnames = ['Title', 'News_content']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        ind=0
        for line in data_newstitles:
            
            writer.writerow({'Title': line, 'News_content': data_newscontent[ind]})
            ind=ind+1   



class Similarity_finder:
    def _init_(self):
        return
    
    def retrieve_Data(self):
        with open('news.csv', mode='r') as csv_file:
            csv_reader=csv.DictReader(csv_file)
            line_count=0
            for row in csv_reader:
                if line_count==0:
                    line_count+=1
                data_newstitles.append(row["Title"])
                data_newscontent.append(row["News_content"])
                line_count+=1
            print(f'Processed {line_count} lines.')
            
    def stemming(self,text):
        ps = PorterStemmer()
        tokenized_text=nltk.word_tokenize(text)
        stemmed_text = ""
        ind=""
        for word in tokenized_text:
            ind=ps.stem(word)
            stemmed_text=stemmed_text+ind+" "
        return stemmed_text

    def lemmatization(self,text):
        tokenized_text=nltk.word_tokenize(text)
        lemmatized_text=WordNetLemmatizer()
        cleaned_text=""
        for word,tag in pos_tag(tokenized_text):
            word_tag=tag[0].lower()
            word_tag=word_tag if word_tag in ['a', 'r', 'n', 'v'] else None
            if not word_tag:
                lemma=word
            else:
                lemma=lemmatized_text.lemmatize(word, word_tag)
            cleaned_text+=lemma+" "
        return cleaned_text

    def remove_stopwords(self,text):
        tokenized_text=nltk.word_tokenize(text)
        text_nostopwords = ""
        stoplist = stopwords.words('english')
        for i in tokenized_text:
            if i not in stoplist:
                text_nostopwords=text_nostopwords+i+" "
        return text_nostopwords

    def punctuation_removal(self,text):
        cleaned_text=''
        for letter in text:
            if letter not in string.punctuation:
                cleaned_text+=letter
            else:
                cleaned_text+=" "
        return cleaned_text

            
    def cleaning_of_text(self,text):
        cleaned_text=""
        cleaned_text=self.punctuation_removal(text)
        cleaned_text=self.remove_stopwords(cleaned_text)
        #cleaned_text=stemming(cleaned_text)
        cleaned_text=self.lemmatization(cleaned_text)
        return cleaned_text
        
    def tag_documents(self):
        index=0
        while index<len(data_newstitles):
            data_newstitles[index]=self.cleaning_of_text(data_newstitles[index])
            data_newscontent[index]=self.cleaning_of_text(data_newscontent[index])
            index+=1
    
        tagged_data_titles = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data_newstitles)]
        tagged_data_content = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data_newscontent)]
        return tagged_data_titles,tagged_data_content
    
    def train_Distributed_Document(self,vec_titles,vec_content):
        max_epochs =100
        vec_size = 300
        alpha = 0.025
        model = Doc2Vec(size=vec_size,alpha=alpha,min_alpha=0.00025,min_count=1,dm =1)
  
        model.build_vocab(vec_content)

        for epoch in range(max_epochs):
            print('iteration {0}'.format(epoch))
            model.train(vec_content,total_examples=model.corpus_count,epochs=model.iter)
            # decrease the learning rate
            model.alpha -= 0.0002
            # fix the learning rate, no decay
            model.min_alpha = model.alpha

        model.save("distributed_documents.model")
        print("Training of Model Completed")
        return
    
    def compute_similarity(self,vec_content):
        model= Doc2Vec.load("distributed_documents.model")
        ##to find the vector of a document which is not in training data
        #test_data = word_tokenize("Iran is facing a tough time against syria".lower())
        #v1 = model.infer_vector(test_data)
        #print("V1_infer", v1)
    
        # to find most similar doc using tags
        newpath=r'/home/ahfahad/FYPWORK/Iteration III/Clusters/clusters_'+day_news
        file_name="cluster_"+day_news;
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        os.chdir(newpath)
        index_of_file=0;
        index_out=0
        index_in=0
        arr_for_rep=[]
        fieldnames = ['Title', 'News_content']
        with open(file_name+'.csv', "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Title','News_content'])
        while index_out<len(vec_content):
            number=0
            if (index_out in arr_for_rep):
                index_out+=1
            else:
                index_in=0
                check_of_news=0
                similar_doc = model.docvecs.most_similar(index_out)
                while index_in<len(similar_doc):
                    if (similar_doc[index_in][1]>0.73):
                        number=int(similar_doc[index_in][0])
                        #fieldnames = ['Title', 'News_content']
                        with open(file_name+'.csv', "a") as csv_file:
                            #writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            #writer.writeheader()
                            writer=csv.writer(csv_file)
                            if (check_of_news==0):
                                writer.writerow([data_newstitles[index_out],data_newscontent[index_out]])
                                check_of_news+=1
                                arr_for_rep.append(index_out)
                        
                            
                            arr_for_rep.append(number)
                            writer.writerow([data_newstitles[number],data_newscontent[number]])
                    
                        #print ("-----")
                        print (similar_doc[index_in])
                        print ("-----")
            
                    index_in+=1
                #print ("finish")
                index_of_file+=1
                if (check_of_news>0):
                    with open(file_name+'.csv', "a") as csv_file:
                        writer=csv.writer(csv_file)
                        writer.writerow(["-","-"])
                check_of_news=0
                index_out+=1
                
        index1=0
        while index1<len(data_newstitles):
            if (index1 not in arr_for_rep):
                with open(file_name+'.csv', "a") as csv_file:
                    writer=csv.writer(csv_file)
                    writer.writerow([data_newstitles[index1],data_newscontent[index1]])
                    writer.writerow(["-","-"])
            
            index1+=1
            
            
        print ("Similarity Computed")    
        return
        
            



def run():
	retrieve_Data('/home/ahfahad/FYPWORK/Iteration III/Data/news_of_'+day_news+'/Dawn_news'+day_news+'.csv')
	retrieve_Data('/home/ahfahad/FYPWORK/Iteration III/Data/news_of_'+day_news+'/thenews'+day_news+'.csv')
	retrieve_Data('/home/ahfahad/FYPWORK/Iteration III/Data/news_of_'+day_news+'/tribune'+day_news+'.csv')
	write_Data_back()
	i=0

	object_similarity=Similarity_finder()

	tagged_data_titles1=[]
	tagged_data_content1=[]
	tagged_data_titles1,tagged_data_content1=object_similarity.tag_documents()

	object_similarity.train_Distributed_Document(tagged_data_titles1,tagged_data_content1)
	object_similarity.compute_similarity(tagged_data_content1)


