from django.urls import path
from . import views

urlpatterns = [
    path('',views.choose_lan,name='choose_lan'),#언어 선택
    path('index/', views.index, name='index'),#유저 main
    path('index/company/',views.company_main,name = "company_main"),#회사 main
    path('index/setting/', views.setting, name='setting'),#설정 메인
    path('choose_use/',views.choose_use, name = 'choose_use'),#여행자 업체 선택
    path('choose_loc/',views.choose_loc, name='choose_loc'),#여행자 지도 5개 중 선택
    path('choose_shop/',views.choose_shop, name='choose_shop'),#회사 정보 리스트
    path('choose_shop/<int:pk>/', views.shop_detail, name='shop_detail'),#회사 상세정보
    path('choose_time/',views.choose_time, name='choose_time'),#예약 시간 선택
    path('choose_end/',views.choose_end, name='choose_end'),#예약 완료
    path('signin/',views.signin, name='signin'),#로그인
    path('signup/',views.signup, name='signup'),#사용자 로그인
    path('signup/company/',views.signup_company, name = 'signup_company'), #업체 회원가입
    path('check_email/',views.checkEmail, name='check_email'), #이메일 중복확인
    path('notice/',views.notice,name = 'notice'),#공지사항
    path('notice/<int:pk>/',views.notice_detail,name = 'notice_detail'),#공지사항 상세
    path('index/setting/<slug:setUrl>/',views.setUrl,name = 'setUrl'),#설정 클릭한 페이지로
    path('index/setting/counsel/write/',views.write,name = 'write'),#1대1 문의 글쓰기
    path('check/',views.check_list,name = "check_list"),#예약 확인 리스트
    path('check/<int:pk>/',views.check_reservation, name = "check_reservation"),#예약 바코드
    path('course/',views.course,name="course")
]