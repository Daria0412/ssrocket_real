from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponse, JsonResponse
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

class Sign:
    def __init__(self):
        pass

    def signin(request, id,pwd):#로그인
        users = User.objects.filter(id = id)
        response = render(request, 'imagine_bic/signin.html',{"okay":1,"users":users})
        if users is not None:
            for user in users:
                if id == user.id and pwd == user.pwd:
                    if user.info == 0:
                        response = render(request, 'imagine_bic/main.html',{"okay":1,"users":users})
                    else:
                        response = render(request,'imagine_bic/company_main.html',{"count":2,"users":users})
                    response.set_cookie('id',id)
                    response.set_cookie('user_info',user.info)
        else : 
            response = HttpResponse("<html><script>alert('로그인 오류입니다. 다시 시도해주세요');location.href='signin';</script></html>")
        return response
    
    def signup(request,user_info): #회원가입
        Sign.trans(request)
        id = request.POST['id']
        name = request.POST['name']
        pwd = request.POST['pwd']
        user = User.objects.create(id = id, name = name, pwd = pwd, info = user_info)
        if user_info == "0":
            return render(request, 'imagine_bic/signin.html')
        response = render(request, 'imagine_bic/signup2_company.html',{"count":1})
        response.set_cookie('id',id)
        return response

    def translate(request):
        lan = request.COOKIES.get('lan')
        if lan == "":
            lan = request.POST['lan']
            request.set_cookie('lan',lan)
        if lan == 'ko' or lan == 'en' or lan == 'jp':
            if translation.LANGUAGE_SESSION_KEY in request.session:
                del(request.session[translation.LANGUAGE_SESSION_KEY])
            translation.activate(lan)
            request.session[translation.LANGUAGE_SESSION_KEY] = f'{lan}'
        else:
            if translation.LANGUAGE_SESSION_KEY in request.session:
                del(request.session[translation.LANGUAGE_SESSION_KEY])
            translation.activate('en')
            request.session[translation.LANGUAGE_SESSION_KEY] = 'ko'
    
    def trans(request):
        lan = request.COOKIES.get('lan')
        Sign.translate(request)

class Choose:
    def lan(request):
        Sign.translate(request)   
        response = render(request, 'imagine_bic/choose_use.html',{"count":1})
        return response