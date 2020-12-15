import json
import numpy as np
import pandas as pd
from collections import Counter

filename = 'new_data.json'
with open(filename,mode="r") as f:
    try: 
        data = json.load(f) 
    except:
        data = []

print("data size : %d" % len(data))

voteNums = []
commentNums = []
createTimes = []
titles = []
for issue in data :
    title,createTime,state,number,commentNum,voteNum = issue.values()
    createTimes.append(createTime)
    voteNums.append(voteNum)
    commentNums.append(commentNum)
    titles.append(title)
issues = {'createTime':createTimes,
          'voteNum':voteNums,
          'commentNum':commentNums,
          'title':titles,
          'level':None}

df = pd.DataFrame(issues)
df['createTime'] = pd.to_datetime(df['createTime']).dt.date
df['createTime'] = (df['createTime'][0] - df['createTime']).astype('timedelta64[D]') 

df1 = df[df['createTime']<=463]
df2 = df[(df['createTime']>463) & (df['createTime']<=463*2)]
df3 = df[(df['createTime']>463*2) & (df['createTime']<=463*3)]
df4 = df[df['createTime']>463*3]

index = df4[df4['voteNum']<=5].index
df4['level'][df4['voteNum']<=5] = 'Lowest'
df4['level'][df4['voteNum']>=6] = 'Low'
df4['level'][df4['voteNum']>=10] = 'Medium'
df4['level'][df4['voteNum']>=20] = 'High'
df4['level'][df4['voteNum']>=60] = 'Highest'

index = df3[df3['voteNum']<=4].index
df3['level'][df3['voteNum']<=4] = 'Lowest'
df3['level'][df3['voteNum']>=5] = 'Low'
df3['level'][df3['voteNum']>=7] = 'Medium'
df3['level'][df3['voteNum']>=13] = 'High'
df3['level'][df3['voteNum']>=31] = 'Highest'

index = df2[df2['voteNum']<=3].index
df2['level'][df2['voteNum']<=3] = 'Lowest'
df2['level'][df2['voteNum']>=4] = 'Low'
df2['level'][df2['voteNum']>=5] = 'Medium'
df2['level'][df2['voteNum']>=8] = 'High'
df2['level'][df2['voteNum']>=17] = 'Highest'

index = df2[df2['voteNum']<=4].index
df1['level'][df1['voteNum']<=4] = 'Lowest'
df1['level'][df1['voteNum']>=5] = 'Low'
df1['level'][df1['voteNum']>=6] = 'Medium'
df1['level'][df1['voteNum']>=10] = 'High'
df1['level'][df1['voteNum']>=21] = 'Highest'

requestLevel = []
requestLevel += df1['level'].values.tolist()
requestLevel += df2['level'].values.tolist()
requestLevel += df3['level'].values.tolist()
requestLevel += df4['level'].values.tolist()
df['level'] = requestLevel

df.drop(['commentNum','createTime','voteNum'],axis=1,inplace=True)
df.to_csv('./dataWithLevel.csv',index=False,columns=['title','level'])