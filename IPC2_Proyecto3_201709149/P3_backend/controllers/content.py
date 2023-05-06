class Publications:
	def __init__(self):
		self.Lista = []

	def Agregar(self, Autor, Contenido, Fecha):
		self.Lista.append(PubliactionClass(Autor, Contenido, Fecha))

	def Editar(self, position, Autor, Contenido):
		if len(self.Lista) > position:
			self.Lista[position].Editar(Autor, Contenido)
			return True
		else:
			return False

class PublicationClass:
	def __init__(self, Autor, Content, Date):
		self.Autor = Autor
		self.Content = Content
		self.Date = Date

publicationsList = [
	{"Autor": "autor1",
	"Contenido": "uso de diccionarios",
	"FechaPublicación": "5-03-2019 09:55:38"},
	{"Autor": "autor2",
	"Contenido": "sin uso de objetos",
	"FechaPublicación": "5-03-2019 09:10:38"}
]