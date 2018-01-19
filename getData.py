import requests
from lxml import html

url = 'https://www.investing.com/commodities/gold-historical-data'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
#print(page.content)
tree = html.fromstring(page.content)

#print page.text
#/div[@title="buyer-name"]/text()
goldDate=tree.xpath('//*[@id="curr_table"]/tbody/tr[3]/td[1]')
#goldDate=tree.xpath('//*[@id="curr_table"]/tbody/tr[3]/td[1]')
goldPrice=tree.xpath('//*[@id="curr_table"]/tbody/tr[1]')
#//*[@id="curr_table"]/tbody/tr[1]/td[3]
#goldPrice=tree.xpath('//*[@id="curr_table"]/tbody/tr[1]/td[2]')
sample = tree.xpath('//*[@id="curr_table"]/tbody/text()')


#print goldDate[0].text
#print goldPrice[0].text
#print sample

#import lxml.etree

#doc = lxml.etree.parse('test.xml')

# We need to locate the <tr> objects somehow... I'm assuming
# there is a single <table><tbody>.. container and no other
# span/div tags in the way.
filename = "goldfile.csv"
goldfile = open(filename, "w")
#gold_dict = {'one': 1, 'two': 2}

for tr in tree.xpath('//*[@id="curr_table"]/tbody/tr'):
    goldDate = tr.xpath('td[1]/text()')
    goldPrice = tr.xpath('td[2]/text()')
    print('date: '+ goldDate[0], 'price: '+ goldPrice[0])
    #print('date: ', goldDate, 'price: ', goldPrice)
    #goldfile.write("Date: %s , price: %s\n" % (goldDate[0], goldPrice[0]))
    goldfile.write('%s:%s\n' % (goldDate[0], goldPrice[0]))

goldfile.close()
    
url = 'https://www.investing.com/commodities/silver-historical-data'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
#print(page.content)
tree = html.fromstring(page.content)

filename = "silverfile.csv"
silverfile = open(filename, "w")

for tr in tree.xpath('//*[@id="curr_table"]/tbody/tr'):
    goldDate = tr.xpath('td[1]/text()')
    goldPrice = tr.xpath('td[2]/text()')
    print('date: '+ goldDate[0], 'price: '+ goldPrice[0])
    #print('date: ', goldDate, 'price: ', goldPrice)
    #goldfile.write("Date: %s , price: %s\n" % (goldDate[0], goldPrice[0]))
    silverfile.write('%s:%s\n' % (goldDate[0], goldPrice[0]))

silverfile.close()
    
