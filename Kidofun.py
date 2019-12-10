from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json


class Kidofun:
    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            options=chromeOptions, executable_path=r"C:\\Users\\beroz\\Pictures\\chromedriver.exe")
        self.get_page_count()
        self.months = {'Ara': 12, 'Oca': 1, 'Şub': 2, 'Mar': 3, 'Nis': 4,
                       'May': 5, 'Haz': 6, 'Tem': 7, 'Ağu': 8, 'Eyl': 9, 'Eki': 10, 'Kas': 11}

    def navigate_link(self, link):
        self.driver.get(link)

    def get_page_count(self):
        driver = self.driver
        self.navigate_link("https://kido-fun.com/cocuk-etkinlikleri")
        pagination = driver.find_element_by_class_name("page-pagination")
        pages = pagination.find_elements_by_tag_name('li')
        self.page_count = len(pages)

    def get_event_links(self):
        driver = self.driver
        eventLinks = []
        for page in range(1, self.page_count+1):
            self.navigate_link(
                "https://kido-fun.com/cocuk-etkinlikleri?p={}".format(page))
            eventBlock = driver.find_element_by_class_name("events-list")
            events = eventBlock.find_elements_by_tag_name('li')
            for event in events:
                eventLink = event.find_element_by_tag_name(
                    'a').get_attribute('href')
                eventLinks.append(eventLink)

        return eventLinks

    def get_attributes_of_event(self):
        driver = self.driver
        eventLinks = self.get_event_links()
        events = []
        for link in eventLinks:
            try:
                self.navigate_link(link)
                # Get Classes
                ImageClass = driver.find_element_by_class_name('event--image')
                DateClass = driver.find_element_by_class_name('event--date')
                DetailClass = driver.find_element_by_class_name(
                    'event--detail')
                PropsClass = DetailClass.find_element_by_class_name(
                    'event--prop').find_elements_by_tag_name('span')
                LocationClass = driver.find_element_by_class_name('col-md-4')

                # Get Values
                eventImage = ImageClass.find_element_by_tag_name(
                    'img').get_attribute('src')
                eventTitle = DetailClass.find_element_by_css_selector(
                    'h1 > a').get_attribute('title')
                eventCategory = PropsClass[0].text
                eventPrice = PropsClass[1].text
                eventAge = PropsClass[2].text
                try:
                    DetailClass.find_element_by_class_name(
                        'morelink').send_keys(Keys.RETURN)
                    eventDescription = DetailClass.find_element_by_css_selector(
                        '.event--caption .more').text[:-17]
                except:
                    eventDescription = DetailClass.find_element_by_css_selector(
                        '.event--caption .more').text
                eventLink = DetailClass.find_element_by_class_name(
                    'event--process').find_elements_by_tag_name('a')[1].get_attribute('href')
                eventMonth = DateClass.find_element_by_class_name(
                    'date-month').text
                eventDay = DateClass.find_element_by_class_name(
                    'date-number').text
                eventTime = DateClass.find_element_by_class_name(
                    'date-time').text
                eventDate = datetime(2019, self.months[eventMonth], int(
                    eventDay), int(eventTime[0:2], int(eventTime[3:5])))
                eventPlace = LocationClass.find_element_by_class_name(
                    'venue-name').text
                try:
                    eventLocation = LocationClass.find_element_by_xpath(
                        '/html/body/main/section[2]/div/div/div[2]/section/div[2]/ul/li[3]').text
                except:
                    pass
                eventLatitude = driver.find_element_by_id(
                    'lat').get_attribute('value')
                eventLongitude = driver.find_element_by_id(
                    'lng').get_attribute('value')

                event = {
                    "name": eventTitle,
                    "category": eventCategory,
                    "description": eventDescription,
                    "image": eventImage,
                    "age": eventAge,
                    "link": eventLink,
                    "price": eventPrice,
                    "date": str(eventDate),
                    "kidoLink": link,
                    "place": eventPlace,
                    "location": eventLocation,
                    "latitude": eventLatitude,
                    "longitude": eventLongitude
                }
                events.append(event)
            except:
                pass
        with open('data.txt', 'w') as outfile:
            json.dump(events, outfile)


a = Kidofun()
print(a.get_attributes_of_event())
