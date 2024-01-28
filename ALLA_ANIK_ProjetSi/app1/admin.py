from django.contrib import admin
from .models import Medcin
from .models import Consultation
from .models import Clinique
from .models import Departement
from .models import DossierMedical
from .models import Patient
from .models import RendezVous
from .models import Tache


admin.site.register(Medcin)
admin.site.register(Consultation)
admin.site.register(Clinique)
admin.site.register(Departement)
admin.site.register(DossierMedical)
admin.site.register(Patient)
admin.site.register(RendezVous)
admin.site.register(Tache)