import time
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
import datetime as dt
import re
import numpy as np
from datetime import date, datetime, timedelta
import re
import os

years_list = [ '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14' ]

for year in years_list:
    try:
        download_dir = Path.cwd() / ('rawpdf' + year)
        Path(download_dir).mkdir(parents=True, exist_ok=True)
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs',  {
            "download.default_directory": str(download_dir),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.plugins_disabled": ["Chrome PDF Viewer"],
            "plugins.always_open_pdf_externally": True
            }
        )
        browser = webdriver.Chrome(options=chrome_options)
        browser.get('https://posoco.in/reports/daily-reports/daily-reports-' + year)
        length_select = Select(browser.find_element_by_css_selector('div.dataTables_length > label > select'))
        length_select.select_by_visible_text('All')

        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, features='lxml')
        links = []
        for link in soup.find_all('a', href=True):
            link = link['href']
            if 'https://posoco.in/download/' in link and '_nldc_psp' in link:
                links.append(link)


        #get the new pdf from link
        for link in links:
            browser.get(link)

        while(True):
            files = ' '.join([str(x).lower() for x in (Path.cwd() / ('rawpdf' + year)).iterdir()])
            if '.crdownload' not in files: break
            time.sleep(2)
    finally:
        browser.quit()