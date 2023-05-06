class Profile:
	name = ""
	keyWordsList = None
	next = None

	def __init__(self, name, keyWordsList):
		self.name = name
		self.keyWordsList = keyWordsList