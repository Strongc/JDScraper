# JD Scraper
===
===
## Package Document
===
  * Project name: JD Scraper
  * Project version: 2.6
  * Author: Guo Zhang
  * Contributer: Xingjian Lin
  * Date: 2016-5-14
  * Python version: 2.7.9
  * Descrption: This is a JD scarper for China's Prices Project

---

## Package Structure
===
  * jdScraper.py (Main function)
    * scraperThreadPool (a thread pool for a scraper)
      * catPara.py (deal with parameters to the scraper function)
    * jdCategoryScraper.py (a category scraper)
      * getParameter.py (unparse parameters for a URL)
      * createFile.py (create a file name for a page)
      * unparseURL.py (create URL for requests)
      * getPageHTML.py (requests for HTMLs)
      * writeData.py (write datas into files or databases)
         * getPrice.py (get price information if no price information from html)
      * ipProxiesList, proxiesList (IP proxies pool)
    * jdCategories.py (the categories required to be scrapered)
  * proxiesPool
    * getIP_xici.py (get IP proxies from xicidaili)-> proxiesList
    * ipChecker.py (check IP proxies)-> ipProxiesList
  * unitTest
    * countData.py (count data, including category number,parameters number and file number) -> stat/ )
    * jdListTest.py(test parameter groups) -> categoriesTest
  * requirements.txt
    * requests
    * bs4
   
---
    
## CHANGELOG
===
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
