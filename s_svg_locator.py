import urllib.request
from bs4 import BeautifulSoup

import sys

def pull_svg(source):
    print(source)
    contents = urllib.request.urlopen(source).read()
    soup = BeautifulSoup(contents, 'lxml')
    set_of_svgs = (soup.find_all('svg'))
    return set_of_svgs

sys.modules[__name__] = pull_svg