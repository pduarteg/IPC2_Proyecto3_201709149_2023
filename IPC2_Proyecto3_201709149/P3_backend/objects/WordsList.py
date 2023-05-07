class WordsList:

	first = None
	cant = 0

	def addWord(self, new_node):
		if self.first == None:
			self.first = new_node
			self.cant += 1
		else:
			t = self.first
			while t.next != None:
				t = t.next
			t.next = new_node
			self.cant += 1

	def isExistent(self, wordText):
		found = False
		t = self.first
		while t != None:
			if t.text == wordText:
				found = True
				break
			else:
				t = t.next
		return found