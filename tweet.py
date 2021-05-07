#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:53:55 2021

@author: macbook
"""
import tweepy


class Tweet:
    
    def __init__(self,
                 consumerkey = '4W9FJLSbFxgvasSSY0Vyz9IXF',
                 consumersecret='9ncAtYMS0IffTJYTbzMRpoCQWK7acc6q7bAsA3adNwRqmX0a56',
                 accestoken='1005545810485022720-X5ZawfK0JHl7lifdGVULSVygZDPkyu',
                 accestokenSecret='iTyp6yjNu4dCDbOxvLSoAs7YiyKLCawOCYt9UfminRkgf',
                 ):
        
        self.consumerkey = consumerkey
        self.consumersecret = consumersecret
        self.accestoken = accestoken
        self.accestokenSecret = accestokenSecret
        
    def takeTweets_user(self,userName,items):
        auth = tweepy.OAuthHandler(self.consumerkey,self.consumersecret)
        auth.set_access_token(self.accestoken,self.accestokenSecret)
        api = tweepy.API(auth)
            
        tweets = []
        self.userName = userName
        self.items = items
        for i in tweepy.Cursor(api.user_timeline,id = userName,tweet_mode="extended").items(items):
            tweets.append(i.full_text)
                
        return tweets
    
    def gezinme(self,cümle,kelimeler):
        emptyList = []
        cümleYeni = cümle.split(' ')
        emptyList.extend(cümleYeni)
        
        for x in emptyList:
            
            if x in kelimeler:
                return True
        return False
    def putInListandWrite(self,userName,items,dic):
        olumluList = dic['olumlu']
        olumsuzList = dic['olumsuz']
        olumluYazı = []
        olumsuzYazı = []
        tweets = self.takeTweets_user(userName,items)
        for cümleler in tweets:
            if t1.gezinme(cümleler,olumluList) == True:
                olumluYazı.append(cümleler+'\n')
            elif t1.gezinme(cümleler,olumsuzList) == True:
                olumsuzYazı.append(cümleler+'\n')
        with open("olumlu3.txt","w",encoding="utf-8") as file1:
            for olumlu in olumluYazı:
                file1.write(olumlu)
        
        with open("olumsuz3.txt","w",encoding="utf-8") as file2:
            for olumsuz in olumsuzYazı:
                file2.write(olumsuz)  
                
        

t1 =Tweet()

        
d = {'olumlu' : ["looking",'start','Projesi','dog','Herkes','shot'],
      'olumsuz': ['@SpaceX','promising','class','please','@DavidSpade','gereken']}

t1.putInListandWrite('elonmusk',5,d)



            
            
           
                
                
            
            
        
        
        


