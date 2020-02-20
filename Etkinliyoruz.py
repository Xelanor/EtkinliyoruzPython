from Kidofun import Kidofun
import requests
from pprint import pprint
from utils import utils

Kidofun = Kidofun()
events = Kidofun.get_attributes_of_event()

events = utils.event_place_details(events)

for event in events:
    res = requests.post("http://34.67.211.44/api/add", event)
