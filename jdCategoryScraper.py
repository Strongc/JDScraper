# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-21'

__moduleVersion__ = '2.1'

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
import math

# import third-party modules
from bs4 import BeautifulSoup

# import my own modules
from getParameter import getParameter
from createFile import createFile
from unparseURL import unparseURL,unparseURL2  
from getPageHTML import getPageHTML 
from writeData import jdWriteData

#----------module import----------


#----------class definition----------

class PageScraper(object):
    'Produce HTMLs for the JD scraper'
    
    def __init__(self,categoryName,pageNum = 1,**urlParameter):
        'Define attributes for ScraperProducer'
        
        self.presentDay = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.presentTime = str(time.strftime('%H-%M-%S',time.localtime(time.time())))
        self.categoryName = categoryName
        self.parameters = getParameter(**urlParameter) 
        self.pageNum = pageNum
        self.logTime = '[{} {}]'.format(self.presentDay,str(time.strftime('%H:%M:%S',time.localtime(time.time()))))
        
        # requests
        self.pageURL = unparseURL(self.categoryName,self.parameters,self.pageNum) 
        self.html = getPageHTML(self.categoryName,self.pageURL) 
        self.pageURL2 = unparseURL2(self.categoryName,self.parameters,self.pageNum)
        self.html2 = getPageHTML(self.categoryName, self.pageURL2)
        
    def getTotalPageNumber(self):
        'Get total page number for a certain category of JD Scaper'
        
        if self.html == None:
            return None
        
        try:
            soup = BeautifulSoup(self.html,'html.parser')
            div_J_searchWrap = soup.body.find('div',attrs={'id':'J_searchWrap'})
            div_m_list = div_J_searchWrap.find('div',attrs={'class':'m-list'})
            div_ml_wrap = div_m_list.find('div',attrs={'class':'ml-wrap'})
            div_J_filter = div_ml_wrap.find('div',attrs={'id':'J_filter'})
            div_f_line_top = div_J_filter.find('div',attrs={'class':'f-line top'})
            div_J_topPage = div_f_line_top.find('div',attrs={'id':'J_topPage'})
            pageNumber = div_J_topPage.span.i.getText() 
            pageNumber = float(pageNumber)
            return int(math.ceil(pageNumber/2))                                      
        except Exception:
            print(self.logTime,'fail to get page number:',(self.pageURL).encode('utf-8'))
            return None
         
    def parseHTML(self):
        try:
            fileName = createFile(self.presentDay,self.presentTime,self.categoryName,self.parameters,self.pageNum) 
            self.parsePageHTML(self.html,fileName)
            self.parsePageHTML2(self.html2,fileName)
        except:
            
            return None
        
    def parsePageHTML(self,html,fileName):
        'Parse the HTML'
    
        if html == None:
            return None
    
        # parse the HTML
        try:
            soup = BeautifulSoup(html,'html.parser')
            div_J_searchWrap = soup.body.find('div',attrs={'id':'J_searchWrap'})
            div_m_list = div_J_searchWrap.find('div',attrs={'class':'m-list'})
            div_ml_wrap = div_m_list.find('div',attrs={'class':'ml-wrap'})
            div_J_goodsList = div_ml_wrap.find('div',attrs={'id':'J_goodsList'})
            ul = div_J_goodsList.ul
            self.parsePageHTML2(ul,fileName)
        except Exception:
            print(self.logTime,'parse error',(fileName).encode('utf-8'))
            return None  

    def parsePageHTML2(self,ul,fileName):
        'Parse the data from HTML'
        
        if ul == None:
            return None
            
        try:
            ul = BeautifulSoup(ul,'html.parser')
        except:
            pass 
                
        # parse the data
        __i__ = 1
        products = ul.find_all('li')
        for product in products:
    
            items = product.find_all('div',attrs={'class':'tab-content-item'})
            if items:
                for item in items:
                    indicator = jdWriteData(item,fileName)
                    if indicator == 0:
                        __i__ = 0  
            else:
                indicator = jdWriteData(product,fileName)
                if indicator == 0:
                    __i__ = 0
             
        # print write error
        if __i__ == 0:        
            print(self.logTime,'write error:',fileName.encode('utf-8'))

#----------class definition----------


#----------function definition----------

def jdPageScraper(categoryName,pageNum=1,**urlParameter):
    scraper = PageScraper(categoryName,pageNum,**urlParameter)
    scraper.parseHTML()    

  
def jdCategoryScraper(categoryName,**urlParameter):
    scraper = PageScraper(categoryName,**urlParameter)
    scraper.parseHTML()
    Number = scraper.getTotalPageNumber()
    #print('%s: page 1'%(categoryName))
    if Number:
        Number += 1
        for i in xrange(2,Number):
            scraper = PageScraper(categoryName, pageNum=i,**urlParameter)
            scraper.parseHTML()
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
