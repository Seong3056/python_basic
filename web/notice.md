ORM(Object-relation mapping, 객체 관계 매핑)
- 데이터베이스의 데이터를 객체와 연결해주는 기능
- Model클래스는 데이터베이스의 테이블의 형태를 나타냄
- Model클래스를 통해 데이터를 가져올 때는 모델의 objects속성을 사용

-전체 데이터목록 가져오기
    - 모델.objects.all()

- 특정 조건을 만족하는 데이터 한 개의 정보를 가져오기
    - 모델.objects.get(조건)

-특정 조건을 만족하는 데이터들의 정보 가져오기
    - 모델.objects.filter(조건)

웹에서 데이터를 전송하는 방법
- GET
- 서버에 보낼 데이터가 공개되어도 상관없는 경우

- POST
- 요청 자체에 데이터를 담아 보내며, 외부에 노출되어서는 안되는 비밀값을 사용할 때 주로 사용

정적 파일(static files)
- 사전적으로는 변화가 없는 파일
- 웹프레임워크에서 정적파일이란 프레임워크의 소스코드를 제외한 나머지 이미지, 동영상, CSS, JavaScript 파일등
- 소스코드는 일반적으로 동적인 결과물을 만들어내는데 사용
정적 파일은 사용자에게 변형 없이 언제나 동일한 형태로 제공됨

템플릿에서 정적파일 사용
    - 템플릿에서 정적파일을 불러올 때는
    - `{% static '정적파일경로' %}`

유저가 업로드하는 정적파일

정적파일의 분류
- Django에서 정적파일은 두 가지로 나뉨
    - 소스코드에 포함되는 정적파일
    - 유저가 업로드하는 정적파일

- 이전에 정적파일을 넣어뒀던 디렉터리는 소스코드에 포함되는 정적파일을 두는 곳
    - 프로젝트의 일부분으로 취급됨

- 유저가 업로드하는 정적파일은 프로젝트에 포함되지 않음
    - 블로그라는 전체 프로젝트와는 별개로 블로그를 사용하는 사용자들이 업로드하는 글에 포함된 이미지와 같은 데이터

유저가 업로드하는 정적파일 설정
- setting.py에서 소스코드에 포함되는 정적파일의 설정은 STATIC_ 로 시작하고, 유저가 업로드하는 정적파일 설정은 MEDIA_ 로 시작함

- MEDIA_URL
    - 유저가 업로드한 파일에 접근할 수 있도록 브라우저에 제공하는 경로 접두어
    - 소스코드에 포함되는 정적파일은 STATIC_URL 이라는 설정값을 사용하며, 기본값은 "/static/"

- MEDIA_ROOT
    - 실제로 유저가 업로드한 파일이 저장될 경로

동적 URL 경로
"posts/<int:post_id>/"
┗ int : 정수 형태의 값을 받도록 제한한다는 의미
┗ post_id : <와> 사이의 영역이 post_id라는 이름을 가진다는 의미

사용자의 입력을 받는 Template
- HTML에서 사용자의 입력을 받는 요소는
    - 입력에 대한 제목: <label>
    - 한 줄 짜리 텍스트 입력: <input type='text'>
    - 여러 줄 텍스트 입력: <textarea>
    - 버튼: <button>

- 사용자의 입력을 받는 요소는 form태그로 감싼다.
- div로 각각의 입력할 항목들을 감싸고, 내부에 label로 해당 항목의 이름을 표시

POST 요청에 대한 Forbidden 오류
- 403 Forbidden: 요청은 받았으나 그요청을 처리할 권한이 없기 때문에 서버에서 거부함

- CSRF 공격
    - CSRF 인증에 실패하여 요청이 중단됨
    - CSRF: Cross-Site-Request-Forgery (사이트간 요청 위조)

- Django에서 처리하는 GET과 POST 요청 
    - 지금까지 CSRF 인증오류가 발생하지 않은 이유는 Django가 데이터를 처리하는 방식이 GET/POST에 따라 다르기 때문
    - GET은 사이트의 특정페이지에 접속하거나, 검색을 하는 등의 읽기/조회 행동을 
        
    - -수행하는데 쓰임브라우저별로 구분되는 값은 서버에 저장되므로 브라우저를 이용하는 사람(이용자또는 해커)은 그값을 알 수 없음
    - 3. POST요청을 하는 form이 브라우저별로 구분되는 값을 가지지 않는다면 요청 거부
    - POST는 사이트의 특정 데이터를 변경/작성하는데 쓰임
    - 따라서 Django는 POST 요청에 대해서 GET요청초바 더높은 보안수준을 적용

- Django의 CSRF 공격 방어기법
    - CSRF 공격 방어의 핵심은 로그인한 사용자가 의도하지 않은 POST요청을 거부하는것
        - 1. Django는 새로운 요청을 하는 브라우저마다 구분되는 값을 서버에 저장
        - 2. POST요청을 하는 form이 브라우저별로 구분되는 값을 가지지 않는다면 요청 거부        
    - 브라우저별로 구분되는 값은 서버에 저장되므로 브라우저를 이용하는 사람(이용자또는 해커)은 그값을 알 수 없음
        - 3. Template 파일에서 {% csrf_token %} 태그를 사용하면 이 영역은 브라우저별로 구분되는 값으로 치환됨

POST 데이터를 사용한 DB row 생성
- ORM을 사용해서 DB에서 데이터를 생성할 때는 create 메서드를 사용
    - create_instance = 모델.objects.create(필드명=필드값)

댓글작성
- 글 작성과의 차이점
    - 제목이 없음
    - 작성한 댓글이 반드시 어떤 글(Post)에 소속되어야 함

글 작성 시 이미지 업로드
- Post 모델에는 썸네일을 다루는 이미지 필드가 있음
- 텍스트와 다르게 이미지와 같은 파일을 form으로 전달받으려면 별도의 처리가 필요
- 파일을 첨부할 때는 <input type="file">태그를 사용

- 파일을 전송해야하는 form에는 enctype="multipart/form-data"속성을 추가해야함
    - enctype 속성은 데이터를 서버로 전송할 때 어떤 인코딩 유형을 쓸 것인지 나타냄
    - 인코딩은 form에 추가한데이터를 어떤 방식으로 변환 시킬 것인지 정하는 규격
    - form에 별도로 enctype을 지정하지 않는다면 텍스트 데이터만 보낼 수 있음

    - view에서 POST메서드로 전달받은 데이터는 request.POST에서 가져옴
    - 전송된 파일은 request.FILES 에서 가져와야함

인증 시스템
- 회원가입, 로그인과 같은 사용자 정보를 활용하는 기능을 통틀어 인증 시스템(Authentication system)이라 부름

- CustomUser
    - django는 기본적으로 로그인을 처리할 수 있는 기본 User 모델을 지원함
        - 기본 User모델은 ID와 비밀번호, 이름과 같은 최소한의 정보만을 지원
        - 사용자 모델에 추가 정보를 저장하고 싶다면 별도의 User모델을 구성해야함

- AbstractUser : Django가 CustomUser 모델을 만들기 위해 제공하는 기본 유저의 형태를 가진 모델클래스
    - AbstractUser를 상속받으면 자동으로 다음 필드들이 모델에 추가됨
        - username: 사용자명, 로그인 할 때의 아이디
        - password: 비밀번호
        - first_name: 이름
        - last_name: 성
        - email: 이메일
        - is_staff: 관리자 여부
        - is_activate: 활성화 여부
        - data_joined: 가입일시
        - last_login: 마지막 로그인일시
- 커스텀 유저 모델을 사용하는 경우, 어떤 모델을 User 모델로 사용하는지 setting.py에 정의해야함

CustomUser에 필드 추가
- CustomUser에 프로필이미지와 소개글 필드를 추가

로그인/피드 페이지 기본 구조
- pystagram에 접속 시, 로그인 중이라면 바로 피드 페이지가 나타남
- 로그인되지 않았거나 처음 접속한 경우에는 로그인 페이지로 이동

- 아래 두 가지 조건에 맞도록 view에서 동작을 제어해야함
    - 이미 사용자가 브라우저에서 로그인을 했다면
        - 피드(새 글 목록) 페이지를 보여줌
    
    - 사용자가 로그인한 적이 없다면(또는 로그아웃을 했다면)
        - 로그인 페이지를 보여줌

page not found(404)에러
- 페이지를 찾을 수 없다는 에러
- 요청한 URL에 대한 페이지를 찾을 수 없다는 응답 코드
- URL을 해석할 때 매칭되는 패턴을 찾지 못했을 때 발생

현재 정의된 URL들은
1. "admin/"으로 시작하는 URL -> 관리자 페이지
2. 공백문자열 -> index view
3. "media/"로 시작하는 URL -> 사용자가 업로드한 정적파일
- 새로 추가한 user/urls.py 에 정의한 URL은 여기에 나타나지않음
    - urls.py 는 RootURLconf에 등록해야함

pystagram/urls.py 에서 사용된 include 함수는 users/ 로 시작하는 URL을 users/urls.py 에서 처리하게 되며, 127.0.0.1:8000/users/login URL은 다음의 과정을 거쳐 view에 전달됨
1. pystagram/urls.py
    - /users/ 로 시작하는 URL을 users/urls.py로 전달

2. users/urls.py
    - 나머지 login/ 부분을 login_view로 전달

3. urls에서 전달해준 요청을 view가 처리

로그인 여부에 따른 접속제한
- 로그인 여부에 따라 동작을 구분하려면 요청을 보낸 사용자의 정보가 필요
- View 함수에 전달된 요청(request)에서 사용자 정보는 request.user 속성으로 가져올 수 있으며, 가져온 request.user가 로그인된 사용자인지 여부는 is_authenticated 속성으로 확인할 수 있음

LoginFrom 인스턴스 생성에 딕셔너리를 전달하면 Form 클래스는 정의된 필드들에 올바른 값이 들어왔는지, 제약조건을 지킨 데이터가 들어왔는지를 검사
- is_valid 메서드를 호출할 때 이 검사가 실행되며, 검사 결과가 올바른지를 True/False로 return해줌

- 전달된 데이터를 검증하는 것 외에도, Form 클래스는 Template에서 input 요소를 생성하는 기능도 수행

Form 은 Template에 input 요소들을 생성할 때와 자신에게 전달된 데이터를 검증할 때 사용

- 일반적으로 data가 없이 생성된 , Form은 Template에 form 정보를 전달하기 위해 사용
- data인수를 채운채 생성도니 Form은 해당 data의 유효성을 검증하기 위해 사용

Form.is_valid
- is_valid 메서드를 실행하기 전에는 form의 cleaned_data 에 접근할 수 없음
- Form 클래스를 사용해 데이터를 받았다면 반드시 is_valid를 호출해야함

authenticate
- 주어진 값에 해당하는 사용자가 있는지 판단
- username과 password에 해당하는 사용자가 있다면 함수의 실행결과로 User 인스턴스가 반환되며, 없다면 반환되지않음

- authenticate 함수의 실행결과가 User 객체라면 입력한 값(credentials; 자격즉명)에 해당하는 사용자가 리턴

login 
- 브라우저에 해당 사용자를 유지시켜주는 기능
- authenticate가 단순 입력한 username/password 에 해당하는 사용자가 있는지 검사하고 User 객체를 되돌려 준다면, login 함수는 우리가 웹사이트에 로그인했다면 기대하는 로그인 상태로 변환 및 유지 기능을 담당
    - login함수 호출에는 현재 요청(request) 객체와 사용자(User)객체가 필요

로그아웃 구현 및 로그인 개선
- 로그아우승ㄴ 로그인과 달리 입력값을 받지 않으므로 Template 없이 View만으로 구현할 수 있음

- 로그아웃 기본 구조
    - View : logout_view
    - URL : 127.0.0.1:8000/users/logout/
    - Template : 없음

회원가입
- 회원가입은 Post 객체를 만드는 글쓰기와 유사하게 입력받은 정보로 User 객체를 만드는 작업
    - 다만, User 객체는 다른 일반적은 Model 클래스와는 다른 특징들을 갖고 있어, 몇가지 더 고려할 사항들이 있음

- 회원가입 기본 구조
    - View : signup
    - Url : 127.0.0.1:8000/users/signup/
    - Template : templates/users/signup.html

- Django는 User의 비밀번호를 변형해서 저장함
    - 사용자가 입력한 비밀번호를 암호화하지않고 DB에 저장하는 것은 보안에도 문제가 있고, 대한민국 개인정보 보호법 위반이다.
- Django의 User 모델에는 비밀번호를 변형해서 저장하는 기능이 내장되어 있음
    - 사용자 정보는 create_user() 메서드를 사용함

User 생성하기
- User를 생성할 때는 몇 가지 고려해야할 사항이 있음
    1. 비밀번호와 비밀번호 확인의 값이 같아야함
    2. 같은 사용자명을 사용하는 User는 생성불가 및 오류전달

SignupForm 내부에서 데이터 유효성 검사
- Form 클래스는 기본적으로 탑재된 유효성 검사 외에 추가적인 검사를 하도록 커스텀마이징 할 수 있음
    - 회원가입시 입력받는 데이터는 username과 password1, password2 이 데이터에 대한 데이터 검증이 필요

- 하나의 필드에 대한 유효성 검사는 clean_{필드명} 메서드가 담당
- Form에 전달된 전체 data에 대한 유효성 검사는 clean 메서드가 담당
    - 예) 하나의 필드인 username은 clean_username 메서드에 검증 로직을 작성
    - 예) 비밀번호는 두 개의 필드 내용을 동시에 사용해야 하므로(password1, password2) 하나의 필드 데이터만 가지고 검증할 수 없음 이때는 전체 데이터를 사용할 수 있는 clean 메서드를 사용

- clean_username은 SignipForm 에 전달된 username 키에 해당하는 값을 검증할 때 사용됨
    - 검증하려는 필드 데이터에 접근할 때는 self.clean_data["필드명"]에서 값을 가져옴
    - 이 값을 사용할 수 있다면 함수에서 return 해주고, 유효하지 않다면 ValidationError를 발생시킴
    - clean_username 에서 ValidationError 를 발생시키는 것은 Form.add_error("username", {입력한 에러메시지})를 호출하는것과 같음    

- 두 개 이상의 필드값을 동시에 비교해야 할 때는 전체 데이터의 검증을 수행하는 clean 메서드 내부에 로직을 구현
- clean_{필드명} 메서드와는 달리, clean 메서드는 마지막에 값을 리턴하지 않아도 됨

Template을 확장하는 {% extends %} 태그
- {% extends "템플릿 경로" %} 태그는 입력한 경로의 template를 기반으로 새 Template 생성

- 공통되는 부분은 남겨두고, Template마다 변경되는 부분은 {% block content %}{% endblock %}으로 치환
    - {% block %} 영역은 이 Template을 확장하는 하위 템플릿에서 변경 가능한부분
    - base.html에는 하나의 block 밖에 없으므로, base.html을 확장(extends)하는 하위 Template 들은 content block 내의 영역만 편집가능하며 나머지 부분은 base.html의 변경사항을 따라가게 됨

- content block 내부를 채우려면 
    {% block content %}로 블록 영역이 시작함을 알리고
    {% endblock %}으로 영역이 끝났음을 선언해주어야 함

댓글 작성
- 블로그 프로젝트에서는 목록 화면에서는 댓글을 보여주기만 하며, 댓글 작성은 글 내부에서만 가능했지만 피드페이지에서는 댓글 달기 기능을 한화면에서 각 post마다 구현해야함

- 사용자의 입력을 받는 input을 직접 만들수도 있지만 Form 클래스를 사용하는 것이 Django의 기본규칙
- 이전까지는 forms.Form 클래스를 사용했지만 ModelForm 클래스를 사용하면 DB테이블에 해당하는 모델 클래스와 연관된 기능들을 제공함

    - Django 모델에 있는 필드인 models.CharField()나 models.integerField()는 ModelForm 에서 forms.CharField()나 forms.IntegerField() 와 같은 Form에서 사용하는 Field로 자동 변환됨

- ModelForm 인스턴스에서 save()를 호출하면 전달받은 데이터를 사용해서 지정된 모델 인스턴스를 생성
    - 오류가 발생
    - 발생한 오류는 posts_comment 테이블의 post_id 는 NULL을 허용하지 않는다는 메시지

    - 오류 해결 방법은 두 가지
        - 1. CommentForm 으로 Comment 객체를 만들되, 메모리상에 객체를 만들고 필요한 데이터를 나중에 채우기
        - 2. CommentForm에 NULL을 허용하지 않는 모든 필드를 선언하고, 인스턴스 생성 시 유효한 데이터를 전달

ModelForm에 모든 필드를 지정하면 별도의 작업 없이 save()만 호출하면 새 모델 인스턴스가 생기므로 fields 리스트에 모든 필드를 지정하는게 맞다고 생각할 수 있음
- 하지만 Form에서 전달받은 데이터는 **사용자가 입력한 데이터**임

Comment를 생성하기 위해 필요한 데이터는 3가지
1. 어떤 글의 댓글인지(Post)
2. 어떤 사용자의 댓글인지(User)
3. 어떤 내용을 가지고 있는지(Content)
- 여기서 사용자가 입력하는 데이터는 1번과 3번
- 어떤 사용자가 댓글을 생성했는지는 사용자가 입력한 데이터에 있으면 안되는 값이며, 시스템에서 자동으로 입력되어야 함

-> 그러므로 CommentForm은 post와 content만을 전달받은 값으로 지정해야하며, 작성자 정보인 user는 시스템에서 채워야함

댓글 작성 처리를 위한 view 구현
- 지금까지는 form을 사용한 POST 요청으로 받은 데이터를 같은 페이지에서 처리했음
- 많은 역할을 하나의 View에서 처리하게 되면 코드를 유지보수하기 어려워짐
- 댓글 작성 form에서 전송한 데이터는 별도의 댓글작성 View에서 처리

View에 require_POST 데코레이터를 사용하면 오로지 POST 유형의 요청만 처리하며, 이 외의 유형의 요청에는 405 Method Not Allowed 응답을 돌려줌

지금까지 form 태그에서 지정해본 속성값
- method: GET과 POST중 어떤 방식으로 데이터를 전달할지
- enctype: 기본값과 파일 전송을 위한 값 중 선택

- 이번에 사용할 속성값은 action
    - action: 이 form의 요청을 어디로 보낼지를 지정
        - 비어있는 경우에는 현재 브라우저의 URL을 사용

작성 완료 후 원하는 Post위치로 이동
- 글에 댓글을 추가한 후, 피드 페이지의 최상단이 아니라 댓글을 추가한 글로 돌아올 수 있도록 구현
    - HTML 요소의 id속성을 활용할 수 있음

URL 뒤에 #(HTML 요소의 id)를 입력하면, 그 id를 가진 요소의 위치로 이동하게됨

글의 댓글 수 표시
- Post에 몇 개의 Comment가 연결되었는지 표시
- 연결된 객체의 정보가 전부 필요하지않고 단순히 개수만 필요하다면 QuerySet의 count 메서드를 사용하면 좋음

댓글 삭제
- 삭제할 댓글의 id정보를 받고, 받은 id에 해당하는 Comment 객체를 delete 메서드로 삭제
    - 댓글 삭제는 DB의 내용을수정하는 명령이므로 method가 POST일 때만 동작해야함

Comment를 작성한 소유자가 아니어도 적당한 Comment의 idㄱ밧을 사용해 comment_delete에 삭제 요청을 하면 댓글을 삭제할 수 있음
- View 함수에서 삭제 요청이 들어온 Comment의 작성자가 요청한 사용자와 일치하는지 먼저 확인해야함

글 작성 기본구조 구현
- View: post_add
- URL: 127.0.0.1:8000/posts/posts_add/
- Template: template/posts/post_add.html
PostForm 클래스 구현
- Form: PostFrom
- Post 모델 사용
- content 입력받을 수 있게 
Post_add.html 에서 PostForm에 사용자에게 데이터를 입력 받을수 있도록

Post 를 만들기 위해서는 내용 뿐 아니라 이미지 파일들도 필요
이미지 파일을 저장하는 필드는 Post 모델이아닌 PostImage모델에 있음

ModelForm은 기본적으로 class Meta 속성에 정의한 하나의 모델만을 생성할 수 있음
- 이미지 파일 여러 장을 추가로 받아 처리하는 기능은 가지고 있지 않음
- 여러 장의 이미지를 업로드해서 PostImage 객체를 여러 개 생성하는 기능을 PostForm 과는 별도로 구성

파일을 첨부하기 위해 <input> 의 type속성을 file로 선언
- 여러개의 파일을 첨부하기 위해서는 multiple 속성이 추가로 선언되어야 함
    - multiple 속성은 선언만 하면 되며 따로 값을 지정하지는 않음

파일을 첨부할 것이므로 form의 enctype을 multipart/form-data 로 지정
---------------------------------------------------------------------------------
label에 있는 for 속성은 이 label이 어떤 input에 대한 설명인지를 지정하는 역할
- 갑을 가리키는 input의 id속성값을 지정해야함

View에서 multiple 속성을 가진 file input 데이터 받기
- Template의 images 와 content 중 content는 PostForm으로 전달하고 images로 전달된 여러 개의 파일을 별도로 처리해야 함
- multiple 속성으로 전달한 여러개의 파일 데이터는 request.FILES 대신 request.FILES.getlist("<전달된 input의 'name'속성>")으로 가져옴

# 동적 URL
## URL 경로를 변경할 때 생기는 중복작업
- 프로젝트가 복잡해질수록 한 URL을 여러 곳에서 사용할 것이고, 변경할 부분이 많음
    - URLconf에 있는 URL 값이 변경되었을때 변경된 내용을 반영할 수 있다면 관리가 쉬워짐
    - Django에서는 이를 위해 동적URL을 사용할 수 있는 기능을 제공함

동적 URL 생성을 위한 요소 추가
- 동적으로 URL을 생성해서 사용하기 위해서는 app별로 분리된 하위 urls.py 에 app_name 이라는 속성이 필요

Template을 위한 {% url %} 태그
- {% 'URL pattern name' %} 태그는 Template에서 urls.py 의 내용을 이용해 동적으로 URL을 생성해줌
    - URL pattern name은 {urls.py에 있는 app_name}:{path()에 지정된 name}의 구조
    
{% url 'posts:comment_delete' comment_id=comment.id %}
- URL pattern name 이 posts:comment_delete 로, app_name이 posts인 urls.py에서 name이 comment_delete 인 URL을 동적으로 생성하겠다는 의미
    - 이 경로는 <int:comment_id> 부분의 값을 URL을 통해 동적으로 입력받음
    - 그러므로 이 path()를 사용해서 URL 경로를 만들려면 동적으로 입력받는 부분인 comment_id값이 필요함

View의 동적 URL 변경
- template 에서 {% url %} 태그를 사용하듯, View에서는 reverse 함수로 동적 URL을 생성
```
reverse("posts:comment_delete", kwargs={"comment_id":1}) 
'/posts/comment_delete/1/'
reverse("posts:comment_delete", args=[1])                
'/posts/comment_delete/1/'
```
---------------------------------------------------------------------------------
다대다 관계 모델
- 다대일(Many-to-one, N:1) 관계는 한 테이블의 한 레코드가 다른 테이블의 여러 레코드와 연관됨을 나타냄
- 다대다(Many-to-Many, N:N) 관계는 한 테이블의 여러 레코드가 다른 테이블의 여러 레코드와 연관되는 관계
- 다대다 관계는 두 테이블의 연결을 정의하는 또 하나의 테이블이 필요

- Post 모델에서 다대다를 선언하거나, HashTag 모델에서 다대다를 선언하거나 어느쪽이든 중간에 테이블이 하나 만들어진다는 결과는 같음
    - 하지만 관계에서 어느 쪽이 좀더 다른 쪽을 포함하는지에 따라 다대다를 선언하는 모델이 달라짐
        - 둘 중에서 좀더 타당하게 느껴지는 쪽을 다대다를 선언하는 모델로 정함
        - |글(Post)에 해시태그 여러 개를 포함하기
        - |해시태그(HashTag)에 글 여러 개를 포함하기

관리자페이지에서 여러 해시태그를 고를 수 있지만 체크박스 형태의 UI보다 불편
- admin에 formfield_overrides 옵션을 추가하면 선택할 항목을 checkbox로 표시할 수 있음

Post 모델에 tags라는 이름의 ManyToManyField를 선언했음
- post.tags.all()로 연결된 전체 HashTag 객체를 불러올 수 있음

해시태그 검색 기본 구조
- View: posts/view.py -> tags 함수
- URL : posts/tags/{tag의 name}/
- Templates posts/tags.html

해시태그 생성
- 모델에 정의된 ManyToManyField에 HashTag를 추가할 때는 add함수를 사용

get_or_create(): 인수로 전달하는 값에 해당하는 객체가 이미 존재한다면 DB의 내용을 가져오고, 없다면 새로 DB에 생성
- get_or_create()의 결과는 2개의 아이템을 가진 튜플로 변환
    - ```{DB에서 가져오거나 생성된 객체}, {생성여부} = Model.objects.get_or_create()```

Template 재사용
- {% include %} 태그로 <article> 태그를 재사용

글 작성 후 이동할 위치 지정
- 기존의 댓글 작성 후 redirect 로직
    - 댓글 작성 완료 후 피드 페이지로 이동하라는 응답을 반환
    - 댓글은 피드 페이지와 글 상세 페이지 양쪽에서 작성할 수  있으므로 각각의 경우에 따라 다르게 지정

{% include %} 태그의 with 옵션
- 각각의 글을 나타내는 HTML요소는 {% include 'post.html' %}로 가져오고 있으며 댓글을 작성하는 CommentForm은 post.html Template 내에서 사용하고 있음
- post.html 을 include로 가져오면서 댓글 작성 후 이동할 URL 값을 전달해야함

{% 태그명 as 변수명 %}:  태그로 만들어진 결과 값을 Template내에서 사용할 변수에 할당
- {% url 'posts:post_detail' post.id as action_redirect_to %} 는 post.id의 상세 페이지 URL이 action_redirect_to 변수에 할당
    - action_redirect_to 변수에 할당된 상세 페이지 URL은 댓글 작성이 완료된 후에 브라우저에서 이동해야 할 주소

{% include 'Template 명' with 변수명=값 %}: include로 가져올 Template에 변수명으로 값을 전달
- {% include 'posts/post.html' with action_redirect_url = action_redirect_to %}는 post.html Template을 렌더할 때, action_redirect_url 이라는 변수를 추가적으로 사용할 수 있게됨

Template 중복코드 제거
- 각 화면 단위 기능의 기반이 되는 레이아웃은 3가지
    - 상단 내비게이션 바가 없는 레이아웃: base.html
    - 내비게이션 바가 있는 레이아웃:base_nav.html
    - 내비게이션 바가 있으며, 이미지 슬라이더 기능이 포함된 레이아웃:base_slider.html

좋아요 기능
- 좋아요 기능은 해시태그와 같은 다대다 관계를 사용
- 해시태그는 글 생성시 입력한 문자열을 쉼표 단위로 구부냏서 생성했지만, 좋아요는 form과 button으로 구성해서 언제든 추가/삭제할 수 있는 토글방식으로 구현

좋아요 모델, 관리자 페이지 구성
- 좋아요 기능은 해시태그와 같은 M2M DB구조를 사용
- 사용자가 좋아요를 누른 Post와 좋아요를 누른 사용자들의 관계는 사용자의 좋아요 액션으로 만들어짐
    - 사용자 쪽이 주도적이므로 User 모델에 like_posts로 ManyToManyField를 정의하고, 좋아요 기능을 구현

필드에 정의한 related_name 속성은 역방향으로 Model을 참조할 때 사용하는 이름
- User 입장에서는 좋아요한 목록을 user.like_posts.all()로 불러올 수 있으며
- 반대로 Post입장에서는 자신에게 좋아요 를 누른 User 목록을 post.like_users.all()로 불러올 수 있음

만약 related_name을 별도로 지정하지 않으면 {모델명의 소문자}_set 으로 지정됨
- post.user_set 이라는 이름은 어떤 조건의 User 들과 연결될 것인지 알 수 없으므로 의미를 명확하게 나타내기 위해 related_name을 별도 지정

좋아요 처리는 토글(toggle)방식을 사용
- 이미 좋아요를 누른 상태라면 해제
- 그렇지 않다면 좋아요 상태로 만듬
- ManyToMany 연결을 제거하거나 추가하는 방식으로 구현할 수 있음

- 사용자가 좋아요를 누른 Post 목록에 좋아요 요청이 전달된 Post가 포함되어 있는지 한단하고
    - 이미 존재한다면 연결을 삭제
    - ManyToManyField의 remove 메서드로 연결을 삭제할 수 있음

- 반대로 전달된 Post 가 이미 좋아요를 누른 목록에 속하지 않는다면
    - add로 새로운 연결을 생성

- 생성이든 삭제든 로직이 실행된 후에는 댓글 작성 때와 같이 next로 전달된 URL로 되돌아감

form 의 action 주소는 방금 생성한 post_like View 함수로 연걸되게 하며, DB데이터를 변경하므로 method 는 POST 방식을 사용

csrf_token을 제외하면 form 내부에 아무런 input이 없음
- Post 의 좋아요 토글 기능에는 특별히 전달할 데이터가 없고
- 이런 경우 내부요소 없이 단순히 POST요청만을 전달

{% if user in post.like_users.all %} 태그로 이 Post에 좋아요를 누른 모든 User 목록에 현재 로그인한 유저가 포함되는지 판단
- 좋아요를 누른 상태라면 button 태그의 style 속성에 color: red; 값을 지정해 글자를 빨간색으로 바꾸어 사용자가 Post에 좋아요 한 상태임을 표시

# 팔로우/팔로잉 기능
- 팔로우/팔로잉 관계는 해시태그, 좋아요와 같이 ManyToManyField를 사용해 다대다 관계로 구성되나 이들과는 다른 점이 있음
- 해시태그와 좋아요는 한쪽에서의 연결은 반대쪽에서도 연결을 나타나는 대칭적(Symmetrical)인 관계
- 팔로우/팔로잉 관계는 한쪽에서의 연결과 반대쪽에서의 연결이 별도로 구분되는 비대칭적인 관계

프로필 페이지
- 프로필 페이지 기본구조
    - 자신의 정보, 작성한 글, 팔로우/팔로잉 수를 보여줄 페이지
    - View : users/views.py -> profile
    - URL : 127.0.0.1:8000/users/<int:user_id/profile>
    - Template : templates/users/profile.html

base_profile.html 구성
- 프로필 페이지에서는 사용자 정보와 사용자의 Post 목록을 표시
- 프로필 페이지의 사용자 정보는 재사용하고
- Post 목록 대신 팔로우/팔로잉 목록을 사용할 수 있도록 
- 상단 사용자 정보를 공통으로 사용하는 기반 Template 인 base_profile.html을 구성

팔로우/팔로잉 목록
- 자신을 팔로우하는 사용자 목록
    - View: users/vies.py -> following
    - URL : /users/<int:user_id>/following/
    - Template : templates/users/following.html

팔로우 토글 View
- Post의 좋아요 기능과 같이 이미 팔로우 되어 잇다면 언팔로우를
- 팔로우 되어 있지 ㅇ낳다면 팔로우 목록에 추가하는 토글 기능을 사용
    - View: users/view.py -> follow
    - URL: users/<int:user_id>/follow/
    - Template: 없음