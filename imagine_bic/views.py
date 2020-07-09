from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import datetime
from .logic import *


def session_check(request):
    if len(request.session.keys()) < 0:
        print('session check')
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")
    print('session 있음')
def index(request):
    try:
        session_check(request)
        return Choose.index(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")


@csrf_exempt
def choose_lan(request):
    try:
        return Choose.choose_lan(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def choose_loc(request):
    try:
        return Choose.choose_loc(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt#,{"count":count}
def choose_shop(request):
    try:
        return Choose.choose_shop(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt#,{"count":count}
def choose_time(request):
    try:
        return Choose.choose_time(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def choose_end(request):
    try:
        return render(request, 'imagine_bic/choose_end.html')
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def signup(request):
    try:
        user_info =request.session['user_info']
        print(user_info)
        if request.method == "POST":
            return Sign.signup(request,user_info)
        if user_info == "0":
            return render(request, 'imagine_bic/signup.html')
        return render(request, 'imagine_bic/signup_company.html')
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")
 
@csrf_exempt
def signin(request):
    try:
        if request.method == "POST":
            id = request.POST['id']
            pwd = request.POST['pwd']
            return Sign.signin(request,id,pwd)
        else:
            return render(request, 'imagine_bic/login.html')
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

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
    try:
        return Choose.choose_use(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def notice(request):
    try:
        return Choose.notice(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def shop_detail(request, pk):
    try:
        return Choose.shop_detail(request,pk)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def notice_detail(request, pk):
    try:
        return Choose.notice_detail(request,pk)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def setting(request):
    try:
        return Choose.setting(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")


def setUrl(request, setUrl):
    try:
        return Choose.setUrl(request,setUrl)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def counsel(request):
    try:
        return Choose.counsel(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def write(request):
    try:
        return Choose.write(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def map(request):
    try:
        return render(request, 'imagine_bic/map.html')
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def check_list(request):
    try:
        return Choose.check_list(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def check_reservation(request, pk):
    try:
        return Choose.check_reservation(request, pk)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

@csrf_exempt
def signup_company(request):
    try:
        return Sign.signup_company(request)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def company_main(request):
    try:
        print("company_main")
        id = request.session['id']
        companys = Company.objects.filter(member_id = id)
        for company in companys:
            company_num = company.company_num
        if request.method=="POST":
            print("post")
            history_num = int(request.POST['history_num'])
            print(history_num)
            rorb = request.POST['val']
            print(rorb)
            if rorb == "r":
                print(Check.bic_return(history_num))
            elif rorb == "b":
                print(Check.bic_rent(history_num))
        historys = History.objects.filter(company_num = company_num, rtime=None)
        last_historys = History.objects.exclude(rtime = None).filter(company_num = company_num)
        print(historys)
        print("last")
        print(last_historys)
        return render(request, 'imagine_bic/company_main.html',{"companys":companys, "historys":historys, "last_historys":last_historys})
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def course(request):
    try:
        return render(request, 'imagine_bic/course.html')
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def company_check(request, pk):
    try:
        return Check.check_company(request, pk)
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def bic_rent(request):
    try:
        pk1 = int(request.POST['pk'])
        pk = Check.bic_rent(pk1)
        print(pk)
        return redirect("http://ssrocket.emirim.kr/check/company/"+pk+"/")
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def bic_return(request):
    try:
        pk1 = int(request.POST['pk'])
        pk = Check.bic_return(pk1)
        print(pk)
        return redirect("http://ssrocket.emirim.kr/check/company/"+pk+"/")
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def nearshop(request):
    try:
        return render(request, "imagine_bic/near_shop.html")
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def introduce(request):
    try:
        return render(request, "imagine_bic/introduce.html")
    except:    
        return HttpResponse("<html><script>alert('잘못된 접근입니다. 처음부터 시도해주세요');location.href='/choose_use';</script></html>")

def logout(request):
    request.session.clear()
    return redirect('choose_use')