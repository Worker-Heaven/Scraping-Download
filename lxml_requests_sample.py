import requests
from lxml import html

def scrape_dk_page(link):
  # link = 'https://oasm.dfsa.dk/uk/showannouncement.aspx?aid=479c06ac-6861-44b5-b116-786827255a71'

  response = requests.get(link) #get page data from server, block redirects
  sourceCode = response.text #get string of source code from response
  htmlElem = html.fromstring(sourceCode) #make HTML element object

  scraped_data = {}

  valid_labels = [
    'ID',
    'Position date',
    'Type',
    'Date of previous notification',
    'Previous message',
    'Made public',
    'Registration',
    'Company',
    'CVR-no',
    'ISIN',
    'Shortseller',
  ]

  for valid_label in valid_labels:
    label = htmlElem.xpath('//div[@class="group"]//div[@class="label" and contains(text(), "%s")]/text()' % valid_label)
    data = htmlElem.xpath('//div[@class="group"]//div[@class="label" and contains(text(), "%s")]/following-sibling::div[1]/text()' % valid_label)
    if len(label) > 0 and len(data) > 0:
      scraped_data[valid_label] = data[0]
    else:
      scraped_data[valid_label] = '-'

  # print (scraped_data)
  return scraped_data