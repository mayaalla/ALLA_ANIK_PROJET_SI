from django.shortcuts import render, redirect
from .models import Departement
from .models import Patient
from .models import Medcin
from .models import RendezVous
from .models import Consultation
from .models import Tache
from .models import DossierMedical
from .forms import AddPatient
from .forms import AddMedcin
from .forms import AddConsultation
from .forms import AddTache
from .forms import AddDossier
from .forms import AddRendezVous



# from .models import Product
# def affiche_departement(request):
# departement = Departement.objects.all()
# return render(request, 'index.html', {"departement": departement})
def affiche_departement(request):
    d = Departement.objects.all()
    return render(request, 'index.html', {"departement": d})

def cardiologique(request):
    return render(request, 'Cardiologie.html')

def patient_afficher(request):
    p = Patient.objects.all()
    return render(request, 'patient.html', {"p": p})

def midecin_afficher(request):
    m = Medcin.objects.all()
    return render(request, 'midecin.html', {"m": m})

def rdv_afficher(request):
    r = RendezVous.objects.all()
    return render(request, 'rdv.html', {"r": r})

def consultation_afficher(request):
    c = Consultation.objects.all()
    return render(request, 'consultation.html', {"c": c})

def tache_afficher(request):
    t = Tache.objects.all()
    return render(request, 'tache.html', {"t": t})

def dossier_afficher(request):
    d = DossierMedical.objects.all()
    return render(request, 'dossier.html', {"d": d})

def rechrche(request):
    return render(request, 'search.html')





def index1(request):
    return render(request, 'index1.html')

# def rdv_afficher(request):
#     r = RendezVous.objects.all()
#     return render(request, 'rdv.html', {"rdv": r})

# def consultation_afficher(request):
#     c = Consultation.objects.all()
#     return render(request, 'consultation.html', {"consultation": c})

# def tache_afficher(request):
#     t = Tache.objects.all()
#     return render(request, 'tache.html', {"tache": t})

# def dossier_afficher(request):
#     d = DossierMedical.objects.all()
#     return render(request, 'dossier.html', {"dossier": d})

def rechrcheP(request):
    patient =''
    
    if request.method =="GET":
        query = request.GET.get('rechrcheP')
        if query:
            patient = Patient.objects.filter(identifiantunique__contains=query)
    return render(request, 'searchp.html', {"patient": patient})

def rechrcheM(request):
    medcin =''
    
    if request.method =="GET":
        query1 = request.GET.get('rechrcheM')
        if query1:
            medcin = Medcin.objects.filter(identifiantunique__contains=query1)
    return render(request, 'searchm.html', {"medcin": medcin})

def rechrcheR(request):
    rdv =''
    
    if request.method =="GET":
        query2 = request.GET.get('rechrcheR')
        if query2:
            rdv = RendezVous.objects.filter(identifiantunique__contains=query2)
    return render(request, 'searchr.html', {"rdv": rdv})

def rechrcheC(request):
    consultation =''
    
    if request.method =="GET":
        query3 = request.GET.get('rechrcheC')
        if query3:
            consultation = Consultation.objects.filter(identifiantunique__contains=query3)
    return render(request, 'searchc.html', {"consultation": consultation})

def rechrcheT(request):
    tache =''
    
    if request.method =="GET":
        query4 = request.GET.get('rechrcheT')
        if query4:
            tache = Tache.objects.filter(identifiantunique__contains=query4)
    return render(request, 'searcht.html', {"tache": tache})

def rechrcheD(request):
    dossier =''
    
    if request.method =="GET":
        query5 = request.GET.get('rechrcheD')
        if query5:
            dossier = DossierMedical.objects.filter(identifiantunique__contains=query5)
    return render(request, 'searchd.html', {"dossier": dossier})



# class Patient(models.Model):
#     identifiantunique = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=255)
#     prenom = models.CharField(max_length=255)
#     date_naissance = models.DateField()
#     sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
#     adresse = models.CharField(max_length=255)
#     numero_telephone = models.CharField(max_length=10)
#     assurance_maladie = models.CharField(max_length=50, unique=True)


def add(request):
    if request.method == 'POST':
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            mssg = "PATIENT AJOUTER AVEC SUCCES"
            return render(request, 'create.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddPatient()
    return render(request, 'create.html', {'form': form})

def addm(request):
    if request.method == 'POST':
        form = AddMedcin(request.POST)
        if form.is_valid():
            form.save()
            mssg = "MEDECIN AJOUTER AVEC SUCCES"
            return render(request, 'createM.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddMedcin()
    return render(request, 'createM.html', {'form': form})

def addp(request):
    if request.method == 'POST':
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            mssg = "PATIENT AJOUTER AVEC SUCCES"
            return render(request, 'createP.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddPatient()
    return render(request, 'createP.html', {'form': form})

def addc(request):
    if request.method == 'POST':
        form = AddConsultation(request.POST)
        if form.is_valid():
            form.save()
            mssg = "CONSULTATION AJOUTER AVEC SUCCES"
            return render(request, 'createC.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddConsultation()
    return render(request, 'createC.html', {'form': form})

def addt(request):
    if request.method == 'POST':
        form = AddTache(request.POST)
        if form.is_valid():
            form.save()
            mssg = "TACHE AJOUTER AVEC SUCCES"
            return render(request, 'createT.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddTache()
    return render(request, 'createT.html', {'form': form})

def addd(request):
    if request.method == 'POST':
        form = AddDossier(request.POST)
        if form.is_valid():
            form.save()
            mssg = "DOSSIER AJOUTER AVEC SUCCES"
            return render(request, 'createD.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddDossier()
    return render(request, 'createD.html', {'form': form})

def addr(request):
    if request.method == 'POST':
        form = AddRendezVous(request.POST)
        if form.is_valid():
            form.save()
            mssg = "RENDEZ VOUS AJOUTER AVEC SUCCES"
            return render(request, 'createR.html', {'form' : form, 'mssg': mssg}) 
    else:
        form = AddRendezVous()
    return render(request, 'createR.html', {'form': form})


def editP(request, id):
    p = Patient.objects.get(identifiantunique=id)

    if request.method == 'POST':
        form = AddPatient(request.POST, instance=p)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            # rediriger vers la page liste patient
            return redirect('/gerer_patient')
    else:
        form = AddPatient(instance=p)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'patientU.html', {'form': form})

def editM(request, id):
    m = Medcin.objects.get(identifiantunique=id)

    if request.method == 'POST':
        form = AddMedcin(request.POST, instance=m)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            # rediriger vers la page url de liste patient
            return redirect('/gerer_medcin')
    else:
        form = AddMedcin(instance=m)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'midecinU.html', {'form': form})

def editC(request, id):
    c = Consultation.objects.get(identifiantunique=id)

    if request.method == 'POST':
        form = AddConsultation(request.POST, instance=c)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            # rediriger vers la page url de liste patient
            return redirect('/gerer_consultation')
    else:
        form = AddConsultation(instance=c)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'consultationU.html', {'form': form})

def editR(request, id):
    r = RendezVous.objects.get(identifiantunique=id)

    if request.method == 'POST':
        form = AddRendezVous(request.POST, instance=r)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            # rediriger vers la page url de liste patient
            return redirect('/gerer_rdv')
    else:
        form = AddRendezVous(instance=r)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'rdvU.html', {'form': form})

def editT(request, id):
    t = Tache.objects.get(identifiantunique=id)

    if request.method == 'POST':
        form = AddTache(request.POST, instance=t)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            # rediriger vers la page url de liste patient
            return redirect('/gerer_tache')
    else:
        form = AddTache(instance=t)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'tacheU.html', {'form': form})

def editD(request, id):
    d = DossierMedical.objects.get(identifiantunique=id)

    if request.method == 'POST':
        form = AddDossier(request.POST, instance=d)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            # rediriger vers la page url de liste patient
            return redirect('/gerer_dossier')
    else:
        form = AddDossier(instance=d)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié
        return render(request, 'dossierU.html', {'form': form})

# def Suppression_Commande(request, id) :
# commande = Commande.Objects.get(id=id)
# if request.method == 'POST' :
# commande.delete()
# return redirect('TBL_cmd')
# return render (request, 'Commande_delete.html', {'commande' ; commande})

def deleteP(request, id):
    p = Patient.objects.get(identifiantunique=id)
    if request.method == 'POST':
        p.delete()
        return redirect('/gerer_patient')
    return render(request, 'patientS.html', {'p': p})

def deleteM(request, id):
    m = Medcin.objects.get(identifiantunique=id)
    if request.method == 'POST':
        m.delete()
        return redirect('/gerer_medcin')
    return render(request, 'midecinS.html', {'m': m})

def deleteC(request, id):
    c = Consultation.objects.get(identifiantunique=id)
    if request.method == 'POST':
        c.delete()
        return redirect('/gerer_consultation')
    return render(request, 'consultationS.html', {'c': c})

def deleteR(request, id):
    r = RendezVous.objects.get(identifiantunique=id)
    if request.method == 'POST':
        r.delete()
        return redirect('/gerer_rdv')
    return render(request, 'rdvS.html', {'r': r})

def deleteT(request, id):
    t = Tache.objects.get(identifiantunique=id)
    if request.method == 'POST':
        t.delete()
        return redirect('/gerer_tache')
    return render(request, 'tacheS.html', {'t': t})

def deleteD(request, id):
    d = DossierMedical.objects.get(identifiantunique=id)
    if request.method == 'POST':
        d.delete()
        return redirect('/gerer_dossier')
    return render(request, 'dossierS.html', {'d': d})