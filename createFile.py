# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals

#----------module import---------

import os
import time
import codecs
import csv

#----------module import----------


#----------function definition----------

def createFile(presentDay,presentTime,categoryName,parameters,pageNum):
    'Create file and its name for a certain page'
    
    # check or create a daily dictionary
    dictionaryName = u'JDData_' + presentDay
    try:
        os.makedirs(dictionaryName)
    except OSError, e:
        if e.errno != 17:
            raise(e)
        
    # create a file and its name for a certain page
    if parameters:
        fileName = ''.join([dictionaryName,'/','jdPrice','_',presentDay,'_',presentTime,'_',categoryName,'_',parameters,'_',str(pageNum)])
    else:
        fileName = ''.join([dictionaryName,'/','jdPrice','_',presentDay,'_',presentTime,'_',categoryName,'_',str(pageNum)])
    
    # write the first line
    with codecs.open(fileName,'wb',) as f:
        writer = csv.writer(f)
        writer.writerow(('goodsURL','goodsName','ID','price','commentsNum','addedPrice'))
  
    return fileName

#----------function definition----------
        

#----------unit test----------
        
if __name__ == '__main__':
    begin = time.time()
    presentDay = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    categoryName = u'酱油'
    parameters = '&cid2=1584&cid3=2677&ev='
    pageNum = 1
    fileName = createFile(presentDay, categoryName, parameters, pageNum)
    print(fileName)
    end = time.time()
    print('time:',end-begin)
    
#----------unit test----------

#----------test result---------

'''Warning: 
the fileName of jd is
JDData_2016-04-21/jdPrice_2016-04-21_酱油_&cid2=1584&cid3=2677&ev=109515_624887%40_1
which the value of 'ev' has a '_'. It should be cared about when dealing with file names
'''
    
#----------test result---------