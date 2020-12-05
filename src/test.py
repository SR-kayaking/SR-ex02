import json
filename = 'data.json'
with open(filename,mode="r") as f:
    try: 
        prev_data = json.load(f) 
    except:
        prev_data = []
l = len(prev_data)
print(l)