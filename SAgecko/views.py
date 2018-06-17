from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import login,authenticate,logout,admin
#from SAgecko import forms
from gecko import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
import json

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def sa_list(request):
    sas = models.Administrators.objects.all()
    return render(request,"sa.html",{
        'sas':sas
    })

@login_required
def pm(request):
    sas = models.Administrators.objects.all()
    return render(request,"pm.html",{
        'sas':sas
                                   })
@login_required
def sys(request):
    return render(request,"sys.html")

@login_required
def permission(request):
    return render(request,"permission.html")

@login_required
def test(request):
    return render(request,"test.html")

@login_required
def ceshi(request):
    return render(request,"ceshi.html")

def acc_login(request):
    errors = {}
    if request.method == "POST":
        _username = request.POST.get("username")
        _password = request.POST.get("password")
        user = authenticate(username = _username, password = _password)
        if user:
            login(request,user)
            next_url = request.GET.get("next","/")
            return redirect(next_url)
        else:
            errors['error'] = "Wrong username or password!"
    return render(request,"login.html",{"errors":errors})

def acc_logout(request):
    logout(request)
    return redirect("/accounts/login/")

def ajax(request):
    if request.method == "POST":
        print (request.POST)
        data = {'status':0,'msg':'请求成功','data':[11,22,33]}
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('ceshi.html')

def get_sa_param(request):
    server_dic={
        'name': request.POST.get('name'),
        'qq':request.POST.get('qq'),
    }
# def host_mgr(request):
#         selected_gid = request.GET.get('selected_gid')
#       if selected_gid:
#           host_list = models.BindHostToUser.objects.filter(host_groups__id =selected_gid)
#       return render(request,"test.html")
class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message

def index2(request):
    user_list = models.Administrators.objects.all()
    try:
        if request.method == "POST":
            qq = request.POST.get('qq',None)
            name = request.POST.get('name',None)
            department = request.POST.get('department',None)
            consult_course_id = request.POST.get('consult_course_id',None)
            models.Administrators.objects.create(qq=qq,name=name,department=department,consult_course_id=consult_course_id)
            models.Administrators.objects.filter(name=name).delete()
        return render(request,"sa_add.html",{"data":user_list})
    except :
        return render(request, "sa_add.html", {"data": user_list})

def index3(request):
    user_list = models.Administrators.objects.all()
    try:
        if request.method == "POST":
            # qq = request.POST.get('qq',None)
            name = request.POST.get('name',None)
            # department = request.POST.get('department',None)
            # consult_course_id = request.POST.get('consult_course_id',None)
            models.Administrators.objects.filter(name=name).delete()
        return render(request,"sa_del.html",{"data":user_list})
    except :
        return render(request, "sa_del.html",{"data": user_list})