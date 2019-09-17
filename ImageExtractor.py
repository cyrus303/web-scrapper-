#!/usr/bin/env python
# coding: utf-8

# In[4]:


from urllib.request import urlopen, urljoin
import re

def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_links(page):
    
    link_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE)
    return link_regex.findall(page)

if __name__== '__main__':
    
    target_url = 'https://www.apress.com/'
    
    apress = download_page(target_url)
    links = extract_links(apress)
    
    for link in links:
        print( urljoin(target_url,link))


# In[ ]:




