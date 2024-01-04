class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.augmenter_population()


paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants de la ville de Paris : {paris.get_nombre_habitants()}")

marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants de la ville de Marseille : {marseille.get_nombre_habitants()}")

# Création des objets Personne
crystal = Personne("crystal", 45, paris)
brioche = Personne("brioche", 4, paris)
pain = Personne("pain", 18, marseille)

crystal.ajouterPopulation()
brioche.ajouterPopulation()
pain.ajouterPopulation()


print(f"Mise à jour de la ville de Paris : {paris.get_nombre_habitants()}")
print(f"Mise à jour de la ville de Marseille : {marseille.get_nombre_habitants()}")
