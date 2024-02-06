from django.shortcuts import render,redirect, get_object_or_404
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def login_view(request):
    # 이미 로그인되어 있다면
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    
    if request.method == "POST":
        # LoginForm 인스턴스를 만들며, 입력데이터는 request.POST를 사용
        form = LoginForm(data=request.POST)
        
        # LoginForm에 전달된 데이터가 유효하다면
        if form.is_valid():
            # username과 password 값을 가져와 변수에 할당
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            # username, password 에 해당하는 사용자가 있는지 검사
            user = authenticate(username=username, password=password)
            
            # 해당 사용자가 존재한다면 
            if user:
                # 로그인 처리 후, 피드 페이지로 redirect
                login(request, user)                
                return redirect("posts:feeds")
            
            # 사용자가 없다면 "실패했습니다" 로그 출력
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")                
                
            
        
        
        
    else:
    # LoginForm 인스턴스를 생성
        form = LoginForm()
    
    # 생성한 LoginForm 인스턴스를 템플릿에 "form"이라는 키로전달
    context ={
        "form" : form
    }
    return render(request, "users/login.html", context)

def logout_view(request):
    # logout 함수 호출에 request를 전달
    logout(request)
    # logout 처리 후, 로그인 페이지로 이동
    return redirect('users:login')

def signup(request):    
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        # Form에 에러가 없다면 곧바로 User를 생성하고 로그인 후 피드페이지로 이동
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts:feeds")
        
        # Form에 에러가 있다면, 에러를 포함한 Form을 사용해 회원가입 페이지를 보여줌
        # else:
        #     context = {"form" : form}
        #     return render(request, "users/signup.html", context)            
    
    else:
        form = SignupForm()
    # context로 전달되는 form은 두 가지 경우가 존재
    # 1. POST 요청에서 생성된 form이 유효하지 않은 경우
        # -> 에러를 포함한 form이 사용자에게 보여짐
    # 2. GET 요청으로 빈 form이 생성되는 경우
    context = {"form" : form}
    return render(request, "users/signup.html", context)

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        "user": user,
    }
    return render(request, "users/profile.html", context)    

def followers(request, user_id):
    user = get_object_or_404(User, id=user_id)
    relationships = user.follower_relationships.all()
    context = {
        "user" : user,
        "title" : "Followers",
        "relationships" : relationships,
    }
    return render(request, "users/followers.html", context)

def following(request, user_id):
    user = get_object_or_404(User, id=user_id)
    relationships = user.following_relationships.all()
    context = {
        "user" : user,
        "title" : "Following",
        "relationships" : relationships,
    }
    return render(request, "users/following.html", context)

def follow(request, user_id):
    # 로그인한 유저
    user = request.user    
    # 팔로우 하려는 유저
    target_user = get_object_or_404(User,id=user_id)
    
    # 팔로우 하려는 유저가 이ㅣ미 자신의 팔로잉 목록에 있는 경우
    if target_user in user.following.all():
        # 팔로잉 목록에서 제거
        user.following.remove(target_user)
    else:
        # 팔로잉 목록에 추가
        user.following.add(target_user)
    
    # 팔로우 토글 후 이동할 URL이 전달 되었다면 해당 주소로
    # 전달되지 않았다면 로그인 한 유저의 프로필 페이지로 이동
    url_next = request.GET.get("next") or reverse("user:profile", args=[user.id])
    
    return HttpResponseRedirect(url_next)
    
    