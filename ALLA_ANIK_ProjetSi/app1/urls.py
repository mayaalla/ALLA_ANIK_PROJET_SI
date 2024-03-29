from django.urls import path
from . import views
urlpatterns = [
path('', views.index1),
path('list_departement/', views.affiche_departement),
path('cardio/', views.cardiologique),
path('gerer_patient/', views.patient_afficher),
path('gerer_medcin/', views.midecin_afficher),
path('gerer_rdv/', views.rdv_afficher),
path('gerer_consultation/', views.consultation_afficher),
path('gerer_tache/', views.tache_afficher),
path('gerer_dossier/', views.dossier_afficher),
path('rechrche/', views.rechrche, name='rechrche'),
path('rechrcheP/', views.rechrcheP, name='rechrcheP'),
path('rechrcheM/', views.rechrcheM, name='rechrcheM'),
path('rechrcheR/', views.rechrcheR, name='rechrcheR'),
path('rechrcheC/', views.rechrcheC, name='rechrcheC'),
path('rechrcheT/', views.rechrcheT, name='rechrcheT'),
path('rechrcheD/', views.rechrcheD, name='rechrcheD'),
path('add/', views.add, name='ADD'),
path('addm/', views.addm, name='ADDM'),
path('addr/', views.addr, name='ADDR'),
path('addp/', views.addp, name='ADDP'),
path('addc/', views.addc, name='ADDC'),
path('addt/', views.addt, name='ADDT'),
path('addd/', views.addd, name='ADDD'),
path('editP/<int:id>', views.editP, name='EDIT'),
path('editM/<int:id>', views.editM, name='EDITM'),
path('editC/<int:id>', views.editC, name='EDITC'),
path('editR/<int:id>', views.editR, name='EDITR'),
path('editT/<int:id>', views.editT, name='EDITT'),
path('editD/<int:id>', views.editD, name='EDITD'),
path('deleteP/<int:id>', views.deleteP, name='DELETE'),
path('deleteM/<int:id>', views.deleteM, name='DELETEM'),
path('deleteC/<int:id>', views.deleteC, name='DELETEC'),
path('deleteR/<int:id>', views.deleteR, name='DELETER'),
path('deleteT/<int:id>', views.deleteT, name='DELETET'),
path('deleteD/<int:id>', views.deleteD, name='DELETED'),

]
