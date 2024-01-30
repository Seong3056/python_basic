from django.shortcuts import render, redirect
from blog.models import Post,Comment
# Create your views here.
def index(request):
    return render(request, "index.html")

def post_list(request):    
    posts = Post.objects.all()    
    context = { 
    "posts" : posts,    
                }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    match request.method :
        case 'POST':
            print("POST요청발생")        
            content = request.POST["comment"]        
            Comment.objects.create(post=post,content=content)
            
            return redirect(f"/posts/{post.id}/")
    
        
        
    context = {
        "post_id" : post_id,
        "post" : post
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        print("method POST")
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES.get("thumbnail" , None)
        
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail
        )
        print(post.id)
        return redirect(f"/posts/{post.id}/")
    
    #print(request.POST) # POST 메서드로 전달된 데이터를 출력
    return render(request, "post_add.html")