from django.shortcuts import render, HttpResponse

index_list = [
    {'id':1, 'index_name':'게시판작성'},
    {'id':2, 'index_name':'마이페이지'},
    {'id':3, 'index_name':'회원탈퇴'}
]

def HTMLtemplate():
    global index_list
    ol=''
    for index in index_list:
        ol+=f'''<li>
                    <a href='/sub_page/{index['index_name']}'>{index['index_name']}
                    </a>
                </li>'''
    return (f'''
            <html>
            <body>
            <h1><a href='/'>메인페이지 입니다.</a></h1>
                <ol>
                    {ol}
                </ol>
            </body>
            </html>
            ''')

# Create your views here.
def index(request):
    return HttpResponse(f'''
                        <h2>안녕하세요. 첫번째 페이지입니다.</h2>
                        <h3>아이디 : </h3>
                        <h3>비밀번호 : </h3>
                        <a href='/main_page'>로그인</a>
                        <a href='/create'>회원가입</a>
                            ''')

def create(request):
    return HttpResponse(f'''
                        <h2>회원가입 페이지입니다.</h2>
                        <h3>이름 : </h3>
                        <h3>연락처 : </h3>
                        <h3>아이디 : </h3>
                        <h3>비밀번호 : </h3>
                        <a href='/'>뒤로가기</a>
                        <a href='/'>회원가입</a>
                        ''')

def main_page(request):
    return HttpResponse(HTMLtemplate())

def sub_page(request,page_name):
    global index_list
    page = ''
    for index in index_list:
        if index['index_name'] == page_name:
            page = index['index_name']
    
    if page_name == '회원탈퇴':
        return HttpResponse(f'''
                            <h2>{page} 페이지입니다</h2>
                            <a href='/'>탈퇴하기</a>
                            ''')
    if page_name == '마이페이지':
        return HttpResponse(f'''
                            <h2>{page} 페이지입니다</h2>
                            <a href='/main_page'>뒤로가기</a>
                            <a href='/sub_page/마이페이지'>수정하기</a>
                            ''')
    if page_name == '게시판작성':
        return HttpResponse(f'''
                            <h2>{page} 페이지입니다</h2>
                            <a href='/write_page'>작성하기</a>
                            <a href='/main_page'>뒤로가기</a>
                            ''')

def write_page(request):
    return HttpResponse(f'''
                            <h2>글쓰기 페이지입니다</h2>
                            <h3>날짜 : </h3>
                            <h3>제목 : </h3>
                            <h3>내용 : </h3>
                            <a href='/sub_page/게시판작성'>뒤로가기</a>
                            <a href='/sub_page/게시판작성'>확인</a>
                            ''')