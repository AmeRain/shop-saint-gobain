import platform

import os

if 'Linux'.__eq__(platform.system()):
    chrome_driver = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'drivers', 'chromedriver')
else:
    chrome_driver = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'drivers', 'chromedriver.exe')

url_multicomfort = 'https://shop.saint-gobain.ru/multicomfort'