# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-21'

__moduleVersion__ = '2.0'

__doc__ = '''
This is a JD category scarper,
in order to get scraping time,url,name,id,price,and comments number
of the goods in a certain category.
'''

#----------module document----------


#----------module import----------

# import system modules
import time
import codecs
import csv

# import third-party modules
from bs4 import BeautifulSoup

# import my own modules
from getParameter import getParameter
from createFile import createFile
from unparseURL import unparseURL,unparseURL2  
from getPageHTML import getPageHTML 
from getTotalPageNumber import getTotalPageNumber  
from parseHTML import parsePageHTML,parsePageHTML2

#----------module import----------


#----------class definition----------

class PageScraper(object):
    'Produce HTMLs for the JD scraper'
    
    def __init__(self,categoryName,pageNum = 1,**urlParameter):
        'Define attributes for ScraperProducer'
        
        self.presentDay = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.categoryName = categoryName
        self.parameters = getParameter(**urlParameter) 
        self.pageNum = pageNum
        self.fileName = createFile(self.presentDay,self.categoryName,self.parameters,self.pageNum) 
        
        # requests
        self.pageURL = unparseURL(self.categoryName,self.parameters,self.pageNum) 
        self.html = getPageHTML(self.categoryName,self.pageURL) 
        self.totalPages = getTotalPageNumber(self.html,self.categoryName,self.parameters) 
        
        self.pageURL2 = unparseURL2(self.categoryName,self.parameters,self.pageNum)
        self.html2 = getPageHTML(self.categoryName, self.pageURL2)
         
    def parseHTML(self):
        parsePageHTML(self.html,self.fileName)
        parsePageHTML2(self.html2, self.fileName)

#----------class definition----------


#----------function definition----------

def jdPageScraper(categoryName,pageNum=1,**urlParameter):
    scraper = PageScraper(categoryName,pageNum,**urlParameter)
    scraper.parseHTML()    
    return scraper.totalPages

    
def jdCategoryScraper(categoryName,**urlParameter):
    Number = jdPageScraper(categoryName,**urlParameter) 
    #print('%s: page 1'%(categoryName))
    if Number:
        Number += 1
        for i in xrange(2,Number):
            jdPageScraper(categoryName,pageNum=i,**urlParameter)
            #print('%s: page %d'%(categoryName,i))
        
#----------function definition----------


#----------main function----------

if __name__ == '__main__':
    
    begin=time.time()
    
    categoryName = u'酱油'
    urlParameter = {'cid2':'1584','cid3':'2677','ev':''}  
    jdCategoryScraper(categoryName,**urlParameter)
    
    end = time.time()
    print('time:',end-begin)

#----------main function----------