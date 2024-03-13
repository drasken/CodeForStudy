#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:04:51 2024

@author: drasken
"""

"""
Simple script to help me download pdf for university by Uni website
"""


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def downloadPdf():
    try:
        
        url = input("URL from wich to download -> ")
        
        response = requests.get(url) #for prof's site add param verify=False
        
        response.raise_for_status()
            
        pars = BeautifulSoup(response.text, 'html.parser')
            
        links = pars.find_all('a', href=True) #to deepen understanding
        
        for link in links:
            href = link['href']
            #print(href)
            
            if href.lower().endswith('.pdf'):
                # Build the absolute URL
                absolute_url = urljoin(url, href)
                
                pdf_name = href.split('/')[-1]
                
                with open(pdf_name, mode='wb') as pdf:
                    pdf_response = requests.get(absolute_url) #for prof's site add param verify=False
                    pdf_response.raise_for_status()
                    pdf.write(pdf_response.content)
                    print('File Downloaded\n')
    
    except requests.exceptions.RequestException as e:
        print(f'Error while downloading pfd: {e}')
    except Exception as e: #handling a generic error
        print(f'Generic error: {e}')

    
if __name__ == '__main__':
    downloadPdf()
