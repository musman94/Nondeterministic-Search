import random
from collections import deque


class Node:
	def __init__(self,ID):
		self.ID = ID
		self.origin = [None] * 6
		self.dest = [None] * 6
		self.children = []

def fillTree(root,S1,S2,S3,B1,B2,b):
	if S1 == 1:
		root.origin[0] = 1
		root.dest[0] = 0
	else:
		root.origin[0] = 0
		root.dest[0] = 1
	if S2 == 1:
		root.origin[1] = 1
		root.dest[1] = 0
	else:
		root.origin[1] = 0
		root.dest[1] = 1
	if S3 == 1:
		root.origin[2] = 1
		root.dest[2] = 0
	else:
		root.origin[2] = 0
		root.dest[2] = 1
	if B1 == 1:
		root.origin[3] = 1
		root.dest[3] = 0
	else:
		root.origin[3] = 0
		root.dest[3] = 1
	if B2 == 1:
		root.origin[4] = 1
		root.dest[4] = 0
	else:
		root.origin[4] = 0
		root.dest[4] = 1
	if b == 1:
		root.origin[5] = 1
		root.dest[5] = 0
	else:
		root.origin[5] = 0
		root.dest[5] = 1


def createTree(root):
	root.children.append(Node(2))
	root.children.append(Node(3))
	root.children.append(Node(4))
	fillTree(root.children[0],1,1,0,1,1,0)
	fillTree(root.children[1],1,1,1,0,0,0)
	fillTree(root.children[2],1,1,1,1,0,0)
	root.children[0].children.append(root)
	root.children[1].children.append(root)
	root.children[2].children.append(root)
	cur = root.children[1]
	cur.children.append(Node(5))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,1,1,1,0,1)
	cur = cur.children[1]
	cur.children.append(Node(6))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,1,0,1,0,0)
	cur = cur.children[1]
	cur.children.append(Node(7))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,1,0,1,1,1)
	cur = cur.children[1]
	cur.children.append(Node(8))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,0,0,1,1,0)
	cur.children.append(Node(9))
	cur.children[2].children.append(cur)
	fillTree(cur.children[2],1,1,0,0,0,0)
	cur = cur.children[2]
	cur.children.append(Node(10))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,1,1,0,0,1)
	cur.children.append(Node(11))
	cur.children[2].children.append(cur)
	fillTree(cur.children[2],1,1,0,1,0,1)
	cur = cur.children[2]
	cur.children.append(Node(12))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,0,0,1,0,0)
	cur = cur.children[1]
	cur.children.append(Node(13))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,0,0,1,1,1)
	cur = cur.children[1]
	cur.children.append(Node(14))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],0,0,0,1,1,0)
	cur.children.append(Node(15))
	cur.children[2].children.append(cur)
	fillTree(cur.children[2],1,0,0,0,0,0)
	cur = cur.children[2]
	cur.children.append(Node(16))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],1,1,0,0,0,1)
	cur.children.append(Node(17))
	cur.children[2].children.append(cur)
	fillTree(cur.children[2],1,0,0,1,0,1)
	cur = cur.children[2]
	cur.children.append(Node(18))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],0,0,0,1,0,0)
	cur = cur.children[1]
	cur.children.append(Node(19))
	cur.children[1].children.append(cur)
	fillTree(cur.children[1],0,0,0,1,1,1)

def draw(root,dic):
	print "SOLUTION PATH:"
	print "Node ID: {}".format(root.ID) 
	orig = "Original side: "
	dest = "Across river: "
	for x in xrange(len(root.origin)):
		if root.origin[x] == 1:
			if x < 3:
				orig += " Soldier "
			elif x < 5:
				orig += " Boy "
			else:
				orig += " Boat "
		else:
			if x < 3:
				dest += " Soldier "
			elif x < 5:
				dest += " Boy "
			else:
				dest += " Boat "
	print orig
	print dest
	print "CLOSED LIST:"
	print dic.keys()
	print "#############"



def search(root,ID):
	dic = {}
	q = deque()
	q.append(root)
	while q:
		root = q.popleft()
		dic[root.ID] = root
		draw(root,dic)
		if root.ID == ID:
			return True
		while root.children:
			temp = root.children.pop()
			if temp.ID not in dic:
				q.append(temp)
		random.shuffle(q)
	return False


root = Node(1)
fillTree(root,1,1,1,1,1,1)
createTree(root)
res = search(root,19)



