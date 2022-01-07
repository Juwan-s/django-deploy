from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello Wordl!</h1>")
    name = "Juwan"
    age = 27
    instagram_id = "what_ju_wan_t"

    return render( request,'index.html' , {"my_name" : name, "my_age":age, "instagram" : instagram_id} )

def coffee_view(request):

    coffee_all = Coffee.objects.all()

    # 만약 Request가 POST 라면
    #POST를 바탕으로 Form을 완성하고
    # Form이 유효하면 저장

    if request.method == "POST":
        form = CoffeeForm(request.POST) # 완성된 form
        if form.is_valid(): # 채워진 form이 유효하다면
            form.save() # 이 form 내용을 Model을 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list":coffee_all, "coffee_form":  form})


    