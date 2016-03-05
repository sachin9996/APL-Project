LEFT = 0
RIGHT = 1

class node:
	def __init__(self, val, par=None, side=None):
		self.key = val
		self.right = None
		self.left = None
		self.direction = side
		self.parent = par

class splay_tree:
	def __init__(self, root=None):
		self.root = root

	def _find(self, n, value):
		if self.root is None:
			return None
		if n.key == value:
			return n
		elif value<n.key:
			if n.left is not None:
				return self._find(n.left, value)
			else:
				return n
		else:
			if n.right is not None:
				return self._find(n.right, value)
			else:
				return n

	def _right_rotate(self, rotate_node):
		b = rotate_node
		a = b.parent
		a.left = b.right
		b.right = a
		b.parent = a.parent
		a.parent = b
		if b.parent is None:
			self.root = b
		
		if a.left is not None:
			a.left.parent = a
		
		b.direction = a.direction
		a.direction = RIGHT
		if a.left is not None:
			a.left.direction = LEFT
		
		return

	def _left_rotate(self, rotate_node):
		b = rotate_node
		a = b.parent
		a.right = b.left
		b.left = a
		b.parent = a.parent
		a.parent = b
		if b.parent is None:
			self.root = b			
		
		if a.right is not None:
			a.right.parent = a
		
		b.direction = a.direction
		a.direction = LEFT
		if a.right is not None:
			a.right.direction = RIGHT
		
		return

	def _splay(self, splay_node):
		if splay_node == self.root or splay_node is None:
			return

		elif splay_node.parent.parent is None:
			if splay_node.direction == LEFT:
				self._right_rotate(splay_node)
			else:
				self._left_rotate(splay_node)
			return

		else:
			parent_node = splay_node.parent
			if parent_node.direction == LEFT:
				if splay_node.direction == LEFT:
					self._right_rotate(parent_node)
					self._right_rotate(splay_node)
				else:
					self._left_rotate(splay_node)
					self._right_rotate(splay_node)
			else:
				if splay_node.direction == LEFT:
					self._right_rotate(splay_node)
					self._left_rotate(splay_node)
				else:
					self._left_rotate(parent_node)
					self._left_rotate(splay_node)
			self._splay(splay_node)		
			return	
				
	def _insert(self, value, insert_node):
		if insert_node is None:
			self.root = node(value)
			return self.root

		elif value>insert_node.key:
			if insert_node.right is None:
				n = node(value, par=insert_node, side=RIGHT)
				insert_node.right = n
				return n
			else:
				return self._insert(value, insert_node.right)

		else:
			if insert_node.left is None:
				n = node(value, par=insert_node, side=LEFT)
				insert_node.left = n
				return n
			else:
				return self._insert(value, insert_node.left)

	def _inorder(self, node):
		if node is None:
			return 
		else:
			self._inorder(node.left)
			print node.key, node.direction,
			if node.parent is not None:
				print node.parent.key
			else:
				print node.parent
			self._inorder(node.right)
			return

	def _delete_root(self):
		if self.root is None:
			return
		elif self.root.left is None and self.root.right is None:
			del self.root
			self.root = None
			return
		elif self.root.left is None:
			new_root = self.root.right
			new_root.direction = None
			new_root.parent = None
			del self.root
			self.root = new_root
			return
		else:
			left_tree = splay_tree(self.root.left)
			right_tree = splay_tree(self.root.right)

			largest = left_tree.root
			while largest.right is not None:
				largest = largest.right
			left_tree._splay(largest)
			new_root = left_tree.root
			new_root.direction = None
			new_root.parent = None
			new_root.right = right_tree.root
			if right_tree.root is not None:
				right_tree.root.parent = new_root
			del self.root
			self.root = left_tree.root
			return

	def find(self, value):
		find_node = self._find(self.root, value)
		self._splay(find_node)
		if find_node is None:
			return None
		else:
			if self.root.key == value:
				return True
			else:
				return False

	def insert(self, value):
		if self.root is None:
			self.root = node(val=value)
		else:
			insert_node = self._find(self.root, value)
			if insert_node.key != value:
				if value>insert_node.key:
					insert_node.right = node(val=value, par=insert_node, side=RIGHT)
					self._splay(insert_node.right)
				else:
					insert_node.left = node(val=value, par=insert_node, side=LEFT)
					self._splay(insert_node.left)
			else:
				self._splay(insert_node)
		return

	def delete(self, value):
		delete_node = self._find(self.root, value)
		if delete_node is None:
			return
		else:
			self._splay(delete_node)
			if self.root.key == value:
				self._delete_root()
		return

	def inorder(self):
		self._inorder(self.root)
		return

'''
T = splay_tree()
T.root = node(val=100, par=None, side=None)
T.root.right = node(val=500, par=T.root, side=1)
T.root.right.left = node(val=400, par=T.root.right, side=0)
print T.find(400)
T.inorder()
'''