# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import---------

import time
import codecs
import csv

#----------module import---------


#----------function definition---------

def jdWriteData(product,fileName):
    indicator = 1
    
    try:
        goodsURL = product.find('div',attrs={'class':'p-name p-name-type-2'}).a['href']
        goodsURL = ''.join(['http:',goodsURL]).encode('utf-8')
    except:
        goodsURL = None
            
    try:
        goodsName = product.find('div',attrs={'class':'p-name p-name-type-2'}).a.em.get_text().encode('utf-8')
    except:
        goodsName = None
    
    try:
        id = product.find('div',attrs={'class':'p-price'}).strong['class'].encode('utf-8')
    except:
        id = None
        
    try:
        price = product.find('div',attrs={'class':'p-price'}).strong['data-price'].encode('utf-8')
    except:
        price = None
        
    try:
        commentsNum = product.find('div',attrs={'class':'p-commit'}).strong.a.get_text().encode('utf-8')
    except:
        commentsNum = None
        
    try:
        with codecs.open(fileName,'ab') as f:
            writer = csv.writer(f)
            writer.writerow((goodsURL,goodsName,id,price,commentsNum))           
    except:
        indicator = 0
        
    return indicator