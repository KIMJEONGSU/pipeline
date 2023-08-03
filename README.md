# Django Web 구현과 데이터 파이프라인 구축

* 프로젝트 기간 : 2023.07.28 ~ 진행중
* skills : ```Python``` ```SQL``` ```Django``` ```AWS EC2``` ```?(데이터 웨어하우스)``` ```?(대시보드)```
* 기술 스택 선택 이유
  - ```Django``` 
    - 추후에 기능 확장과 빠른 개발 속도 및 안전성
    - 데이터베이스 처리, 관리자 인터페이스, 사용자 인증, URL 라우팅 등 다양한 기능을 제공.
    - 큰 커뮤니티와 풍부한 문서로 지원되어 있어서 개발자들에게 많은 도움을 제공
  - ```?(데이터웨어하우스)```
  - ```?(대시보드)```

### 프로젝트 개요
 - Django를 활용해 웹을 구현하여 웹에서 발생하는 데이터의 파이프라인을 구축해보기 위함.

### 프로젝트 수행절차
#### 제작 과정
1. 웹 서버 구축과 URL 매핑
2. 로그인, 회원가입, 게시판 기능 구현(CRUD)
3. AWS EC2를 활용하여 웹 배포
4. WSGI 서버 구축
   * 동적 페이지 요청과 파이썬 프로그램 호출을 위한 WSGI 서버 구축
   * Gunicorn 사용
5.  WSGI 서버 호출을 위한 Nginx 설치
#### 파이프라인


### 한계점 및 개선사항
* 한계점
* 개선사항
  * Django REST Framework를 사용하여 API 구축 
