from linkFeeder import file_to_list
from downlodeyt import downlode
import time
file = 'links.txt'


for item in file_to_list(file):
    downlode(item)
    time.sleep(2)