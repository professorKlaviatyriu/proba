from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from django.db.models import Q
from .models import *
from .urlls import *
from .forms import *


# сылка чтобы видна табла
# Create your views here.
def lawyers_list(request):
    lawyers = Lawyer.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        lawyers = Lawyer.objects.filter(Q(name__contains=search_query) | Q(body__contains=search_query))
    else:
        lawyers = Lawyer.objects.all()

    return render(request, 'lawyer/index.html', context={'lawyers': lawyers})


class LawyerCreate(ObjectCreateMixin, View):
    model_form = LawyerForm
    template = 'lawyer/lawyer_create.html'


class LawyerUpdate(ObjectUpdateMixin, View):
    model = Lawyer
    model_form = LawyerForm
    template = 'lawyer/lawyer_update.html'


class LawyerDelete(ObjectDeleteMixin, View):
    model = Lawyer
    template = 'lawyer/lawyer_delete.html'
    redirect_url = 'lawyer/lawyer_detail.html'


class LawyerDetail(ObjectDetailMixin, View):
    model = Lawyer
    template = 'lawyer/lawyer_detail.html'


def timetables_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'lawyer/timetables_list.html', context={'timetables': timetables})


class TimetableCreate(ObjectCreateMixin, View):
    model_form = TimetableForm
    template = 'lawyer/timetable_create.html'


class TimetableUpdate(ObjectUpdateMixin, View):
    model = Timetable
    model_form = TimetableForm
    template = 'lawyer/timetable_update.html'


class TimetableDelete(ObjectDeleteMixin, View):
    model = Timetable
    template = 'lawyer/timetable_delete.html'
    redirect_url = 'lawyer_detail.html'


class TimetableDetail(ObjectDetailMixin, View):
    model = Timetable
    template = 'lawyer/timetable_detail.html'


def cantors_list(request):
    cantors = Cantor.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        cantors = Cantor.objects.filter(Q(name__contains=search_query) | Q(body__contains=search_query))
    else:
        cantors = Cantor.objects.all()
    return render(request, 'lawyer/cantors_list.html', context={'cantors': cantors})


class CantorCreate(ObjectCreateMixin, View):
    model_form = CantorForm
    template = 'lawyer/cantor_create.html'


class CantorUpdate(ObjectUpdateMixin, View):
    model = Cantor
    model_form = CantorForm
    template = 'lawyer/cantor_update.html'


class CantorDelete(ObjectDeleteMixin, View):
    model = Cantor
    template = 'lawyer/cantor_delete.html'
    redirect_url = 'cantor_detail.html'


class CantorDetail(ObjectDetailMixin, View):
    model = Cantor
    template = 'lawyer/cantor_detail.html'


def klients_list(request):
    klients = Klient.objects.all()
    return render(request, 'lawyer/klients_list.html', context={'klients': klients})


class KlientCreate(ObjectCreateMixin, View):
    model_form = KlientForm
    template = 'lawyer/klient_create.html'


class KlientUpdate(ObjectUpdateMixin, View):
    model = Klient
    model_form = KlientForm
    template = 'lawyer/klient_update.html'


class KlientDelete(ObjectDeleteMixin, View):
    model = Klient
    template = 'lawyer/klient_delete.html'
    redirect_url = 'klient_detail.html'


class KlientDetail(ObjectDetailMixin, View):
    model = Klient
    template = 'lawyer/klient_detail.html'
