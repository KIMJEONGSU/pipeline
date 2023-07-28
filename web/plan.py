# django 선택이유 : 파이썬을 웹 서비스에 쓴다고 하면 Django 또는 flask를 쓴다고 생각하면되는데 둘의 차이는 풀스택 프레임워크(Django)냐 아니냐 정도이다.
# 추후에 기능 확장과 빠른 개발 속도 및 안전성때문에 선택.
# Django는 기본적으로 데이터베이스 처리, 관리자 인터페이스, 사용자 인증, URL 라우팅 등 다양한 기능을 제공하므로 빠르게 개발가능.
# Django의 ORM (Object-Relational Mapping)은 데이터베이스와의 상호작용을 추상화하여 데이터베이스 쿼리를 쉽게 작성할 수 있게 해줌.
# Django는 큰 커뮤니티와 풍부한 문서로 지원되어 있어서 개발자들에게 많은 도움을 제공.


# 참고 블로그
'''
https://lucky516.tistory.com/52
설치 1:pip install django

프로젝트 만들기  :django-admin startproject project
이미 프로젝트 폴더를 생성했다면 현재 프로젝트에 장고 config를 생성해주는것 django-admin startproject config . #현재폴더에 프로젝트 구성
주로 파이참쓰시는 분들이 많고 파이참에서 프로젝트를 생성한뒤 이 글을 보고계시면 아래 커맨드로 프로젝트 구성.

개발서버 시작하기
#아래 두줄이 무엇을 의미하는지는 모델 배울실 때 나옵니다.
python manage.py makemigrations
python manage.py migrate

#서버를 실행하는 커맨드 입니다
python manage.py runserver
'''

'''
MTV 모델
MTV MVC 둘이 같은개념이고 이름만 다릅니다.
Model
서버가 가지고 있는 데이터베이스 작업이라고 생각하면 됩니다.

View
브라우저 상에서 사용자에게 보여지는 페이지를 의미합니다.

Controller
Model 에다가 일을 시키는 작업. User는 뷰를 통해 컨트롤러를 실행시켜 Model에다가 작업을 요청합니다.

View와 Model의 중간다리 역할을 하는 셈이죠.
MTV               MVC
Model       <->   Model
View         <->   Template
Controller  <->    View

서버쪽 데이터베이스를 만드는것은 Model을 만든다 생각하시면 되고

웹페이지 화면을 만든다 하면 Template를 만든다 생각하시면 되고

템플릿에서 서버에 일을 시키는건 View를 만든다 생각하시면 됩니다
'''

'''
application만들기
Django에서는 어플리케이션 단위로 웹페이지를 개발
이 application기능은 프로젝트 폴더에 넣었다 뺐다 할 수 있어서 개발속도 향상에 아주 큰 도움을 줍니다.

원하는 기능이 있으면 처음부터 구현하기보단 구글링에 찾아서 꽂아 넣고 커스텀만 하면 되니깐요!
python manage.py startapp login
view.py파일에 클라이언트에게 보여질 화면 구성.
urls.py파일 생성 후 프로젝트를 끼워넣기
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

project.urls.py파일에 만든 app을 연결시켜준다.
'''

'''
model 생성 후 애플리케이션의 모델도 프로젝트 모델 스키마에 연결해줘야함.
login/settiongs.py->INSTALLED_APPS 에다가 애플리케이션 등록.
이때 이름은 login.apps.py에서 확인가능하다.
애플리케이션 등록 후 Migration해야함.
Migration이란 아까 말씀드린것 처럼 기존에 있던 프로젝트의 데이터베이스 모델에 application의 데이터베이스 모델을 이식시키는 과정
makemigrations 커맨드는 application에서 model의 수정사항을 기록
--------
makemigrations는 여러분의 application의 model의 model에 대한 변화를 기록합니다.

migrate는 makemigrations의 변화 기록을 참고하여 실제로 프로젝트 모델 스키마에 application의 모델 변화사항을 반영해주는 커맨드
'''

'''
어드민페이지 생성.
모델에 데이터를 추가하는 방법은 여러가지가 있다.
Django의 장점은 이 admin페이지를 기본적으로 제공해준다는 점
1. 웹페이지상 view에서 model에 데이터베이스 추가하도록 요청하는 기능 구현

2. 서버 개발자가 admin페이지에서 직접 데이터 추가

3. 서버 개발자가 django shell을 이용해서 직접 데이터 추가
'''