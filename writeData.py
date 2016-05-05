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
        goodsURLs = []
        goodsURL_divs = product.find_all('div',attrs={'class':'p-name p-name-type-2'})
        for goodsURL_div in goodsURL_divs:
            goodsURL = goodsURL_div.a['href']
            goodsURL = ''.join(['http:',goodsURL]).encode('utf-8')
            goodsURLs.append(goodsURL)
            
    except:
        goodsURLs = None
            
    try:
        goodsNames = []
        goodsName_divs = product.find_all('div',attrs={'class':'p-name p-name-type-2'})
        for goodsName_div in goodsName_divs:
            goodsName = goodsName_div.a.em.get_text().encode('utf-8')
            goodsNames.append(goodsName) 
    except:
        goodsNames = None
    
    try:
        ids = []
        id_divs = product.find_all('div',attrs={'class':'p-price'})
        for id_div in id_divs:
            id = id_div.strong['class'][0]
            id = id.encode('utf-8')
            ids.append(id)
    except:
        ids = None
        
    try: 
        prices = []
        price_divs = product.find_all('div',attrs={'class':'p-price'})
        for price_div in price_divs:
            price = price_div.strong.i.get_text().encode('utf-8')
            prices.append(price)
    except:
        prices = None
        
    try:
        commentsNums = []
        commentsNum_divs = product.find('div',attrs={'class':'p-commit'})
        for commentsNum_div in commentsNum_divs:
            commentsNum = commentsNum_div.a.get_text().encode('utf-8')
            commentsNums.append(commentsNum)
    except:
        commentsNums = None
        
    try:
        for goodsURL,goodsName,id,price,commentsNum in zip(goodsURLs,goodsNames,ids,prices,commentsNums):
            with codecs.open(fileName,'ab') as f:
                writer = csv.writer(f)
                writer.writerow((goodsURL,goodsName,id,price,commentsNum))           
    except:
        indicator = 0
        
    return indicator