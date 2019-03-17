# Retrieving data from a webpage


### Description

The script uses tools from the Beautiful Soup Python library to pull data out of webpages.
It first uses Selenium to access to an internet webpage protected with identifier 
and password and read its contents. 

In this particular script, we aim to retrieve, from 
a geocaching webpage, the list of visitors of a geocache.

Once the cache GCcode, your identifier and password have been provided, the information is 
used to connect to the website and access to the correct page. 
BeautifulSoup is then used to read the full page, extract the log table, treat the chain 
of characters to save the logs in a csv table (test.csv created). 




### Prerequisites


To run the script, you will need to install several Python libraries installed, including
pandas, Beautiful Soup and Selenium.


You can install Beautiful Soup and Selenium on your machine via pip:
```
pip install beautifulsoup4

```
```
pip install selenium
```


Documentation can be found at
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
and
https://selenium-python.readthedocs.io/installation.html




## How to use the script PredictDustpedia.py:

**Inputs:** 

GCcode : GC code of the cache you want to treat

MyIdentifier : geocaching personal identifier

MyPassword : password associated


**Output** 

test.csv file to save the log table and the list of geocachers that logged the cache



## Versioning

We use python 2.7.12. 


## Authors

* **Maud Galametz** 

