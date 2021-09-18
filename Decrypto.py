import string

class Decrypto:
	"""
	cette class est cree pour crypter ou decrypter
	des phrase et des scriptes
	"""
	def __init__(self, script, key):
		self.alpha = list(char for char in string.ascii_lowercase)
		self.script = script.lower()
		self.key = "".join(key).lower()
		self.matrix = self.create_matrix()
		self.collage = self.pre_collage()
		self.decrypte = self.decryptage()
		

	def create_matrix(self):
		"""
		Cette methode pour cree la gride de cryptage des phrases
		ou decryptage des scripte
		"""
		matrix=[]
		num_row_created=0
		while len(matrix) < len(self.alpha):
			row =[]
			for num in range(len(self.alpha)):
				if len(matrix)==0:
					row.append(self.alpha[num])
				else:
					row.append(self.alpha[num_row_created-len(self.alpha)+num])
			matrix.append(row)
			num_row_created+=1
		return matrix

	def pre_collage(self):
		"""
		cette methode pour pre-coller la char du key sur les scripte
		"""
		crypto_script=[]
		pas =0
		for lettre in self.script:
			if lettre in string.ascii_lowercase:
				if pas == len(self.key):
					pas =0
					crypto_script.append(self.key[pas])
					pas +=1
				else:
					crypto_script.append(self.key[pas])
					pas +=1
			else:
				crypto_script.append(lettre)
		return crypto_script

	def decryptage(self):
		"""
		cette methode pour faire la comparison entre le scripte
		et le pre_collage methode pour extraire les lettre
		"""
		decrypta_script =[]
		pos_letter_ph=0
		for pre_collage_lettre in self.collage:
			if pre_collage_lettre in self.alpha:
				pos_cp = self.alpha.index(pre_collage_lettre)
				for row in self.matrix:
					if row[pos_cp] == self.script[pos_letter_ph]:
						decrypta_script.append(row[0])
					else:
						pass
			else:
					decrypta_script.append(pre_collage_lettre)
			pos_letter_ph +=1
		return "".join(decrypta_script)


