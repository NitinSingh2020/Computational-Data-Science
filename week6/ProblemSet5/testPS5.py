from graph import *
from ps5 import *

def test1():
	g = WeightedDigraph()
	na = Node('a')
	nb = Node('b')
	nc = Node('c')
	g.addNode(na)
	g.addNode(nb)
	g.addNode(nc)
	e1 = WeightedEdge(na, nb, 15, 10)
	print e1 # a->b (15, 10)
	print e1.getTotalDistance() # 15
	print e1.getOutdoorDistance() # 10
	e2 = WeightedEdge(na, nc, 14, 6)
	e3 = WeightedEdge(nb, nc, 3, 1)
	print e2 # a->c (14, 6)
	print e3 # b->c (3, 1)
	g.addEdge(e1)
	g.addEdge(e2)
	g.addEdge(e3)
	print g # a->b (15.0, 10.0) a->c (14.0, 6.0) b->c (3.0, 1.0)

def test2():
	mitMap = load_map("mit_map.txt")
	print isinstance(mitMap, Digraph)
	print isinstance(mitMap, WeightedDigraph)

if __name__ == '__main__':
	test2()