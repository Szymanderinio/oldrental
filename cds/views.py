from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import CD, RentedCD, Song
from .forms import CDNewForm


# Create your views here.

class CDView(View):
    def get(self, request):
        cds = CD.objects.filter().order_by('band')
        return render(request, 'cds.html', {'cds': cds})


class CDNew(View):
    def post(self, request):
        cd = CDNewForm(request.POST)
        if cd.is_valid():
            cd_temp = cd.save(commit=False)
            cd_temp.save()
            return render(request, 'cd_detail.html', {'cd': cd_temp})

    def get(self, request):
        cd = CDNewForm()
        return render(request, 'cd_edit.html', {'cd': cd})


class CDDetail(View):
    def get(self, request, pk):
        cd = get_object_or_404(CD, pk=pk)
        return render(request, 'cd_detail.html', {'cd': cd})


class CDEdit(View):
    def post(self, request, pk):
        cd = get_object_or_404(CD, pk=pk)
        form = CDNewForm(request.POST, instance=cd)
        if form.is_valid():
            cd_temp = form.save(commit=False)
            cd_temp.save()
            return render(request, 'cd_detail.html', {'cd': cd_temp})

    def get(self, request, pk):
        cd = get_object_or_404(CD, pk=pk)
        form = CDNewForm(instance=cd)
        return render(request, 'cd_edit.html', {'cd': form})


class CDRemove(View):
    def get(self, request, pk):
        cd = get_object_or_404(CD, pk=pk)
        cd.delete()
        return redirect('cds')


class RentedCDView(View):
    def get(self, request):
        rentedcds = RentedCD.objects.filter().order_by('-date_to')
        return render(request, 'rentedcds.html', {'rentedcds': rentedcds})


class CDRent(View):
    def post(self, request, pk):
        cd = get_object_or_404(CD, pk=pk)
        if request.user.is_authenticated:
            cd.rent(request.user)
            cd.save()
            return render(request, 'cd_detail.html', {'cd': cd})
        else:
            return redirect('home')


class CDUnRent(View):
    def post(self, request, pk):
        cd = get_object_or_404(CD, pk=pk)
        cd.unrent()
        cd.save()
        return render(request, 'cd_detail.html', {'cd': cd})