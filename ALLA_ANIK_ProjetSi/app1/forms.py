from django.db.models import fields
from django import forms
from .models import Patient, Medcin, RendezVous, Consultation, Tache, DossierMedical, Departement

class AddPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class AddMedcin(forms.ModelForm):
    class Meta:
        model = Medcin
        fields = '__all__'

class AddRendezVous(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = '__all__'

class AddConsultation(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'

class AddTache(forms.ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'

class AddDossier(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = '__all__'