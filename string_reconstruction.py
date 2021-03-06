import sys, fileinput

def walk_graph(graph, walked_graph, num_edges, cycle):
#	print cycle, num_edges
	if len(cycle) == num_edges:
		return cycle
#find the starting node
	start = 0
	node = cycle[start]
	while start<len(cycle):
		node = cycle[start]
		if len(walked_graph[node])<len(graph[node]):
			break
		start+=1
#refurbish cycle
	cycle = cycle[start:]+cycle[:start]
	if len(cycle)==1:
		cycle = []
	
	while len(cycle)<num_edges and len(graph[node])>len(walked_graph[node]):
		cycle.append(node)
		next_node = [ii for ii in graph[node] if ii not in walked_graph[node]][0]
		walked_graph[node].add(next_node)
		node = next_node

#	print cycle

	return walk_graph(graph, walked_graph, num_edges, cycle)

source = fileinput.input()


graph = {}
walked_graph = {}
num_edges = 0

graph_counts = {}

for line in source:
	if '->' not in line:
		break
	(s,t) = [l.strip() for l in line.strip().split('->')]
	nodes = set(t.split(','))
	graph[s] = nodes
	num_edges += len(nodes)
	walked_graph[s] = set()
	if s not in graph_counts:
		graph_counts[s] = [0,0]
	graph_counts[s][1] = len(nodes)
	for n in nodes:
		if n not in graph_counts:
			graph_counts[n] = [0,0]
		graph_counts[n][0]+=1

source.close()

#unbalanced = [k for k in graph_counts if graph_counts[k][0]!=graph_counts[k][1]]

#print unbalanced

the_start, the_finish = None,None

for k in graph_counts:
	if the_start>=0 and the_finish>=0:
		break
	if graph_counts[k][0]==graph_counts[k][1]:
		continue
	if graph_counts[k][0]<graph_counts[k][1]:
		the_start = k
	else:
		the_finish = k

#print the_start, the_finish

if (not(the_start is None) and not(the_finish is None)):
 	if the_finish not in graph:
		graph[the_finish] = set()
		walked_graph[the_finish] = set()
	graph[the_finish].add(the_start)
	num_edges+=1
#exit(0)

cycle = walk_graph(graph, walked_graph, num_edges, [graph.keys()[0]])

if not(the_start is None) and not(the_finish is None):
#	print "!!!"
	while cycle[0]!=the_start or cycle[-1]!=the_finish:
#		print cycle
		cycle = cycle[1:]+[cycle[0]]

#cycle.append(cycle[0])
#print cycle
print cycle[0]+''.join([cc[-1] for cc in cycle[1:]])

