from django.db import models
class Patient(models.Model):
    identifiantunique = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    adresse = models.CharField(max_length=255)
    numero_telephone = models.IntegerField(max_length=10)
    assurance_maladie = models.CharField(max_length=12, unique=True)


    def __str__(self):
        return  f"{self.nom} {self.prenom}"


class Medcin(models.Model):
    identifiantunique = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=100)
    numero_licence = models.CharField(max_length=15, unique=True)
    numero_telephone = models.IntegerField(max_length=10)




    def __str__(self):
        return  f"{self.nom} {self.prenom}"






class RendezVous(models.Model):
        identifiantunique = models.AutoField(primary_key=True)
        date_rdv = models.DateField()
        heure_rdv = models.TimeField()
        motif_rdv = models.TextField()
        statut = models.CharField(max_length=20, choices=[('C', 'Confirmé'), ('A', 'Annulé'), ('EA', 'En attente'), ('R', 'Reprogrammé'), ('EC', 'En cours'), ('T', 'Terminé')])
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        medcin = models.ForeignKey(Medcin, on_delete=models.CASCADE)
        def __str__(self):
            return f"Rendez-vous {self.identifiantunique} - {self.date_rdv} {self.heure_rdv}"

class Consultation(models.Model):
    identifiantunique = models.AutoField(primary_key=True)
    date_consultation = models.DateField()
    motif_consultation = models.TextField()
    pateint_consultee = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medcin_responsable = models.ForeignKey(Medcin, on_delete=models.CASCADE)
    notes_consultation = models.TextField()




    def __str__(self):
        return f"Consultation {self.identifiantunique} - {self.date_consultation}"


class Departement(models.Model):
    identifiant_unique = models.AutoField(primary_key=True)
    nom_departement = models.CharField(max_length=255)
    chef_departement = models.ForeignKey(Medcin, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_departement

class Clinique(models.Model):
    identifiant_unique = models.AutoField(primary_key=True)
    nom_clinique = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    numero_telephone = models.IntegerField(max_length=10)
    departements = models.ManyToManyField(Departement, related_name='cliniques')

    def __str__(self):
        return self.nom_clinique


class DossierMedical(models.Model):
    identifiantunique = models.AutoField(primary_key=True)
    date_creation = models.DateField()
    motif_consultation = models.TextField()
    antecedents_medicaux = models.TextField()
    resultats_examens = models.TextField()
    diagnostic = models.TextField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    traitement_prescrit = models.TextField()
    evolution_sante = models.TextField()
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    medcin = models.ForeignKey(Medcin, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dossier Médical {self.identifiantunique} - {self.date_creation}"

class Tache(models.Model):
        identifiantunique = models.AutoField(primary_key=True)
        date_creation = models.DateField()
        date_echeance = models.DateField()
        description = models.TextField()
        dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)
        medcin = models.ForeignKey(Medcin, on_delete=models.CASCADE)
        statut = models.CharField(max_length=20, choices=[('A', 'A faire'), ('E', 'En cours'), ('T', 'Terminé')])
        priorite = models.CharField(max_length=20, choices=[('F', 'Faible'), ('M', 'Moyenne'), ('E', 'Elevée')])
        def __str__(self):
            return f"Tache {self.identifiantunique} - {self.date_creation}"
   
   
   
   
    




