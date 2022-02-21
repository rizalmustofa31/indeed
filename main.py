import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
site = 'https://www.indeed.com/'
params = {
    'q': 'Python Developer',
    'l': 'New York State',
    'vjk': '71acc67a281f6038'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
res = requests.get(url, params=params, headers=headers)


def get_total_pages():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        'vjk': '71acc67a281f6038'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()


    total_pages = []
    #Scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())

    pagination = soup.find('ul','pagination-list')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)


    total = int(max(total_pages))
    print(total)
    return total

def get_all_items():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        'vjk': '71acc67a281f6038'
    }
    res = requests.get(url,params=params, headers=headers)

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    soup = BeautifulSoup(res.text, 'html.parser')

    #scraping prosses
    contents = soup.find_all('table','jobCard_mainContent big6_visualChanges')

    # pick item
    # * title
    # * company name
    # * company link
    # * company address

    for item in contents:
        title = item.find('h2', 'jobTitle').text
        company = item.find('span', 'companyName')
        company_name = company.text
        try:
            company_link = site + company.find('a')['href']
        except:
            company_link = 'Link is not available'

        print(company_link)


if __name__ == '__main__':
    get_all_items()