class Writer:

	def write_stored_data_s1(self, savedProfiles, dWords):

		file = open('files/storedDataService1.xml', 'w')

		file.write('<configuracion>\n')

		file.write('	<perfiles>\n')

		tProfile = savedProfiles.first

		while tProfile != None:
			file.write('		<perfil>\n')
			file.write('			<nombre>' + tProfile.name + '</nombre>\n')
			file.write('			<palabrasClave>\n')

			tWord = tProfile.keyWordsList.first

			while tWord != None:
				file.write('				<palabra>' + tWord.text + '</palabra>\n')
				tWord = tWord.next
			file.write('			</palabrasClave>\n')
			file.write('		</perfil>\n')
			tProfile = tProfile.next

		file.write('	</perfiles>\n')
		
		tWord = None
		tWord = dWords.first
		file.write('	<descartadas>\n')
		while tWord != None:
			file.write('		<palabra>' + tWord.text + '</palabra>\n')
			tWord = tWord.next

		file.write('	</descartadas>\n')
		file.write('</configuracion>')