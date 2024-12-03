import json

# load the following file
with open('following.json', 'r') as file:
    data = json.load(file)["relationships_following"]
following_set = set()
for user in data:
    following_set.add(user["string_list_data"][0]['value'])

# load the followers file
with open('followers_1.json', 'r') as file:
    data = json.load(file)
followers_set = set()
for user in data:
    followers_set.add(user["string_list_data"][0]['value'])

# Compare the difference of the two files
res = []
for i, user in enumerate(following_set.difference(followers_set)):
    res.append((i, user))
print(res)