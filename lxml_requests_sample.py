import requests
from lxml import html

link = "https://oasm.dfsa.dk/uk/searchresult.aspx?t=shortselling"
response = requests.get(link) #get page data from server, block redirects
sourceCode = response.text #get string of source code from response
htmlElem = html.fromstring(sourceCode) #make HTML element object


urls = htmlElem.xpath('//div[@class="login"]/a/text()')
resultNumber = htmlElem.xpath("//h1/text()")

print(resultNumber)
