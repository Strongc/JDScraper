# crontab

* crontab -e

* choose 3 (first time)

* edit
  * minute hour \* \* \* sh /home/ubuntu/JDScraper/serverManager/jdscraper.sh >> /home/ubuntu/log/jdscraper.log 2>&1
  * minute hour \* \* \* sh /home/ubuntu/JDScraper/serverManager/jdrar.sh >> /home/ubuntu/log/jdrar.log 2>&1
  * minute hour \* \* \* sh /home/ubuntu/JDScraper/serverManager/jdemail.sh >> /home/ubuntu/log/jdemail.log 2>&1