# Sentiment Analysis- Amazon Mobile Phones Product Reviews

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Project Evaluation](#project-evaluation)
  * [Technologies Used](#technologies-used)
  * [License](#license)
  
  
## Overview
Sentiment analysis refers to the class of computational and natural language processing based techniques used to identify, extract or characterize subjective information, such as opinions, expressed in a given piece of text. The main purpose of sentiment analysis is to classify a writer’s attitude towards various topics into positive, negative or neutral categories.Sentiment analysis has gain much attention in recent years. In this paper, we aim to tackle the problem of sentiment polarity categorization, which is one of the fundamental problems of sentiment analysis. A general process for sentiment polarity categorization is proposed with detailed process descriptions. Data used in this study are online product reviews collected from amazon. Experiments for both sentence-level categorization and review-level categorization are performed with promising outcomes. At last, we also give insight into our future work on sentiment analysis.


## Objective
Scrape the customer reviews for 10 mobile phones listed on Amazon and perform Sentiment Analysis for the customer reviews.


## Procedure:

1. Go to amazon.in and scrape the customer reviews of 100 mobile phones
2. Develop a Sentiment Analysis model using the data provided as training data
3. Using the model you developed evaluate the sentiment of the customer reviews scraped by you.


## Project Deliverables:
1. Send us a copy of the code used to scrape the customer reviews. Your case study will be evaluated on how fast your program scrapes the reviews
2. Send us the code of your Sentiment Analysis model along with EDA.
3. Submit an excel sheet with the names of all the mobile phones along with the Fine-grained sentiment analysis score of the customer reviews for all the mobile phones
4. Submit data visualizations to represent your sentiment analysis results.
5. Please make sure your code is well commented.


## Installation
1. Creating a project environment:
```
python -m venv project_env
```
Activating the enviroment:
```
project_env\Scripts\activate.bat
```


2. The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```
pip install -r requirements.txt
```


3. Installing Scrapy :

We will start by installing Scrapy in our system. There can be two cases here though. If you are using conda, then you can install scrapy from the conda-forge using the following command:
```
conda install -c conda-forge scrapy
```
In case you are not using conda, you can use pip and directly install it in your system using the below command:
```
pip install scrapy
```

This will install the following libraries:

```
attrs            20.2.0
Automat          20.2.0
beautifulsoup4   4.9.3
bs4              0.0.1
certifi          2020.6.20
cffi             1.14.3
chardet          3.0.4
click            7.1.2
constantly       15.1.0
cryptography     3.1.1
cssselect        1.1.0
cycler           0.10.0
Cython           0.29.14
gensim           3.8.3
h5py             2.10.0
hyperlink        20.0.1
idna             2.10
incremental      17.5.0
itemadapter      0.1.1
itemloaders      1.0.3
jmespath         0.10.0
joblib           0.17.0
Keras            2.4.3
kiwisolver       1.2.0
lxml             4.6.0
matplotlib       3.3.2
nltk             3.5
numpy            1.19.2
pandas           1.1.3
parsel           1.6.0
Pillow           8.0.0
pip              19.0.3
Protego          0.1.16
pyasn1           0.4.8
pyasn1-modules   0.2.8
pycparser        2.20
PyDispatcher     2.0.5
PyHamcrest       2.0.2
pyOpenSSL        19.1.0
pyparsing        2.4.7
python-dateutil  2.8.1
pytz             2020.1
PyYAML           5.3.1
queuelib         1.5.0
regex            2020.10.15
requests         2.24.0
scikit-learn     0.23.2
scipy            1.5.3
Scrapy           2.4.0
seaborn          0.11.0
service-identity 18.1.0
setuptools       40.8.0
six              1.15.0
sklearn          0.0
smart-open       3.0.0
soupsieve        2.0.1
threadpoolctl    2.1.0
tqdm             4.50.2
Twisted          20.3.0
urllib3          1.25.10
w3lib            1.22.0
zope.interface   5.1.2
```

4. Save amazon_reviews.py amazon_reviews_scraping\amazon_reviews_scraping\spiders in order to scrape data from the spider we created above.

## Run

### > Step-1
We will start by creating a scrapy project. A scrapy project enables users to collate different components of the crawlers into a single folder. To create a scrapy project use following command

```
scrapy startproject amazon_reviews_scraping
```

### > Step-2
Once we have the project in place, we need to create a spider. A spider is a chunk of python code that determines how a web page will be scrapped. It is the main component that crawls different web pages and extracts content out of it. In our case, this will be the code chuck that will perform the task of visiting Amazon and scraping Amazon reviews. To create a spider, you can use the following command:

```
scrapy genspider amazon_review your-link-here
```

### > Step-3
Storing Scraped Results
Finally, we have successfully built our spider. The only task now left is to run this spider. We can run this spider by using the runspider command. It takes to input the spider file to run and the output file to store the collected results. In the case below, spider file is amazon_reviews.py and the output file is reviews.csv

```
scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_reviews.py -o reviews.csv
```

### > Step-4
Open Jupyter Notebook and run 'Sentiment Analysis- Amazon Mobile Phone Products Reviews.ipynb' in order to train your custom dataset within your loacl machine and preprocess the dataset followed by Modeling meanwhile.
