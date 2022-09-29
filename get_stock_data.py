#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:27:25 2022

@author: bokie
"""

from cmschina_tianyan.session import CmsSession

dataset = CmsSession.init(appId="cb632213cf764a019b32f8cc9d2040b7", 
  appSecret="b23700b9fbf0090709c7b72ac0fdcb390cd19cc663bcf1c7a07c12b8c32bf377")

        
#%%
stock_code = '603355' #上交所

#上交所取数
sql = f''' 
SELECT * 
FROM quota_01.sh_stock_snapshot
where security_id = '{stock_code}' and date_time > 20220927000000 and date_time < 20220928000000
'''

df_sh = dataset.get_data(sql)

df_sh        

#%%

stock_code = '002044' #深交所
stock_code = '300760' #深交所
stock_code = '002145' #深交所

#深交所取数
sql = f''' 
SELECT * 
from quota_01.snap_level_spot 
where security_id = '{stock_code}' AND trade_date = '20220927'
'''
df_sz = dataset.get_data(sql)

df_sz