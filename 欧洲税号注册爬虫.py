# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:53:20 2019

@author: Xinji
"""
import os
import  time 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
from selenium.webdriver.chrome.options import Options

def get_data():
    data = pd.ExcelFile('VAT Number.xlsx')
    df = data.parse(data.sheet_names[0])
    return df
 
'''
find the edi fit your own env
webdriver chrome dowload in:http://chromedriver.chromium.org/downloads
'''    


if __name__ == '__main__':
    
    your_path = str(input('input your path of chorm driver:  '))
    tic = time.time()
    check_result  = []
    df = get_data()
    
    '''get date'''
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    '''option to make driver work background'''
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    
    '''open browser'''
    driver = webdriver.Chrome(executable_path = your_path+'/chromedriver')  # Optional argument, if not specified will search path.
    url = 'http://ec.europa.eu/taxation_customs/vies/vatResponse.html'
    try:
        os.mkdir(your_path+'/'+now)
    except:
        pass
    for i in range(len(df)):

        driver.get(url)
        '''locate button'''
        select = Select(driver.find_element_by_name('memberStateCode'))
        element = driver.find_element_by_id("number")
        element.send_keys(str(df['Vat number'][i]))
        select.select_by_value(df['Country'][i])
        driver.find_element_by_id("submit").click()
        driver.save_screenshot(filename = your_path+'/'+now+'/'+df['Name'][i]+'.jpg')