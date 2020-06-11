def dispRes(pFriendlies,pEnemies):
    print("---" * 10)
    result = "Friendlies - "
    for x in pFriendlies:
        result += str(x.hp) + " - "
    print(result + "\n")
    result = "Enemies - "
    for x in pEnemies:
        result += str(x.hp) + " - "
    print(result)
    print("---" * 10)