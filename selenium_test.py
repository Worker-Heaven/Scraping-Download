from selenium import webdriver
import lxml.html

site_url = 'https://oasm.dfsa.dk/uk/searchresult.aspx?t=shortselling'
chromedriver_path = "E:/Utilities/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.implicitly_wait(30)

driver.get(site_url)

page = lxml.html.fromstring(driver.page_source)

urls = page.xpath('//div[@class="headlink"]/a/text()')

print(urls)