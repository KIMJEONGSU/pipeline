from django.urls import path
from app import views

# 라우트(=경로)에 대한 것들을 작성
urlpatterns = [
    path('',views.index),  # 첫페이지
    path('create/',views.create),  # 회원가입
    path('main_page/',views.main_page), # 메인페이지
    path('sub_page/<page_name>',views.sub_page),  # 서브페이지
    path('write_page/',views.write_page), # 글작성페이지
]
