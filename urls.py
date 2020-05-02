from django.urls import path
from .views import *

# урлы для откр
urlpatterns = [
    path('', lawyers_list, name='lawyers_list_url'),
    path('lawyer/create/', LawyerCreate.as_view(), name='lawyer_create_url'),
    path('lawyer/<str:slug>/', LawyerDetail.as_view(), name='lawyer_detail_url'),
    path('lawyer/<str:slug>/update', LawyerUpdate.as_view(), name='lawyer_upgrade_url'),
    path('lawyer/<str:slug>/delete', LawyerDelete.as_view(), name='lawyer_delete_url'),
    path('timetables/', timetables_list, name='timetables_list_url'),
    path('timetable/create/', TimetableCreate.as_view(), name='timetable_create_url'),
    path('timetable/<str:slug>/', TimetableDetail.as_view(), name='timetable_detail_url'),
    path('timetable/<str:slug>/update/', TimetableUpdate.as_view(), name='timetable_update_url'),
    path('timetable/<str:slug>/delete/', TimetableDelete.as_view(), name='timetable_delete_url'),
    path('cantors', cantors_list, name='cantors_list_url'),
    path('cantors/create/', CantorCreate.as_view(), name='cantor_create_url'),
    path('cantors/<str:slug>/', CantorDetail.as_view(), name='cantor_detail_url'),
    path('cantors/<str:slug>/update/', CantorUpdate.as_view(), name='cantor_upgrade_url'),
    path('cantors/<str:slug>/delete/', CantorDelete.as_view(), name='cantor_delete_url'),
    path('klients/', klients_list, name='klients_list_url'),
    path('klients/create/', KlientCreate.as_view(), name='klient_create_url'),
    path('klients/<str:slug>/', KlientDetail.as_view(), name='klient_detail_url'),
    path('klients/<str:slug>/update/', KlientUpdate.as_view(), name='klient_update_url'),
    path('klients/<str:slug>/delete/', KlientDelete.as_view(), name='klient_delete_url'),

]
