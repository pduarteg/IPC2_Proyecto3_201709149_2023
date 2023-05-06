class ProfilesList:

	first = None
	cant = 0

	def addProfile(self, new_node):
		if self.first == None:
			self.first = new_node
			self.cant += 1
		else:
			t = self.first
			while t.next != None:
				t = t.next
			t.next = new_node
			self.cant += 1