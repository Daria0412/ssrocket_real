from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
import datetime
import qrcode
class Sign:
    def __init__(self):
        pass

    def signin(request, id,pwd):#로그인
        users = User.objects.filter(id = id)
        if users is not None:
            for user in users:
                if id == user.id and pwd == user.pwd:
                    request.session['id']=id
                    request.session['user_info']=user.info
                    if user.info == 0:
                        return render(request, 'imagine_bic/index.html',{"okay":1,"users":users})
                    else:
                        return redirect('/index/company/')
        else : 
            return HttpResponse("<html><script>alert('로그인 오류입니다. 다시 시도해주세요');location.href='signin';</script></html>")
        return render(request, 'imagine_bic/login.html',{"okay":1,"users":users})
    
    def signup(request,user_info): #회원가입
        id = request.POST['id']
        name = request.POST['name']
        pwd = request.POST['pwd']
        user = User.objects.create(id = id, name = name, pwd = pwd, info = user_info)
        if user_info == "0":
            return render(request, 'imagine_bic/login.html')
        request.session['id']=id
        return render(request, 'imagine_bic/signup2_company.html',{"count":1})

    def signup_company(request):
        user_info =request.session['user_info']
        id = request.session['id']
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
            request.session.clear()
            return redirect("/signin/")
        return render(request, 'imagine_bic/signup2_company.html')

class Choose:
    def __init__(self):
        pass

    def index(request):
        id = request.session['id'] 
        users = User.objects.filter(id = id)
        for user in users :
            user_info = user.info
        if user_info == 0:
            return render(request, 'imagine_bic/index.html', {'users':users,"count":1})
        return render(request, 'imagine_bic/company_main.html',{'users':users,"count":1})

    def choose_lan(request):
        if request.method == "POST":
            request.session['lan'] = request.POST['lan']
            return render(request, 'imagine_bic/choose_use.html',{"count":1})
        return render(request, 'imagine_bic/choose_lan.html')

    def choose_loc(request):
        id = request.session['id'] 
        users = User.objects.filter(id = id)
        if request.method == "POST":
            request.session['company_loc']=request.POST['search']
            return redirect('/choose_shop')
        return render(request, 'imagine_bic/choose_loc.html',{"users":users})

    def choose_shop(request):
        company_loc = request.session['company_loc'] 
        companys = Company.objects.filter(company_loc = company_loc)
        return render(request, 'imagine_bic/choose_shop.html',{"companys":companys})

    def choose_time(request):
        id = request.session['id'] 
        company_loc=request.session['company_loc']
        company_num = request.session['company_num']
        users = User.objects.filter(id = id)
        for user in users:
            name = user.name
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
            #db insert
            history = History.objects.create(company_num=company_num, member_id = id, r_btime = r_btime, r_rtime = r_rtime, reserved_At = datetime.datetime.now())
            for company in companys:
                Company.objects.update(rent_num=company.rent_num+1)
            return render(request, 'imagine_bic/choose_end.html',{"name":name,"history_num":history.history_num})
        return render(request, 'imagine_bic/choose_time.html',{"shop":shop})

    def choose_use(request):
        if request.method == "POST":
            user_info = request.POST['user_info']
            request.session['user_info'] = user_info
            return render(request, 'imagine_bic/login.html',{"count":1})
        return render(request, 'imagine_bic/choose_use.html',{"count":1})
        

    def notice(request):
        notices = Notice.objects.all().order_by('num')
        for notice in notices:
            print(notice.subject)
        return render(request, 'imagine_bic/notice.html', {'notices':notices})

    def shop_detail(request,pk):
        shop = get_object_or_404(Company, pk=pk)
        id = request.session['id']
        users = User.objects.filter(id = id)
        if request.method == "POST":
            request.session['company_num'] = pk
            return render(request, 'imagine_bic/choose_time.html', {'shop': shop,'count':1})
        return render(request, 'imagine_bic/shop_detail.html', {'shop': shop,'count':1, 'users':users})

    def notice_detail(request,pk):
        notice = get_object_or_404(Notice, pk=pk)
        return render(request, 'imagine_bic/notice_detail.html', {'notice': notice})

    def setting(request):
        user_info = request.session['user_info']
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

    def counsel(request):
        id = request.session['id']
        counsels = Counsel.objects.filter(member_id = id)
        if request.method == "POST":
            category = request.POST['category']
            request.session['category'] = category
            return render(request, 'imagine_bic/setting_write.html',{"count":1})
        return render(request, 'imagine_bic/setting_counsel.html',{"counsels":counsels,"count":1})

    def write(request):
        if request.method == "POST":
            category = request.session['category']
            id = request.session['id']
            subject = request.POST['subject']
            content = request.POST['content']
            counsel = Counsel.objects.create(member_id = id, subject = subject, content = content, regdate = datetime.datetime.now(), category = category) 
            return render(request, 'imagine_bic/setting_write.html',{"count":2})
        return render(request, 'imagine_bic/setting_write.html')

    def check_list(request):
        id = request.session['id']
        historys = History.objects.filter(member_id = id)
        return render(request, 'imagine_bic/course_rec.html',{"count":1,"historys":historys})
    
    def check_reservation(request, pk):
        id = request.session['id']
        history = get_object_or_404(History, history_num=pk)
        #qrcode 만들기
        qr = qrcode.QRCode(version = 2,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 2,border = 2)
        url = 'http://3.23.87.223:8000/check/company/'+str(pk)
        qr.add_data(url)
        qr.make()
        img = qr.make_image(fill_color="black", back_color="white")
        imgurl = "img/qrcode/check{}.png".format(str(pk))
        print(imgurl)
        img.save("imagine_bic/static/{}".format(imgurl))
        companys = Company.objects.filter(company_num = history.company_num)
        #test용
        for company in companys:
            return render(request, 'imagine_bic/reservation_check.html',{"history":history,"company":company,"imgurl":imgurl})
        #real
        if history.member_id == id:
            companys = Company.objects.filter(company_num = history.company_num)
            for company in companys:
                return render(request, 'imagine_bic/reservation_check.html',{"history":history,"company":company,"imgurl":imgurl})
        return HttpResponse("<html><script>alert('잘못된 경로입니다.');location.href='index';</script></html>")

class Check:
    def check_company(request, pk):
        history = get_object_or_404(History, history_num=pk)
        print(pk)
        print(history)
        return render(request, 'imagine_bic/company_check.html',{"history":history, "pk":pk})


    def bic_rent(request):
        pk = int(request.POST['pk'])
        History.objects.filter(history_num = pk).update(btime = datetime.datetime.now())
        return redirect("http://3.23.87.223:8000/check/company/"+str(pk)+"/")

    def bic_return(request):
        pk = int(request.POST['pk'])
        History.objects.filter(history_num = pk).update(rtime = datetime.datetime.now())
        return redirect("http://3.23.87.223:8000/check/company/"+str(pk)+"/")