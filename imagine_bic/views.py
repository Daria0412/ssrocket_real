from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import datetime
from .logic import *

def index(request):
    return Choose.index(request)

@csrf_exempt
def choose_lan(request):
    return Choose.choose_lan(request)

@csrf_exempt
def choose_loc(request):
    return Choose.choose_loc(request)

@csrf_exempt#,{"count":count}
def choose_shop(request):
    return Choose.choose_shop(request)

@csrf_exempt#,{"count":count}
def choose_time(request):
    return Choose.choose_time(request)
    

def choose_end(request):
    return render(request, 'imagine_bic/choose_end.html')

@csrf_exempt
def signup(request):
    user_info =request.session['user_info']
    if request.method == "POST":
        return Sign.signup(request,user_info)
    if user_info == "0":
        return render(request, 'imagine_bic/signup.html')
    return render(request, 'imagine_bic/signup_company.html')
 
@csrf_exempt
def signin(request):
    if request.method == "POST":
        id = request.POST['id']
        pwd = request.POST['pwd']
        return Sign.signin(request,id,pwd)
    else:
        return render(request, 'imagine_bic/login.html')

def checkEmail(request):
    try:
        user = User.objects.get(id=request.GET['id'])
    except Exception as e:
        user = None

    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)

def checkEmailCp(request):
    try:
        company = Company.objects.get(id=request.GET['id'])
    except Exception as e:
        company = None

    result = {
        'result':'success',
        # 'data' : model_to_dict(user)  # console에서 확인
        'data' : "not exist" if company is None else "exist"
    }
    return JsonResponse(result)


def choose_use(request):
    return Choose.choose_use(request)

def notice(request):
    return Choose.notice(request)

@csrf_exempt
def shop_detail(request, pk):
    return Choose.shop_detail(request,pk)

def notice_detail(request, pk):
    return Choose.notice_detail(request,pk)

@csrf_exempt
def setting(request):
    return Choose.setting(request)

def setUrl(request, setUrl):
    return Choose.setUrl(request,setUrl)

@csrf_exempt
def counsel(request):
    return Choose.counsel(request)

@csrf_exempt
def write(request):
    return Choose.write(request)

def map(request):
    return render(request, 'imagine_bic/map.html')

@csrf_exempt
def check_list(request):
    return Choose.check_list(request)

@csrf_exempt
def check_reservation(request, pk):
    return Choose.check_reservation(request, pk)

@csrf_exempt
def signup_company(request):
    return Sign.signup_company(request)


def company_main(request):
    id = request.session['id']
    companys = Company.objects.filter(member_id = id)
    for company in companys:
        company_num = company.company_num
    historys = History.objects.filter(company_num = company_num)
    return render(request, 'imagine_bic/company_main.html',{"count":1,"companys":companys, "historys":historys})

def course(request):
    return render(request, 'imagine_bic/course.html')

def company_check(request, pk):
    return Check.check_company(request, pk)

def bic_rent(request):
    pk = Check.bic_rent(request)
    print(pk)
    return redirect("http://3.23.87.223:8000/check/company/"+pk+"/")

def bic_return(request):
    pk = Check.bic_return(request)
    print(pk)
    return redirect("http://3.23.87.223:8000/check/company/"+pk+"/")

