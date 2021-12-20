import requests
from bs4 import BeautifulSoup
import csv

print('--- WEB SCRAPING FIND BUYER ---')
print('-- FROM WEB GO4WORLDBUSINESS --')
print('------- by Asep Sopiyan -------')
keywords = input("\nInput Keyword : ")
rangepage = input('Input Range Page : ')

print('\n--------- RESULT DATA ---------')

keywords = keywords.replace(' ','+')
rangepage = int(rangepage)

datas = []
for page in range(1,rangepage+1):
      url = f'https://www.go4worldbusiness.com/find?searchText={keywords}&pg_buyers={page}&pg_suppliers=1&_format=html&BuyersOrSuppliers=buyers'
      content = requests.get(url)

      if content.status_code != 200:
            print('!! ERROR STATUS CODE NOT : 200 !!')
      else:
            None

      soup = BeautifulSoup(content.text, 'html.parser')
      for result in soup.find_all('div', 'col-xs-12 nopadding search-results'):
            dbuyer = result.find('span', 'pull-left subtitle text-capitalize').text
            buyer = dbuyer.split()
            buyer = buyer[2:]
            buyer = ''.join(buyer)

            ddate = result.find('div', 'col-xs-3 col-sm-2 xs-padd-lr-2 nopadding').text
            date = ddate.strip()

            try:
                  dcommodities = result.find('h2', 'text-capitalize entity-row-title h2-item-title').text
                  dcommodities = dcommodities.split()
                  commodities = dcommodities[2:]
                  commodities = ' '.join(commodities)

            except AttributeError:
                  continue

            datas.append([date, buyer, commodities])

            print('Date :', date, '|', 'Country :', buyer, '|', 'Commodities :', commodities)



field = ['Date', 'Country', 'Commodities']
writer = csv.writer(open('results/{}_{}.csv'.format(keywords,rangepage),'w',newline=''))
writer.writerow(field)
for d in datas: writer.writerow(d)
