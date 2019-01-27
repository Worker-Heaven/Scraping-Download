import requests
from lxml import html

# link = "https://oasm.dfsa.dk/uk/searchresult.aspx?t=shortselling"
link = 'https://oasm.dfsa.dk/uk/showannouncement.aspx?aid=479c06ac-6861-44b5-b116-786827255a71'

response = requests.get(link) #get page data from server, block redirects
sourceCode = response.text #get string of source code from response
htmlElem = html.fromstring(sourceCode) #make HTML element object


urls = htmlElem.xpath('//div[@class="label"]/text()')

print(urls)
