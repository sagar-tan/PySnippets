def score_diff(g1, g2):
    result={} #newDict
    for key in p1:
        result[key] = p1[key]-p2[key]
    return result
game1 = {"Alice": 100, "Bob": 95} 
game2 = {"Alice": 90, "Bob": 85} 
print(score_diff(game1, game2))
