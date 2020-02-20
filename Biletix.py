from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json


class Biletix:
    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            options=chromeOptions, executable_path=r"C:\\Users\\b_ozelsel\\Pictures\\chromedriver.exe")
        self.navigate_link('https://www.biletix.com/')

    def navigate_link(self, link):
        self.driver.get(link)

    def music_events(self):
		driver = self.driver
		musicEvents = []
        self.navigate_link('https://www.biletix.com/category/MUSIC/TURKIYE/tr')
		try:
			driver.find_element_by_id('showhotcat').click()
		except:
			pass
		
		catLinks = []
		categories = driver.find_elements_by_class_name('subcat_item')
		for category in categories:
			catLinks.append(category.get_attribute('href'))
			
		for cat in catLinks:
			self.navigate_link(cat)
			pages = driver.find_element_by_class_name('pagination-clean').find_elements_by_tag_name('li')
			for pageNumber in range(1,len(pages)-1):
				pages = driver.find_element_by_class_name('pagination-clean').find_elements_by_tag_name('li')
				pages[pageNumber].click()
				events = driver.find_elements_by_class_name('searchResultEventName')[1:]
				for event in events:
					eventLink = event.get_attribute('href')
					musicEvents.append(eventLink)
		
		for event in musicEvents:
			self.navigate_link(event)
			eventTitle = driver.find_element_by_id('eventnameh1').text
			eventCategory = "Müzik"
			eventImage = driver.find_element_by_class_name('eventimage').find_element_by_tag_name('link').get_attribute('content')
			
			
			
			
			
			
			