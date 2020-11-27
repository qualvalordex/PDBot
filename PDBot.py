# -*- coding: utf-8 -*-

import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class PDBot:
    def __init__(self):
        pass

    def wd_init(self):
        # Ignore webdriver warnings
        warnings.filterwarnings('ignore')

        # Webdriver configure
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(executable_path='./chromedriver_linux.exe', options=self.chrome_options)
    
    def get_protein_img(self, pdb_reference):
        # Initialize webdriver
        self.wd_init()

        # Load PDB protein page
        try:
            self.browser.get('https://www.rcsb.org/structure/' + pdb_reference)
        except:
            self.browser.close()
            print('Error: Could not load asked page.')

        # Get image url
        try:
            img_url = self.browser.find_element_by_css_selector('img.mainImage').get_attribute('src')
            self.browser.close()
        except:
            self.browser.close()
            print('Error: Could not find image selector.')

        return img_url