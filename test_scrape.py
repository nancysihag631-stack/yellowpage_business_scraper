import requests
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
import random

ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
}

url = 'https://www.yellowpages.com/los-angeles/restaurants?page=1'
print(f'Testing: {url}')

resp = requests.get(url, headers=headers, timeout=20)
print(f'Status: {resp.status_code if resp else "No resp"}')

if resp and resp.status_code == 200:
    soup = BeautifulSoup(resp.content, 'html.parser')
    print('\\n=== PAGE TITLE ===')
    print(soup.title.text if soup.title else 'No title')
    
    print('\\n=== FOUND CONTAINERS ===')
    selectors = [
        '[data-impressionid]',
        '[data-analytics*="result"]',
        'div[class*="result"]',
        'div[class*="listing"]',
        'div[class*="business"]',
        '.info',
        '.search-result',
        'div > a[href*="/"]',
        '.nrt-rcont',
        '[role="article"]',
    ]
    all_containers = []
    for sel in selectors:
        cons = soup.select(sel)
        count = len(cons)
        print(f'{sel}: {count}')
        if count:
            all_containers.extend(cons[:5])
    
    print(f'\\nTotal containers: {len(all_containers)}')
    
    if all_containers:
        cont = all_containers[0]
        print('\\n=== SAMPLE CONTAINER HTML ===')
        print(cont.prettify()[:1000])
        
        # Test name extraction
        name_sel = ['a[title]', '.business-name', '.name', 'h1 a', 'h2 a', 'a strong']
        name = ''
        for s in name_sel:
            e = cont.select_one(s)
            if e:
                name = e.get_text(strip=True)
                print(f'Name from {s}: {name}')
                break
        print(f'Final name: {name or "None"}')
else:
    print('\\nHTML snippet:', resp.text[:2000] if resp else 'No response')
