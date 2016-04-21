# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import----------

import time

#----------module import----------


#----------function definition----------

def getParameter(**urlParameter):
    'get parameters of an URL and join them together to be part of URL'
    
    parameters = ''
    for parameterTuple in urlParameter.items():
        addedParameter = ''.join([parameterTuple[0],'=',parameterTuple[1]])
        parameters = '&'.join([parameters,addedParameter])
    return parameters

#----------function definition----------


#----------unit test----------

if __name__ =='__main__':
    begin = time.time()
    urlParameter = {'cid2':'1584','cid3':'2677','ev':'',}  
    parameters = getParameter(**urlParameter)
    print(parameters)
    end = time.time()
    print('time:',end-begin)

#----------unit test----------    