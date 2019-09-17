#!/usr/bin/env python
# coding: utf-8

# In[31]:


from urllib.request import urlopen, urljoin
import re


# In[32]:


def download_page(url):
    return urlopen(url).read().decode('utf-8')


# In[33]:


def extract_links(page):
    
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return link_regex.findall(page)


# In[34]:


if __name__== '__main__':
    
    target_url = 'https://www.apress.com/'
    
    apress = download_page(target_url)
    links = extract_links(apress)
    
    for link in links:
        print(urljoin(target_url, link))


# In[ ]:




