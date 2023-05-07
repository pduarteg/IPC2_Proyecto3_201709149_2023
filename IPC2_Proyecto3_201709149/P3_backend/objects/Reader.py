import os
import xml.etree.ElementTree as eT

from . import ProfilesList
from . import Profile
from . import Word
from . import WordsList

class Reader:

	savedProfiles = ProfilesList.ProfilesList()
	discartedWords = WordsList.WordsList()

	new_profiles_cant = 0
	updated_profiles_cant = 0
	created_d_words = 0

	def process_XML_Sol1(self, root):
		self.new_profiles_cant = 0
		self.updated_profiles_cant = 0
		self.created_d_words = 0

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

			if found == None:
				self.new_profiles_cant += 1
				self.savedProfiles.addProfile(new_profile)
			else:
				self.updated_profiles_cant += 1
				found.update(new_key_words_list)							

		# Extracción de palabras descartadas
		discartedWords = root.find('descartadas').findall('palabra')
		for dWord in discartedWords:
			if self.discartedWords.isExistent(dWord.text) == False:
				self.created_d_words += 1
				self.discartedWords.addWord(Word.Word(dWord.text))

		print(" *** Información guardada correctamente.")

	def load_from_data_base(self):
		print(" *** Se cargará información de la base de datos...")
		self.reset_TDA()
		# Define la ruta del archivo XML

		print(os.getcwd())
		ruta_archivo = "files/storedDataService1.xml"

		try:
			# Abre el archivo XML
			tree = eT.parse(ruta_archivo)
			# Obtiene el elemento raíz del archivo XML
			root = tree.getroot()
			self.process_XML_Sol1(root)
			print(" *** Información previa cargada...")
		except:
			f = open('files/storedDataService1.xml', 'w')
			f.write('')

			print(" *** No se ha podido cargar la información previa.")

	def reset_TDA(self):
		self.savedProfiles = ProfilesList.ProfilesList()
		self.discartedWords = WordsList.WordsList()

		self.new_profiles_cant = 0
		self.updated_profiles_cant = 0
		self.created_d_words = 0