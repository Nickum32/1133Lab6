scoreDict = {}
names = ['joe', 'tim', 'barb', 'sue', 'sally']
scores = [10,23,13,18,12]
def makeDictionary(name, score):
    for i in range(5):
        scoreDict[name[i]] = score[i]

makeDictionary(names, scores)

def getScore(name, d):
    try:
        return d[name]
    except KeyError:
        print('Error, name not found.')
        return -1
    
