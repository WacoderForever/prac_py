users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Add list of friends to each user
for user in users:
    user["friends"] = []

for i,j in friendships:
    user[i]["friends"].append(user[j])
    user[j]["friends"].append(user[i])

# Total number of connections
def get_no_of_friends_for_user(user):
    return len(user["friends"])

total_connections = sum(get_no_of_friends_for_user(user) for user in users)
# average connections per user
from __future__ import division
num_users = len(users)
avg_connection = total_connections / num_users

num_friends_by_id = [(user["id"],get_no_of_friends_for_user(user))
                     for user in users]
sorted(num_friends_by_id,
       key = lambda (user_id,num_friends): num_friends,
       reverse=True)
# Friends of friends suggester
def friends_of_friends_id_bad(user):
    return [foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]]

from collections import Counter

def not_the_same(user,other_user):
    return user["id"] != other_user["id"]
def not_friends(user,other_user):
    return all(not_the_same(friend,other_user)
                for friend in user["friends"])
