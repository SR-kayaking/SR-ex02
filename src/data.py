import json
filename = 'data.json'
with open(filename,mode="r") as f:
    try: 
        data = json.load(f) 
    except:
        data = []

print("data size : %d" % len(data))

issues = []
for issue in data :
    title, reactions = issue.values()
    positive_count = 0
    for reaction in reactions:
        if reaction in ['+1','laugh','heart','hooray']:
            positive_count += 1
    issues.append([positive_count,title])
   
issues.sort(key=lambda issue:issue[0],reverse = True)
maxValue = issues[0][0]
minValue = issues[-1][0]
highest_high = (maxValue-minValue)*0.8
high_mid = (maxValue-minValue)*0.6
mid_low = (maxValue-minValue)*0.4
low_lowest = (maxValue-minValue)*0.2

for i in issues:
    if i[0]>=highest_high:
        i.append('Highest')
    elif i[0]>=high_mid:
        i.append('High')
    elif i[0]>=mid_low:
        i.append('Medium')
    elif i[0]>=low_lowest:
        i.append('Low')
    else:
        i.append('Lowest')
        
f = open("data.txt",mode='w',encoding='utf8')
for i in issues:
    f.write("{} {} {}\n".format(i[0],i[2],i[1]))
f.close()