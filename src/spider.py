from github import Github, RateLimitExceededException
import time
import json

def save_in_file(filename,data):
    with open(filename,mode="r") as f:
        try: 
            prev_data = json.load(f) 
        except:
            prev_data = []
        data = prev_data + data
      
    with open(filename,mode="w") as f:
        f.write(json.dumps(data))
        
def get_stored_data_length(filename):
    l = 0
    with open(filename,mode='r') as f :
        try:
            prev_data = json.load(f)
        except:
            prev_data = []
        l = len(prev_data)
        prev_data.clear()
    return l

def count_upvote(reactions):
    count = 0
    for r in reactions :
        if r == '+1' :
            count += 1
    return count 

    
g = Github("1e0ed5dc9fdccd2faa1c055510baf0c9b294f790") # empty param here : github access token 
repo = g.get_repo("microsoft/vscode")
issues = repo.get_issues(labels = ["feature-request"], state = "all")
data = []
filename = 'new_data.json'
ts = time.time()

start_pos = get_stored_data_length(filename)
count = start_pos 
print("start from %d" % start_pos)
for issue in issues[start_pos:]:
    count += 1
    try:
        data.append({
            "title": issue.title,
            "createdAt": issue.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "state": issue.state,
            "number": issue.number,
            "commentNum": issue.comments,
            "voteNum": count_upvote([reaction.content for reaction in issue.get_reactions()])
        })
    except RateLimitExceededException as RE:
        save_in_file(filename,data)
        data.clear()
        print("up to rate limit , sleep for 1h")
        time.sleep(3600)
    except Exception:
        save_in_file(filename,data)
        data.clear()
        print("timeout exception, previous data has been stored, please restart the program")
        exit(0)
    te = time.time()
    print('{} issues got, time: {}'.format(count,te-ts))
    ts = te
    if count % 400 == 0:
        save_in_file(filename,data)
        data.clear()
        print("previous data has been stored")

save_in_file(filename,data)

# print(data)
print("total:{}".format(count))