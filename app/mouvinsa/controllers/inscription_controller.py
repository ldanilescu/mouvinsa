from wtforms import Form, BooleanField, TextField, FloatField, PasswordField, SelectField, DateField, validators

class InscriptionForm(Form):
	email = TextField(u'Email', [validators.Required(message='Ce champs est obligatoire. Veuillez le remplir.'), validators.EqualTo('Confirmez votre email', message='Les 2 emails doivent correspondre'), validators.Length(min=6, max=35, message='La longeur doit etre comprise entre 6 et 35 caracteres.')])

	confirmEmail = TextField(u'Confirmez votre email', [validators.Required(message='Ce champs est obligatoire. Veuillez le remplir.'), validators.Length(min=6, max=35, message='La longeur doit etre comprise entre 6 et 35 caracteres.')])

	surnom = TextField(u'Pseudonyme', [validators.Required(message='Ce champs est obligatoire. Veuillez le remplir.'), validators.Length(min=2, max=25, message='La longeur doit etre comprise entre 2 et 25 caracteres.')])

	nom = TextField(u'Nom', [validators.Optional(), validators.Length(min=2, max=25, message='La longeur doit etre comprise entre 2 et 25 caracteres.')])

	prenom = TextField(u'Prenom', [validators.Optional(), validators.Length(min=2, max=25, message='La longeur doit etre comprise entre 2 et 25 caracteres.')])

	categorie = SelectField(u'Categorie ', [validators.Required(message='Ce champs est obligatoire. Veuillez choisir un item dans la liste.')], choices=[('',''),('Etudiant', 'Etudiant'), ('Enseignant-Chercheur', 'Enseignant-Chercheur'), ('Personnel BIATOS', 'Personnel BIATOS')])

	annee = SelectField(u'Annee ', choices=[('', ''), ('Premiere', 'Premiere'), ('Deuxieme', 'Deuxieme'), ('Troisieme', 'Troisieme'), ('Quatrieme', 'Quatrieme'), ('Cinquieme', 'Cinquieme')])

	cycle = SelectField(u'Cycle ', choices=[('', ''), ('Premier', 'Premier'), ('Second', 'Second')])

	filiere = SelectField(u'Filiere ', choices=[('', ''), ('Filiere Internationale','Filiere Internationale'), ('Filiere Clasique', 'Filiere Clasique'), ('PCE','PCE'), ('FAS','FAS'), ('SHN','SHN')])

	departement = SelectField(u'Departement', choices=[('',''), ('BB', 'BB'), ('BIM', 'BIM'), ('GE', 'GE'), ('GI', 'GI'), ('GCU', 'GCU'), ('GEN', 'GEN'), ('GMC', 'GMC'), ('GMD', 'GMD'), ('GMPP', 'GMPP'), ('IF', 'IF'), ('SGM', 'SGM'), ('TC', 'TC')])

	password = PasswordField(u'Mot de Passe', [
		validators.Required(message='Ce champs est obligatoire. Veuillez le remplir.'),
		validators.EqualTo('confirm', message='Les 2 mots de passe doivent correspondre'),
		validators.Length(min=4, max=25, message='La longeur doit etre comprise entre 4 et 25 caracteres.')
	])

	confirm = PasswordField(u'Confirmez votre mot de passe', [validators.Required(message='Ce champs est obligatoire. Veuillez le remplir.')])

	dateNaissance = DateField(u'Ne(e) le', format='%d/%m/%Y',  validators=[validators.Optional()])

	sexe = SelectField(u'Sexe ', choices=[('', ''), ('Masculin', 'Masculin'), ('Feminin', 'Feminin')])

	poids = FloatField(u'Poids (kg)', [validators.Optional(), validators.NumberRange(min=20, max=300, message='Le poids doit etre compris entre 20 kg et 300 kg')])

	hauteur = FloatField(u'Taille (cm)', [validators.Optional(), validators.NumberRange(min=90, max=250, message='La taille doit etre comprise entre 90 cm et 250 cm.')])

	position = TextField(u'Position', [validators.Optional(), validators.Length(min=3, max=100,  message='La longeur doit etre comprise entre 3 et 100 caracteres.')])

	affiliation = TextField(u'Affiliation', [validators.Optional(), validators.Length(min=3, max=100,  message='La longeur doit etre comprise entre 3 et 100 caracteres.')])


def createStudent(form, student):
	student.firstname = form.prenom.data
	student.lastname = form.nom.data
	student.nickname = form.surnom.data
	student.password = form.password.data
	student.email = form.email.data
	if form.sexe.data == '':
		student.sex = 'Inconnu'
	else:
		student.sex = form.sexe.data
	student.category = 'etudiant'
	student.year = form.annee.data
	student.cycle = form.cycle.data
	if form.cycle.data == 'Premier':
		student.branch = form.filiere.data
	else:
		student.branch = form.departement.data
	student.birthdate = form.dateNaissance.data
	student.weight = form.poids.data
	student.height = form.hauteur.data
	student.etat = "PREREGISTERED"


def createEmployee(form, employee):
	employee.firstname = form.prenom.data
	employee.lastname = form.categorie.data
	employee.nickname = form.surnom.data
	employee.password = form.password.data
	employee.birthdate = form.dateNaissance.data
	employee.email = form.email.data
	employee.sex = form.sexe.data
	if form.categorie.data == 'Enseignant-Chercheur':
		employee.category = 'enseignant'
	else:
		employee.category = 'iatos'

	employee.weight = form.poids.data
	employee.height = form.hauteur.data
	employee.etat = "PREREGISTERED"
