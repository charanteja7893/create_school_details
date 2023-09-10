from django.shortcuts import render

# Create your views here.
from app.models import*
from django.http import HttpResponse
def create_school(request):
    if request.method=='POST':
        scn=request.POST['scn']
        sp=request.POST['sp']
        sl=request.POST['sl']

        SO=school.objects.get_or_create(scname=scn,scprincipal=sp,sclocation=sl)[0]
        SO.save()
        QLSO=school.objects.all()
        d={'QLSO':QLSO}
        return render(request,'displayschool.html',d)
    return render(request,'school.html')

