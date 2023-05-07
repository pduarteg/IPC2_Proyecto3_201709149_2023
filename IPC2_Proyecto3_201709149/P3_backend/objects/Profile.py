from . import Word

class Profile:
	name = ""
	keyWordsList = None
	next = None

	def __init__(self, name, keyWordsList):
		self.name = name
		self.keyWordsList = keyWordsList

	def update(self, list):
		t = list.first

		while t != None:
			if self.keyWordsList.isExistent(t.text) == False:
				self.keyWordsList.addWord(Word.Word(t.text))
			t = t.next