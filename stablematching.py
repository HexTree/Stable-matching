__author__ = 'Liam Mencel'

import networkx as nx
#import matplotlib.pyplot as plt

# Read data from text file, and populate data tables
with open("data.txt", 'r') as f:
    a, b = [int(x) for x in f.readline().split()]
    scores = [int(x) for x in f.readline().split()]

    # collect names of students
    students = f.readline().split()
    slookup = set(students)
    n = len(students)

    # collect names of tasks
    tasks = f.readline().split()
    tlookup = set(tasks)
    m = len(tasks)

    cost = dict()
    for line in f:
        if line == "\n":
            break
        data = line.split()
        if data[1] != '-':
            print "ERROR - missing \'-\' symbol"
            break
        if data[0] not in slookup:
            print "ERROR - " + data[0] + " not in list of students. Typo?"
        for i in range(2, len(data)):
            c = 0
            if (i-2) < len(scores):
                c = -scores[i-2]
            if data[i] not in tlookup:
                print "ERROR - " + data[i] + " not in list of tasks. Typo?"
            cost[(data[0], data[i])] = c

# Build graph under networkx
G = nx.DiGraph()
G.add_node('S', demand = -n)
G.add_node('T', demand = (n - m*a))
for i in range(n):
    G.add_edge('S', students[i], capacity = 1)
for i in range(m):
    G.add_node(tasks[i], demand = a)
    G.add_edge(tasks[i], 'T', capacity = (b-a))
for i in range(n):
    for j in range(m):
        c = 0
        if (students[i], tasks[j]) in cost:
            c = cost[(students[i], tasks[j])]
        G.add_edge(students[i], tasks[j], weight = c)

# Use to view graph
#nx.draw_networkx(G)
#plt.show()

# Run flow algorithm
print "Calculating optimal solution..."
flowCost, flowDict = nx.network_simplex(G)
print "...done. Total score = %d" % -flowCost
#print flowDict
for x in students:
    for y in flowDict[x]:
        if flowDict[x][y] == 1:
            print "Assign " + x + " to " + y

