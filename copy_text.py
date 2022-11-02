import shutil
import os

def copyfun():
    os.unlink('/home/ahfahad/Dropbox/News/entertainment_detail.csv')
    os.unlink('/home/ahfahad/Dropbox/News/business_detail.csv')
    os.unlink('/home/ahfahad/Dropbox/News/health_detail.csv')
    os.unlink('/home/ahfahad/Dropbox/News/politics_detail.csv')
    os.unlink('/home/ahfahad/Dropbox/News/sport_detail.csv')
    os.unlink('/home/ahfahad/Dropbox/News/tech_detail.csv')

    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/Details/entertainment_detail.csv', '/home/ahfahad/Dropbox/News')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/Details/business_detail.csv', '/home/ahfahad/Dropbox/News')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/Details/health_detail.csv', '/home/ahfahad/Dropbox/News')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/Details/politics_detail.csv', '/home/ahfahad/Dropbox/News')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/Details/sport_detail.csv', '/home/ahfahad/Dropbox/News')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/Details/tech_detail.csv', '/home/ahfahad/Dropbox/News')
    
    os.unlink('/home/ahfahad/Dropbox/NewsGenre/entertainment_news.csv')
    os.unlink('/home/ahfahad/Dropbox/NewsGenre/business_news.csv')
    os.unlink('/home/ahfahad/Dropbox/NewsGenre/health_news.csv')
    os.unlink('/home/ahfahad/Dropbox/NewsGenre/politics_news.csv')
    os.unlink('/home/ahfahad/Dropbox/NewsGenre/sports_news.csv')
    os.unlink('/home/ahfahad/Dropbox/NewsGenre/tech_news.csv')

    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/NewsGenre/entertainment_news.csv', '/home/ahfahad/Dropbox/NewsGenre')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/NewsGenre/business_news.csv', '/home/ahfahad/Dropbox/NewsGenre')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/NewsGenre/health_news.csv', '/home/ahfahad/Dropbox/NewsGenre')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/NewsGenre/politics_news.csv', '/home/ahfahad/Dropbox/NewsGenre')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/NewsGenre/sports_news.csv', '/home/ahfahad/Dropbox/NewsGenre')
    newPath = shutil.copy('/home/ahfahad/FYPWORK/Iteration III/NewsGenre/tech_news.csv', '/home/ahfahad/Dropbox/NewsGenre')

def run():
    copyfun()
