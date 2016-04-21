# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import----------

import time

#----------module import----------


#----------function definition----------

def unparseURL(categoryName,parameters,pageNum):
    'Create the first part of page URL'
    
    page = str(pageNum*2-1)
    s = str((pageNum-1)*60+1)
    
    try:
        urlFirst = u'http://search.jd.com/search?enc=utf-8&psort=3'
        query = ''.join([u'&page=',page,u'&s=',s,u'&keyword=',categoryName]) 
        pageURL = ''.join([urlFirst,query,parameters])
        return pageURL
    except Exception:
        print('unparsing URL error:',(categoryName).encode('utf-8'),(pageNum).encode('utf-8'))
        return None
    
    
def unparseURL2(categoryName,parameters,pageNum):
    'Create the second part of page URL'
    
    page = str(pageNum*2)
    s = str(pageNum*60-29)
    
    try:
        urlFirst =u'http://search.jd.com/s_new.php?enc=utf-8&psort=3&scrolling=y'
        query = ''.join([u'&page=',page,u'&s=',s,u'&keyword=',categoryName]) 
        pageURL2 = ''.join([urlFirst,query,parameters])
        return pageURL2
    except Exception:
        print('unparsing URL2 error:',(categoryName).encode('utf-8'),(pageNum).encode('utf-8'))
        return None
    
#----------function definition----------


#----------unit test----------
    
if __name__ =='__main__':
    
    begin = time.time()
    
    categoryName = u'酱油'
    parameters = u'&cid2=1584&cid3=2677&ev='
    pageNum = 1
    
    pageURL = unparseURL(categoryName, parameters, pageNum)
    pageURL2 = unparseURL2(categoryName, parameters, pageNum)
    
    print(pageURL)
    print(pageURL2)
    
    end = time.time()
    print('time:',end-begin)
    
#----------unit test---------