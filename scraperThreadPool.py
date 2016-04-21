# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-17'

__moduleVersion__ = '2.0'

__doc__ = '''
This is a multithreading pool for a scarper 
'''

#----------module document----------


#----------module import----------

from threading import Thread
import time

from jdCategoryScraper import jdCategoryScraper
from jdCategories import CATEGORIES_NAME

#----------module import----------


#----------class definition----------

class ScraperThread(Thread):
    
    def __init__(self,function,categoryName,**urlParameters):
        self.categoryName = categoryName
        self.urlParameters = urlParameters
        self.function = function
        super(ScraperThread,self).__init__()
        
    def run(self):
        self.function(self.categoryName,**self.urlParameters)
        
#----------class definition----------
        
        
#----------function definition----------  
      
def scraperThreadPool(function,categories):
    
    threads =[]
    
    for category in categories:
        
        # parameters
        if type(category)== list:
            categoryName = category[0]
            try:
                if type(category[1]==dict):
                    urlParameters = category[1]
                else:
                    urlParameter = {}
            except IndexError:
                urlParameters = {}
        elif (type(category)== unicode or type(category)==str):
            categoryName = category
            urlParameters = {}
        else:
            print('Error: wrong jdCategories list!!'.encode('utf-8'))
            
        t = ScraperThread(function,categoryName,**urlParameters)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
#----------function definition---------- 

#----------unit test----------

if __name__ == '__main__':
    start = time.time()
    
    categories = CATEGORIES_NAME
    function = jdCategoryScraper
    scraperThreadPool(function,categories)
    
    end = time.time()
    print('time:',end-start)
    
#----------unit test----------