from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
import datetime
from .logic import *


# # 번역 함수
# # lan = request.COOKIES.get('lan') 뒤에 호출해서 사용 (두 개 세트로 사용해야 함)
# def translate(request, lan):
#     if lan == 'ko' or lan == 'en' or lan == 'jp':
#         if translation.LANGUAGE_SESSION_KEY in request.session:
#             del(request.session[translation.LANGUAGE_SESSION_KEY])
#         translation.activate(lan)
#         request.session[translation.LANGUAGE_SESSION_KEY] = f'{lan}'
#     else:
#         if translation.LANGUAGE_SESSION_KEY in request.session:
#             del(request.session[translation.LANGUAGE_SESSION_KEY])
#         translation.activate('en')
#         request.session[translation.LANGUAGE_SESSION_KEY] = 'ko'

def index(request):
    lan = request.COOKIES.get('lan')
    Sign.translate(request)
    id = request.COOKIES.get('id') 
    users = User.objects.filter(id = id)
    for user in users :
        user_info = user.info
    if user_info == 0:
        print("이 유저는 여행자")
        response = render(request, 'imagine_bic/index.html', {'users':users,"count":1})
        response.set_cookie('id',id)
        return response
    return render(request, 'imagine_bic/company_main.html',{'users':users,"count":1})

@csrf_exempt
def choose_lan(request):
    if request.method == "POST":
        return Choose.lan(request)
    return render(request, 'imagine_bic/choose_lan.html')

@csrf_exempt
def choose_loc(request):
    id = request.COOKIES.get('id') 
    users = User.objects.filter(id = id)
    if request.method == "POST":
        response = render(request, 'imagine_bic/choose_shop.html',{"count":1})
        response.set_cookie('company_loc',request.POST['company_loc'])
        response.set_cookie('id',id)
        return response
    return render(request, 'imagine_bic/choose_loc.html',{"users":users})

@csrf_exempt#,{"count":count}
def choose_shop(request):
    company_loc = request.COOKIES.get('company_loc') 
    companys = Company.objects.filter(company_loc = company_loc)
    return render(request, 'imagine_bic/choose_shop.html',{"companys":companys})

@csrf_exempt#,{"count":count}
def choose_time(request):
    print(request.COOKIES)
    id = request.COOKIES.get('id') 
    company_loc=request.COOKIES.get('company_loc')
    company_num = request.COOKIES.get('company_num')
    users = User.objects.filter(id = id)
    for user in users:
        name = user.name
    print(company_num)
    print(company_loc)
    companys = Company.objects.filter(company_num = company_num)
    for company in companys:
        shop = company
    if request.method == "POST":
        print("post")
        r_year = request.POST['r_year']
        r_month = request.POST['r_month']
        r_date = request.POST['r_date']
        r_b = request.POST['r_btime']
        r_r = request.POST['r_rtime']
        r_btime = "{}-{}-{} {}".format(r_year,r_month,r_date,r_b)#datetime formatting
        r_rtime = "{}-{}-{} {}".format(r_year,r_month,r_date,r_r)
        btime = "1970-01-02 00:00:00"
        rtime = "1970-01-02 00:00:00"
        #db insert
        history = History.objects.create(company_num=company_num, member_id = id, r_btime = r_btime, r_rtime = r_rtime, reserved_At = datetime.datetime.now(), btime =btime, rtime = rtime)
        response = render(request, 'imagine_bic/choose_end.html',{"name":name,"history_num":history.history_num})
        for company in companys:
            Company.objects.update(rent_num=company.rent_num+1)
        return response
    print(shop)
    return render(request, 'imagine_bic/choose_time.html',{"shop":shop})

def choose_end(request):
    return render(request, 'imagine_bic/choose_end.html')

@csrf_exempt
def signup(request):
    user_info =request.COOKIES.get('user_info')
    if request.method == "POST":
        # lan = request.COOKIES.get('lan')
        # translate(request, lan)
        return Sign.signup(request,user_info)
    if user_info == "0":
        return render(request, 'imagine_bic/signup.html')
    return render(request, 'imagine_bic/signup_company.html')
 
@csrf_exempt
def signin(request):
    if request.method == "POST":
        lan = request.COOKIES.get('lan')
        Sign.translate(request)
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


def choose_use(request):
    if request.method == "POST":
        user_info = request.POST['user_info']
        response = render(requset, 'imagine_bic/choose_use.html')
        response.set_cookie("user_info",user_info)
        return response
    return render(request, 'imagine_bic/choose_use.html',{"count":1})

def notice(request):
    notices = Notice.objects.all().order_by('num')
    for notice in notices:
        print(notice.subject)
    return render(request, 'imagine_bic/notice.html', {'notices':notices})

@csrf_exempt
def shop_detail(request, pk):
    shop = get_object_or_404(Company, pk=pk)
    id = request.COOKIES.get('id') 
    users = User.objects.filter(id = id)
    if request.method == "POST":
        response = render(request, 'imagine_bic/choose_time.html', {'shop': shop,'count':1})
        response.set_cookie('company_num',pk)
        print(response.cookies)
        print(pk)
        return response
    return render(request, 'imagine_bic/shop_detail.html', {'shop': shop,'count':1, 'users':users})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'imagine_bic/notice_detail.html', {'notice': notice})

@csrf_exempt
def setting(request):
    user_info = request.COOKIES.get('user_info')
    if request.method == "POST":
        return render(request, 'imagine_bic/setting_'+request.POST['setUrl']+".html", {"count":1,"user_info":user_info})
    return render(request, 'imagine_bic/setting.html',{"user_info":user_info})

def setUrl(request, setUrl):
    html = ""
    if setUrl == "" :
        html ='imagine_bic/setting.html'
    elif setUrl == "modify":
        html ='imagine_bic/setting_modify.html'
    elif setUrl == "secession":
        html = 'imagine_bic/setting_secession.html'
    elif setUrl == "counsel":
        html = 'imagine_bic/setting_counsel.html'
    elif setUrl == "logout":
        html = 'imagine_bic/setting_logout.html'
    print(html)
    return render(request, html)

@csrf_exempt
def counsel(request):
    id = request.COOKIES.get('id')
    counsels = Counsel.objects.filter(member_id = id)
    if request.method == "POST":
        category = request.POST['category']
        response = render(request, 'imagine_bic/setting_write.html',{"count":1})
        response.set_cookie("category",category)
        return response
    return render(request, 'imagine_bic/setting_counsel.html',{"counsels":counsels,"count":1})

@csrf_exempt
def write(request):
    if request.method == "POST":
        category = request.COOKIES.get('category')
        id = request.COOKIES.get('id')
        subject = request.POST['subject']
        content = request.POST['content']
        counsel = Counsel.objects.create(member_id = id, subject = subject, content = content, regdate = datetime.datetime.now(), category = category)
        response = render(request, 'imagine_bic/setting_write.html',{"count":2})
        return response
    return render(request, 'imagine_bic/setting_write.html')

def map(request):
    return render(request, 'imagine_bic/map.html')

@csrf_exempt
def check_list(request):
    id = request.COOKIES.get('id')
    historys = History.objects.filter(member_id = id)
    return render(request, 'imagine_bic/course_rec.html',{"count":1,"historys":historys})

@csrf_exempt
def check_reservation(request, pk):
    id = request.COOKIES.get('id')
    history = get_object_or_404(History, history_num=pk)
    if history.member_id == id:
        companys = Company.objects.filter(company_num = history.company_num)
        for company in companys:
            return render(request, 'imagine_bic/reservation_check.html',{"history":history,"company":company})
    return HttpResponse("<html><script>alert('잘못된 경로입니다.');location.href='index';</script></html>")


def choose_use(request):
    if request.method == "POST":
        user_info = request.POST['user_info']
        response = render(request, 'imagine_bic/login.html',{"count":1})
        response.set_cookie('user_info',user_info)
        return response
    return render(request, 'imagine_bic/choose_use.html',{"count":1})


@csrf_exempt
def signup_company(request):
    user_info =request.COOKIES.get('user_info')
    id = request.COOKIES.get('id')
    users = User.objects.filter(id = id)
    for user in users:
        name = user.name
    if request.method == "POST":
        company_addr = request.POST['company_addr']
        company_loc = request.POST['company_loc']
        company_phone = request.POST['company_phone']
        bicycle_num = request.POST['bicycle_num']
        s_business = request.POST['s_business']
        e_business = request.POST['e_business']
        company_info = request.POST['company_info']
        company = Company.objects.create(member_name = name, company_addr = company_addr,company_phone=company_phone,bicycle_num=bicycle_num,member_id=id, s_business=s_business,e_business=e_business,company_info=company_info,company_loc=company_loc,rent_num=0)
        response = render(request, 'imagine_bic/login.html',{"count":1})
        response.delete_cookie('id')
        return response
    return render(request, 'imagine_bic/signup2_company.html')


def company_main(request):
    id = request.COOKIES.get('id')
    users = User.objects.filter(id = id)
    return render(request, 'imagine_bic/company_main.html',{"count":1,"users":users})

def course(request):
    return render(request, 'imagine_bic/course.html')
