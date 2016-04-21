# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import---------

import time
import codecs
import math

from bs4 import BeautifulSoup

#----------module import----------


#----------function definition----------

def getTotalPageNumber(html,categoryName,parameters):
    'Get total page number for a certain category of JD Scaper'
    
    if html == None:
        return None
    
    try:
        soup = BeautifulSoup(html,'html.parser')
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
        print('fail to get page number:',(categoryName).encode('utf-8'),parameters.encode('utf-8'))
        return None
    
#----------function definition---------


#----------unit test----------

if __name__ =='__main__':
    
    begin = time.time()
    
    categoryName = u'酱油'
    parameters =  u'&cid2=1584&cid3=2677&ev='
    html = codecs.open('unitTest_html')
    totalPageNumber = getTotalPageNumber(html, categoryName,parameters)
    print(totalPageNumber)
    
    end = time.time()
    print('time:',end-begin)
    
#----------unit test----------
