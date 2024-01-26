from django.http import HttpResponse 
# HttpResponse : Django가 반환한 값을 브라우저가 읽을 수 있도록 적절한 처리를 해주는 역할
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return HttpResponse("안녕하세요 버거맨입니다.")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록: ",burgers)   
    
    # Template으로 전달해줄 dict객체     
    context = {
        "burgers" : burgers, # burgers 키에 burgers 변수(QuerySet객체)를 전달
    }
    return render(request, "burger_list.html", context)

def burger_search(request):
    keyword = request.GET.get("keyword", None)
    print(keyword)
    if keyword: # keyword값이 주어진경우                
        # 이름에 전달받은 키워드 값이 포함된 버거를 검색
        burgers = Burger.objects.filter(name__contains=keyword)        
        
    else: # keyword가 주어지지 않아, None이 할당된 경우
        burgers = Burger.objects.none()
    context = {
            "burgers" : burgers,
        }
    return render(request, "burger_search.html", context)

