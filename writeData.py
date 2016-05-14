# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import---------

import time
import codecs
import csv

from getPrice import getPrice

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
        id = product.find('div',attrs={'class':'p-price'}).strong['class'][0].encode('utf-8')
    except:
        id = None
        
    try:
        price = product.find('div',attrs={'class':'p-price'}).i.get_text().encode('utf-8')
        addedPrice = None
        if not price:
            price = getPrice(id)
            addedPrice = '1'
    except:
        price = None
        addedPrice = '0'
            
    # if addedPrice = None: it is normal
    # elif addedPrice = '1': it is a binding goods of last goods
    # elif addedPrice = '0': there is no price infromation
        
    try:
        commentsNum = product.find('div',attrs={'class':'p-commit'}).strong.a.get_text().encode('utf-8')
    except:
        commentsNum = None
        
    #try:
    with codecs.open(fileName,'ab') as f:
        writer = csv.writer(f)
        writer.writerow((goodsURL,goodsName,id,price,commentsNum,addedPrice))  
    
    #except:
        #indicator = 0
        
    return indicator