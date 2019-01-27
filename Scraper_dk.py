import requests
from lxml import html

class Scrape:
  api_url = 'https://oasm.dfsa.dk/Reserved/SearchSSS.aspx'
  page_count = 4

  def scrape_details(self, details_urls):
    for link in details_urls:
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

      print (scraped_data)

  def run(self):
    for page_index in range(self.page_count):
      api_params = {
        't': 'shortselling',
        'ps': 10,
        'p': page_index,
        'publication': '(pubafter:2017/2/01 and pubbefore:2019/2/01)',
      }

      response = requests.get(url=self.api_url, params=api_params)

      status = response.status_code

      if status == 200:
        parsed_json = response.json()

        result = parsed_json['ResultSet']

        details_urls = []
        for data in result:
          fields = data['Fields']

          for field in fields:
            if field['FieldName'] == 'showurlda':
              details_url = field['Value']
              details_urls.append(details_url)
            elif field['FieldName'] == 'title':
              details_title = field['Value']
              print(details_title)
          
        self.scrape_details(details_urls)

task = Scrape()
task.run()