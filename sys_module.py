# import sys
# from pathlib import Path

# # readme_file=Path('README.md')
# # with open(readme_file,'r')as rm:
# #     rm.readlines()


# sys.path

# for i in sys.path :
#     print(i)

# print(f'SYS ARGV- Giving python file path- {sys.argv}')

# print(f'Length of sys.argv ={len(sys.argv)}')
# if len(sys.argv)>=2:
#     file=sys.argv[-1]
#     with open (file) as f:
#         file=f.readlines(500)

# else :
#     file ='File not found, Give file name correctly'

# print(file)


# print(f'SYS ARGV- Giving python file path- {sys.argv}')

# print(f'Length of sys.argv ={len(sys.argv)}')
# if len(sys.argv)>=2:
#     file=sys.argv[-1]
#     with open (file) as f:
#         file=f.readlines(500)
#     sys.exit()
# else :
#     file ='File not found, Give file name correctly'

# print(file)

# # Display Hook


# print(sys.platform)
# print(sys.version)

# 

l=[1,2,3,4,5,6,7,8,9]
k=[1,2,3,4,5,6,7,8,0]

for i in range(0,len(l)-1,2):
    k[i],k[i+1]=k[i+1],k[i]
print(k)

a=l.copy()
i=0
while i+1 < len(a):
    a[i],a[i+1]=a[i+1],a[i]
    i+=2
print(a)

from sqlalchemy import create_engine

engine=create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/madrid")
import pandas as pd
df=pd.read_sql("select * from age_group_distribution",engine)
# print(df.head())

import sys
print(sys.executable)