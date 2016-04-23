# JD Scraper
===
===
## Package Document
===
  * Python version: 2.7.9
  * Author: Guo Zhang
  * Date: 2016-4-23
  * Module version: 2.1
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
      * getTotalPageNumber.py (parse the HTML to get total page numbers of a category)
      * parseHTMl.py (parse the HTML)
        * writeData.py (write datas into files or databases)
      * ipProxiesList, proxiesList (IP proxies pool)
    * jdCategories.py (the categories required to be scrapered)
  * proxiesPool
    * getIP_xici.py (get IP proxies from xicidaili)-> proxiesList
    * ipChecker.py (check IP proxies)-> ipProxiesList
  * requirements.txt
    * requests
    * bs4
   
---
    
## CHANGELOG
===
  * Version 2.0(2016-4-21):    
      * first version of JD Scraper 
