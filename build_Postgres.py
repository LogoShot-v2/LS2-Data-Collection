#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

volumes = ['0M0','000','001','002','003','004','005','006','007','008','009','010',
           '015','018','020','023','029','030','031','034','038']
volumes.extend([format(i, '03d') for i in range (40, 111)])
volumes.reverse()


# # Dump Non- (goods, applicant, agent) columns and (goods, applicant, agent) respectively.

# In[11]:


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String

conn_string = ''    # postgresql://...

db = create_engine(conn_string)
conn = db.connect()
print("-- Connection established --")


# In[ ]:


for vol in volumes:
    df = pd.read_csv(f'CSV/{vol}.csv')
    
    base = []
    goods = []    # 'appl-no' as primary key
    applicants = []
    agents = []
    for i in range(len(df.columns)):
        if 'goods'in df.columns[i]:
            goods.append(df.columns[i])
        elif 'applicant' in df.columns[i]:
            applicants.append(df.columns[i])
        elif 'agent' in df.columns[i]:
            agents.append(df.columns[i])
        else:
            base.append(df.columns[i])
    # Split list into sub-lists (single units)
    goods = [goods[x:x+3] for x in range(0, len(goods), 3)]
    applicants = [applicants[x:x+6] for x in range(0, len(applicants), 6)]
    agents = [agents[x:x+2] for x in range(0, len(agents), 2)]
    
    df[base].to_sql('Base', con=conn, if_exists="append", index=False, dtype={'appl-no': String(length=9)})
    for i in range(len(goods)):
        cols = ['appl-no'] + goods[i]
        df_sub = df[cols]
        df_sub.columns = ['appl-no', 'goodsclass-code', 'goods-name', 'goods-group']
        df_sub.to_sql('Goods', con=conn, if_exists="append", index=False, dtype={'appl-no': String(length=9)})
    for i in range(len(applicants)):
        cols = ['appl-no'] + applicants[i]
        df_sub = df[cols]
        df_sub.columns = ['appl-no', 'chinese-name', 'english-name', 'japanese-name', 'address', 'country-code', 'chinese-country-name']
        df_sub.to_sql('Applicants', con=conn, if_exists="append", index=False, dtype={'appl-no': String(length=9)})
    for i in range(len(agents)):
        cols = ['appl-no'] + agents[i]
        df_sub = df[cols]
        df_sub.columns = ['appl-no', 'chinese-name', 'address']
        df_sub.to_sql('Agents', con=conn, if_exists="append", index=False, dtype={'appl-no': String(length=9)})
    print(f'-- {vol}: CSV to PosgreSQL completed --')


# ### The following code is for display in Python Notebook.

# In[ ]:


# import psycopg2

# conn = psycopg2.connect(conn_string)
# conn.autocommit = True
# cursor = conn.cursor()

# sql = "SELECT * FROM \"TmarkAppl\";"
# cursor.execute(sql)
# for i in cursor.fetchall():
#     print(i)

# conn.commit()
# conn.close()

