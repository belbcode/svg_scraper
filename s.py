import urllib.request
from bs4 import BeautifulSoup
contents = urllib.request.urlopen("https://www.youtube.com").read()
soup = BeautifulSoup(contents, 'lxml')
# soup= soup.prettify()

print(soup.find_all('svg'))
# content = ""
# array_of_svgs = []
# readContent = False

# for x in range(0, len(soup)):
#     if(soup[x:x+4]== /refex/):
#         i = x + 4
#         if(soup[i]!='>'):
#             i += 1
#             continue
#         readContent = True
#     if(soup[x:x+6]=='</div>'):
#         readContent = False
#         array_of_svgs.append(content)
#         content = ""
#     if(readContent):
#         content += soup[x]
# print(array_of_svgs)