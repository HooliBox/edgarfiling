# Textual analysis in 10K reports  

This project intends to find if the part Risk Factors talked in company's 10K filing relates to it's stock performance. I plan to use nltk package to find the most commonly talked topic for all companies. Then for each company, gives each topic a score. and use some statistical analysis to see if the score relates to the performance or not.

### Detail about how to read 10K/10Q: [Link](https://www.sec.gov/fast-answers/answersreada10khtm.html)  


# Download data from web

## Getting the company and security data
Using SP500 as universe to study.Download SP500 data from [datahub.io](https://datahub.io/core/s-and-p-500-companies/). Try to use [Bloomberg Figi](https://openfigi.com/) API to map ticker to Bloomberg Global ID to gain a perminent security id. Then uses [Edgar company search](https://www.sec.gov/edgar/searchedgar/companysearch.html) to scrap the ticker to SEC Cik, which is a company level perminent key.  

### [download_spy_constituents](https://github.com/HooliBox/edgarfiling/blob/master/download_spy_constituents.ipynb)  

## Download the filings for these companies  

First find the [Filing Index](https://www.sec.gov/Archives/edgar/full-index/) for these securities.  
Based on the index, find the [10K/10Q](https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/0000320193-18-000070.txt)  

### [download_10k](https://github.com/HooliBox/edgarfiling/blob/master/download_10k.ipynb)  


# Extract Item 1A Risk Factors information from 10K  

### detail [clean_process_data](https://github.com/HooliBox/edgarfiling/blob/master/clean_process_data.ipynb), [another_way_of_processing](https://github.com/HooliBox/edgarfiling/blob/master/another_way_of_processing.ipynb)  


# Getting some analysis 
### [analysis](https://github.com/HooliBox/edgarfiling/blob/master/analysis.ipynb)