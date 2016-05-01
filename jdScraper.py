# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module document----------

__pyVersion__ = '2.7.9'

__author__ = 'Guo Zhang'

__date__ = '2016-4-21'

__moduleVersion__ = '2.0'

__doc__ = '''
This is a JD scarper,
in order to get scraping time,url,name,id,price,and comments number
of the goods in the categories list.
'''

#----------module document----------


#----------module import----------

# import system modules
import time

# import my own modules
from jdCategoryScraper import jdCategoryScraper
from jdCategories import CATEGORIES_NAME
from scraperThreadPool import scraper

#----------module import----------


#----------function rename----------

scraperFunction = jdCategoryScraper

#----------function rename----------


#----------function definition----------

def jdScraper():
    begin = time.time()

    categories = CATEGORIES_NAME
    scraper(scraperFunction, categories)
    
    end = time.time()
    print('time:',end-begin)
    print('Web scraping is over')

#----------function definition----------


#----------main function----------

if __name__ == '__main__':
    jdScraper()

#----------main function----------