"""乐队评价推荐 """
"""user = {
        "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}"""
#用户评分
users ={
    "Angelica":{"Blue Travel":3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes":2.5, "Vampire Weekend": 2.0},
    "Bill":{"Broken Bells": 4.0,"Broken Bells": 3.5, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 3.0},
    "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
    "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
    "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
    "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
    "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
    "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}
#print(user["Veronica"])
#计算曼哈顿距离
def manhattan(rating1,rating2):
    """rating1和rating2参数中存储的数据格式均为
    {"Blues Traveler": 3.0, "Norah Jones": 5.0}"""
    distance = 0
    for key in rating1:
        if key in rating2:
            distance +=abs(rating1[key]-rating2[key])
    return distance
#print(user["Angelica"],user["Bill"])
"""print(manhattan(users["Hailey"],users["Veronica"]))
print(manhattan(users["Hailey"],users["Jordyn"]))"""
#计算所有用户至username用户的距离，并按序排列
def compiuterNearestNeighbor(username,users):
    distances = []
    for user in users:
        if user != username:
            distance =manhattan(users[user],users[username])
            distances.append((distance,user))

    distances.sort()
    return distances

#print(compiuterNearestNeighbor("Hailey",users))
"""结果：[(2.0, 'Veronica'), (2.5, 'Bill'), (4.0, 'Chan'), (4.0, 'Sam'), (4.5, 'Dan'), (5.0, 'Angelica'), (7.5, 'Jordyn')]"""
def recommend(username,users):
    """返回推荐列表"""
    #找到距离最近的一个人
    nearest = compiuterNearestNeighbor(username,users)[0][1]
    recomendation=[]
    #找到那个人的评价过，但username用户未评价的乐队
    neighborRating = users[nearest]
    userRating = users[username]
    for artist in neighborRating:
        if not artist in userRating:
            recomendation.append((artist,neighborRating[artist]))
    return sorted(recomendation,key=lambda artistTuple: artistTuple[1], reverse = True)

#print(recommend("Hailey",users))
def minkowski(rating1,rating2):
    r=0
    for rating1 in users:
        for rating2 in users:
            if rating1!=rating2:
                for key1 in rating1:
                    if key1 in rating2:
                        r=r+1
    for key11 in rating1:
        if key11 in rating2:
            juli +=pow((rating1[key11]-rating2[key11]),r)
    return pow(juli,1.0/r)
print(minkowski(users["Angelica"],users["Bill"]))
