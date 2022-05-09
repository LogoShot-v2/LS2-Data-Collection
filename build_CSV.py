#!/usr/bin/env python
# coding: utf-8

# # Recap
# 
# - Data retrieved from the server is in XML format.
# - CSV files are more friendly for downstream tasks.

# In[1]:


import pandas as pd
import xml.etree.ElementTree as ET
import urllib.request

cols = ['appl-no', 'appl-date', 'tmark-name',
        'tmark-class', 'tmark-class-desc',
        'tmark-image-url',
        'tmark-type', 'tmark-type-desc',
        'tmark-color', 'tmark-color-desc',
        'tmark-draft-c', 'tmark-draft-e', 'tmark-draft-j',
        'tmark-sign', 'word-description', 'receive-date',
        'goodsclasses', 'parties']

volumes = ['0M0','000','001','002','003','004','005','006','007','008','009','010',
           '015','018','020','023','029','030','031','034','038']
volumes.extend([format(i, '03d') for i in range (40, 111)])

print(volumes)


# In[2]:


# # Create sub-directories.
# import os

# for i in volumes:
#     os.makedirs(f'pics/{i}')


# In[3]:


# Image retrieval module
def fetch_image(src, filename):
    """Download image from the provided source URL."""
    urllib.request.urlretrieve(src, f"pics/{filename}")


# In[ ]:


for vol in volumes:
    data = []
    if vol=='030':
        indices = [format(i, '05d') for i in range (99999)]
    else:
        indices = [format(i, '06d') for i in range (999999)]
    
    for index in indices:
        try:
            file = f's220ftp.tipo.gov.tw/TmarkAppl/{vol}/TmarkAppl_{vol}{index}.xml'
            tree = ET.parse(file)    # revise: direct access with ftp address
        except:
            continue

        root = tree.getroot()       # get root element
        item = {}
        appl_no = 0

        for i in root:
            for col in cols:
                if col=='tmark-image-url':
                    for k in range(1, 7):
                        cname = col + '_' + str(k)
                        url_tipo = i.find(f'{col}/image-data-{str(k)}').text
                        if (url_tipo):
                            fname = f'{vol}/{appl_no}_{str(k)}.jpg'
                            try:
                                fetch_image(url_tipo, fname)    # download image from tipo server
                                item[cname] = fname
                            except:
                                print(f'!! {vol}-{index}: Request failed. !!')
                                continue
                elif col=='goodsclasses':
                    for element in i.find(f'{col}'):
                        num = element.attrib['sequence']
                        cname = f'goodsclass-code_{str(num)}'
                        item[cname] = i.find(f'{col}/goodsclass/goodsclass-code').text
                        cname = f'goods-name_{str(num)}'
                        item[cname] = i.find(f'{col}/goodsclass/goods-name').text
                        cname = f'goods-group_{str(num)}'
                        item[cname] = i.find(f'{col}/goodsclass/goods-group').text
                elif col=='parties':
                    for element in i.find(f'{col}/applicants'):
                        num = element.attrib['sequence']
                        cname = f'applicant{str(num)}_chinese-name'
                        item[cname] = i.find(f'{col}/applicants/applicant/chinese-name').text
                        cname = f'applicant{str(num)}_english-name'
                        item[cname] = i.find(f'{col}/applicants/applicant/english-name').text
                        cname = f'applicant{str(num)}_japanese-name'
                        item[cname] = i.find(f'{col}/applicants/applicant/japanese-name').text
                        cname = f'applicant{str(num)}_address'
                        item[cname] = i.find(f'{col}/applicants/applicant/address').text
                        cname = f'applicant{str(num)}_country-code'
                        item[cname] = i.find(f'{col}/applicants/applicant/country-code').text
                        cname = f'applicant{str(num)}_chinese-country-name'
                        item[cname] = i.find(f'{col}/applicants/applicant/chinese-country-name').text
                    for element in i.find(f'{col}/agents'):
                        num = element.attrib['sequence']
                        cname = f'agent{str(num)}_chinese-name'
                        item[cname] = i.find(f'{col}/agents/agent/chinese-name').text
                        cname = f'agent{str(num)}_address'
                        item[cname] = i.find(f'{col}/agents/agent/address').text
                else:
                    item[col] = i.find(col).text
                    if col=='appl-no':
                        appl_no = item[col]
        data.append(item)
    
    df_data = pd.DataFrame.from_records(data, index='appl-no')
    df_data.to_csv(f'CSV/{vol}.csv')
    print(f'-- {vol}: XML to CSV conversion completed, dimensions: {df_data.shape} --')


# In[ ]:


# for key, value in item.items():
#     print(key, ':', value)

