import xml.etree.ElementTree as eT

from . import ProfilesList
from . import Profile
from . import Word
from . import WordsList

class Reader:

	savedProfiles = ProfilesList.ProfilesList()
	discartedWords = WordsList.WordsList()

	def process_XML_Sol1(self, root):
		print("Se procesará el archivo de la solicitud 1")
		# Procesado de perfiles
		profiles = root.find('perfiles').findall('perfil')

        # Extracción de perfiles
		for profile in profiles:
			name = profile.find('nombre').text
			new_key_words_list = WordsList.WordsList()
			words = profile.find('palabrasClave').findall('palabra')
			for word in words:
				new_key_word = Word.Word(word.text)
				new_key_words_list.addWord(new_key_word)
				#palabras_clave = [palabra.text for palabra in perfil.find('palabrasClave').findall('palabra')]
				new_profile = Profile.Profile(name, new_key_words_list)

			found = self.savedProfiles.searchByName(name)
			if found != None:
				
				self.savedProfiles.addProfile(new_profile)
		# Extracción de palabras descartadas
		discartedWords = root.find('descartadas').findall('palabra')
		for dWord in discartedWords:
			self.discartedWords.addWord(Word.Word(dWord.text))
		print(" *** Información guardada correctamente.")