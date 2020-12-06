import json
filename = 'data.json'
with open(filename,mode="r") as f:
    try: 
        data = json.load(f) 
    except:
        data = []

print("data size : %d" % len(data))

f = open("train_data.txt",mode='w',encoding='utf8')
issues = []
for issue in data :
    title, reactions = issue.values()
    positive_count = 0
    for reaction in reactions:
        if reaction in ['+1','laugh','heart','hooray']:
            positive_count += 1
    f.write("{} {}\n".format(title,positive_count))
    issues.append((title,positive_count))
f.close()


issues.sort(key=lambda issue:issue[1],reverse = True)
for issue in issues[:50]:
    print(issue)