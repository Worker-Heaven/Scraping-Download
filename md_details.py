from selenium import webdriver
import lxml.html

site_url = 'https://www.investing.com/equities/verizon-communications-inc-elks'
chromedriver_path = "E:/Utilities/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.implicitly_wait(30)

driver.get(site_url)

page = lxml.html.fromstring(driver.page_source)

# page_name = page.xpath('//h1[@itemprop="name"]/text()')[0]

# exchange = page.xpath('//div[@id="DropDownContainer"]//i[contains(@class, "btnTextDropDwn")]/text()')[0]


# valid_labels = [
#   'Type',
#   'Market',
#   'ISIN',
#   'CUSIP',
# ]

# small_table_data = {}
# for valid_label in valid_labels:
#   labels = page.xpath('//div[@id="quotes_summary_current_data"]//div[@class="right"]//div/span[1][contains(text(), "%s")]/text()' % valid_label)
#   data = []
#   if valid_label != 'Market':
#     data = page.xpath('//div[@id="quotes_summary_current_data"]//div[@class="right"]//div/span[1][contains(text(), "%s")]/following-sibling::span[1]/text()' % valid_label)
#   else:
#     data = page.xpath('//div[@id="quotes_summary_current_data"]//div[@class="right"]//div/span[1][contains(text(), "%s")]/following-sibling::span[1]/@title' % valid_label)

#   if len(labels) > 0 and len(data) > 0:
#     small_table_data[valid_label] = data[0]
#   else:
#     small_table_data[valid_label] = '-'

industry = page.xpath('//div[@class="companyProfileHeader"]/div[contains(text(), "Industry")]/a/text()')[0]

sector = page.xpath('//div[@class="companyProfileHeader"]/div[contains(text(), "Sector")]/a/text()')[0]

# print(page_name)
# print (exchange)
# print (small_table_data)

print (industry, sector)
