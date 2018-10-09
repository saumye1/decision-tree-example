import math

target = 'play'
data = [{ 'outlook' : 'sunny', 'temperature' : 'hot', 'humidity' : 'high', 'windy' : 'false', 'play' : 'no'}
,{ 'outlook' : 'sunny', 'temperature' : 'hot', 'humidity' : 'high', 'windy' : 'true', 'play' : 'no'}
,{  'outlook' : 'overcast', 'temperature' : 'hot', 'humidity' : 'high', 'windy' : 'false', 'play' : 'yes'}
,{  'outlook' : 'rainy', 'temperature' : 'mild', 'humidity' : 'high', 'windy' : 'false', 'play' : 'yes'}
,{  'outlook' : 'rainy', 'temperature' : 'cool', 'humidity' : 'normal', 'windy' : 'false', 'play' : 'yes'}
,{  'outlook' : 'rainy', 'temperature' : 'cool', 'humidity' : 'normal', 'windy' : 'true', 'play' : 'no'}
,{  'outlook' : 'overcast', 'temperature' : 'cool', 'humidity' : 'normal', 'windy' : 'true', 'play' : 'yes'}
,{  'outlook' : 'sunny', 'temperature' : 'mild', 'humidity' : 'high', 'windy' : 'false', 'play' : 'no'}
,{  'outlook' : 'sunny', 'temperature' : 'cool', 'humidity' : 'normal', 'windy' : 'false', 'play' : 'yes'}
,{  'outlook' : 'rainy', 'temperature' : 'mild', 'humidity' : 'normal', 'windy' : 'false', 'play' : 'yes'}
,{  'outlook' : 'sunny', 'temperature' : 'mild', 'humidity' : 'normal', 'windy' : 'true', 'play' : 'yes'}
,{  'outlook' : 'overcast', 'temperature' : 'mild', 'humidity' : 'high', 'windy' : 'true', 'play' : 'yes'}
,{  'outlook' : 'overcast', 'temperature' : 'hot', 'humidity' : 'normal', 'windy' : 'false', 'play' : 'yes'}
,{  'outlook' : 'rainy', 'temperature' : 'mild', 'humidity' : 'high', 'windy' : 'true', 'play' : 'no'}]

def log2(x):
    return math.log10(x)/math.log10(2)

def entropy(data, target):
    '''Finds entropy of a 'target' for given 'data'.
    Entropy is uncertainity in the data or randomness
    '''
    cl = {}
    for x in data:
        if cl.has_key(x[target]):
            cl[x[target]] += 1
        else:
            cl[x[target]] = 1
    tot_cnt = sum(cl.viewvalues())
    return sum([ -1 * (float(cl[x])/tot_cnt) * log2(float(cl[x])/tot_cnt) for x in cl])


def findInformationGain(data, target, column, entropyParent):
    '''Finds Informatin Gain with 'column' w.r.t 'target'.
    Information Gain = Entropy under current node - Weighted average of all desicion paths from current node
    '''
    keys = { i[column] for i in data }
    entropies = {}
    count = {}
    avgEntropy = 0
    for val in keys:
        modData = [ x for x in data if x[column] == val]
        entropies[val] = entropy(modData, target)
        count[val] = len(modData)
        avgEntropy += (entropies[val] * count[val])

    tot_cnt = sum(count.viewvalues())
    avgEntropy /= tot_cnt
    return entropyParent - avgEntropy

node = 0
nodeMapping = {}
edges = []

def makeDecisionTree(data, target, parent=-1, path=''):
    '''Creates decision tree.
    '''
    global node, nodeMapping
    if parent >= 0:
        edges.append((parent, node, path))

    #Code to find the variable(column) with maximum information gain
    infoGain = []
    columns = [x for x in data[0]]
    for column in columns:
        if not(column == target):
            ent = entropy(data, target)
            infoGain.append( (findInformationGain(data, target, column, ent), column) )
    splitColumn = max(infoGain)[1]

    #Leaf node, final result, if maximum information gain is not significant
    if max(infoGain)[0] < 0.01:
        nodeMapping[node] = data[0][target]
        node += 1
        return
    nodeMapping[node] = splitColumn
    parent = node
    node += 1
    paths = { i[splitColumn] for i in data }#All out-going edges from current node
    for path in paths:

        #Create sub table under the current decision path
        modData = [x for x in data if x.has_key(splitColumn) and x[splitColumn] == path]
        for y in modData:
            if y.has_key(splitColumn):
                del y[splitColumn]

        #create sub-tree
        makeDecisionTree(modData, target, parent, path)

makeDecisionTree(data, target)

print 'nodemapping ==> ', nodeMapping, '\n\nedges ===>', edges
