from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkcalendar import *
from datetime import date

#definition de fentre
fenetre = Tk()
fenetre.title("Insurability")
fenetre.geometry('520x820')

#insert data label
label = Label(fenetre, text="Inserer les données du client ici")
label.grid(column=1,row=1,pady=30,columnspan=3)

#CIN line
CIN_label = Label(fenetre, text="CIN: ")
CIN_label.grid(column=1,row=2,pady=10)
CIN = Entry(fenetre,width=10)
CIN.grid(column=2, row=2,columnspan=2)

#Nom line
name_label = Label(fenetre, text="Nom: ")
name_label.grid(column=1,row=3,pady=10)
nom = Entry(fenetre,width=30)
nom.grid(column=2, row=3,columnspan=2)

#Prenom line
last_label = Label(fenetre, text="Prenom: ")
last_label.grid(column=1,row=4,pady=10)
last = Entry(fenetre,width=30)
last.grid(column=2, row=4,columnspan=2)

#date naissance line
birth_label = Label(fenetre, text="Date de naisance: ")
birth_label.grid(column=1,row=5,pady=10)
date_nais = Calendar(fenetre, selectmode="day", year=2000, month=1, day=1)
date_nais.grid(column=2,row=5,columnspan=2)

#Genre line
genre_label = Label(fenetre, text="Genre: ")
genre_label.grid(column=1,row=6,pady=10)
genre = IntVar()
genre.set(1)
rbh = Radiobutton(fenetre, text="H", variable=genre, value=1)
rbh.grid(column=2,row=6)
rbf = Radiobutton(fenetre, text="F", variable=genre, value=2)
rbf.grid(column=3,row=6)

#Situation line
sit_label = Label(fenetre, text="Situation: ")
sit_label.grid(column=1,row=7,pady=10)
situ = Combobox(fenetre, state='readonly')
situ['values']= ("<choisir>",  "Célibataire", "Marié", "Divorcé", "Veuf")
situ.current(0) #set the selected item
situ.grid(column=2,row=7,columnspan=2)

#date permis line
perm_label = Label(fenetre, text="Date d'obtention du permis: ")
perm_label.grid(column=1,row=8,pady=10)
date_perm = Calendar(fenetre, selectmode="day", year=2020, month=1, day=1)
date_perm.grid(column=2,row=8,columnspan=2)

#Type vehicule line
type_label = Label(fenetre, text="Type de vehicule: ")
type_label.grid(column=1,row=9,pady=10)
typ = Combobox(fenetre, state='readonly')
typ['values']= ("<choisir>",  "Sport", "SUV", "Break", "Berline", "Compact", "Utilitaire")
typ.current(0) #set the selected item
typ.grid(column=2,row=9,columnspan=2)

#puissance line
p_label = Label(fenetre, text="Puissance de vehicule: ")
p_label.grid(column=1,row=10,pady=10)
chev = Combobox(fenetre, state='readonly')
chev['values']= ("<choisir>",  "4 CV et moins", "5 à 7 CV", "8 à 9 CV", "10 à 11 CV", "12 à 13 CV", "14 à 15 CV", "16 CV et plus")
chev.current(0) #set the selected item
chev.grid(column=2, row=10,columnspan=2)


result = Label(fenetre, text="")
result.grid(column=2,row=11,columnspan=2)

def clicked():

	cin = CIN.get()
	name = nom.get()
	prenom = last.get()
	situa = situ.get()
	ty = typ.get()
	puiss = chev.get()
	ob_perm = date_perm.get_date()
	now = date.today()
	curr_year = now.year
	#anc reptresente l'ancienneté du permis 
	if (int(ob_perm[-2:]) > int(str(curr_year)[2:4])):
		anc = curr_year - int("19" + ob_perm[-2:]) 
	else:
		anc = int(str(curr_year)[2:4]) - int(ob_perm[-2:])


	
	error_string = "Informations manquantes: "
	if (len(cin) != 8):
		error_string += "\n -Numero CIN valide"

	if (len(name) == 0):
		error_string += "\n -Nom vide"

	if (len(prenom) == 0):
		error_string += "\n -Prénom"

	if (situa == "<choisir>"):
		error_string += "\n -Aucune situation selectionnée"

	if (ty == "<choisir>"):
		error_string += "\n -Aucun type de vehicule selectionné"

	if (puiss == "<choisir>"):
		error_string += "\n -Aucune puissance de vehicule selectionnée"
	

	if (error_string != "Informations manquantes: "):
		result['text'] = error_string

	else:
		score = 0

		situ__switcher = {
			"Célibataire" : 0,
			"Marié" : 6,
			"Divorcé" : 2,
			"Veuf" : 4
		}

		type__switcher = {
			"Sport" : 0,
			"SUV" : 5,
			"Break" : 10,
			"Berline" : 15,
			"Compact" : 20,
			"Utilitaire" : 25
		}

		puiss__switcher = {
			"4 CV et moins" : 60,
			"5 à 7 CV" : 50,
			"8 à 9 CV" : 40,
			"10 à 11 CV" : 30,
			"12 à 13 CV" : 20,
			"14 à 15 CV" : 10,
			"16 CV et plus" : 0 
		}


		score += ( puiss__switcher.get(puiss) + type__switcher.get(ty) + situ__switcher.get(situa) )

		if   5 < anc <= 15 : score += 7
		elif 15 < anc <= 25 : score += 14
		elif 25 < anc  : score += 21

		#messagebox.showinfo("score",str(score))

		if score <= 20 : result['text'] = "Mauvais assuré"
		elif 20 < score < 40 : result['text'] = "Assuré incertain"
		elif score >= 40 : result['text'] = "Bon assuré"
		
	

bt = Button(fenetre,text="Verifier",command=clicked)
bt.grid(column=1,row=11,pady=10)



fenetre.mainloop()
