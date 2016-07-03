# JD Scraper
===
===
## Package Document
===
  * Project name: JD Scraper
  * Project version: 3.0
  * Author: Guo Zhang
  * Contributer: Xingjian Lin,Lin Chen
  * Date: 2016-6-30
  * Python version: 2.7.9
  * Descrption: This is a JD scarper for China's Prices Project

---

## Package Structure
===
 * main.py (main function)
  * TmallPageScraper.py (a page scraper for Tmall)
    * dataCleaning.py (clean source data)
  * geventQueue.py (a gevent queue for Tmall and JD scrapers)
  * TmallCategories.py (the category list for Tmall)
  
  * decorator.py (decorators)

* proxiesPool
  * headers.py (user-agents and proxies for request headers) 
  * checkedProxies & proxies (IP proxies pool)

---

## requirements
===
   * requests
   * bs4
   * gevent
   * pymongo
   
---
    
## CHANGELOG
===
  * Version 3.0.2(2016-7-3)
    * modify bugs
  * Version 3.0.1(2016-7-1)
    * modify bugs
  * Version 3.0(2016-6-30)
    * rewrite the whole project. 
  * Version 2.6(2016-5-14)
    * add getPrice.py
    * edit writeData.py,createFile.py
    * add addedPrice item for data(addedPrice = None,'1','0')
  * Version 2.5(2016-5-12)
    * edit jdCategoryScraper.py
    * edit writeData.py
  * Version 2.3(2016-4-30)
    * add emailSending.py
	* add JD type sh
	* add logTime
  * Version 2.2(2016-4-27)
    * rewrite jdCategoryScraper.py
    * add unitTest
  * Version 2.1(2016-4-23)
    * rewrite scraperThreadPool.py
  * Version 2.0(2016-4-21)    
    * first version of JD Scraper 
