from linkFeeder import links
from downlodeyt import downlode
import time

for item in links():
    downlode(item)
    time.sleep(2)