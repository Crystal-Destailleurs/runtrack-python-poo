class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Vroom! La voiture démarre.")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Vroum! La moto démarre.")

voiture1 = Voiture(marque="Toyota", modele="Camry", annee=2022, prix=25000)

voiture1.informationsVehicule()

voiture1.demarrer()

moto1 = Moto(marque="Honda", modele="CBR", annee=2022, prix=12000)

moto1.informationsVehicule()

moto1.demarrer()
