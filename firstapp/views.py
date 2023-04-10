from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Book


# Create your views here.
@login_required
@csrf_exempt

def home(request):     #http request 
    # print(request.method)
    if request.method=="POST": 
        data= request.POST
        print(data)
        bid = data.get("book_id")
        # print(request.POST)678
        name = data.get("book_name")
        qty = data.get("book_qty")
        price = data.get("book_price")
        author = data.get("book_author")
        is_pub = data.get("book_is_pub")
        # print(name, qty, price, author, is_pub)
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False

        if not bid:
            Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_pub)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_pub
            book_obj.save()
        return redirect("home_page")
        # return HttpResponse("Success")
    elif request.method=="GET":
        # return render(request, "home.html", context={"all_books":Book.objects.all()})
        return render(request, "old_home.html", context={"person_name": "Vaishnavi"})
        
@login_required
def show_books(request):
    return render(request, "show_books.html", {"books" : Book.objects.filter(is_active = True), "active":True})

@login_required
def update_book(request, id):           
    book_obj = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book": book_obj})

@login_required
def delete_book(request, pk):
    Book.objects.get(id=pk).delete()
    return redirect("all_active_books")

@login_required
def soft_delete_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = False
    book_obj.save()
    return redirect("all_inactive_books")

@login_required
def show_inactive_books(request):
    return render (request, "show_books.html", {"books" : Book.objects.filter(is_active = False), "inactive":True})

@login_required
def restore_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = True
    book_obj.save()
    return redirect("all_active_books")

# 
from .forms import BookForm, AddressForm
from django.contrib.auth.forms import UserCreationForm
@login_required
def book_form(request):
    form = BookForm()
    if request.method == 'POST':
        print(request.POST)
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()         # database save
            return HttpResponse("Successfully Registered!!!")
    else:
        context = {'form':form}
        return render(request, "book_form.html", context=context)

# simpleisbetterthancomplex
def sibtc(request):
    return render(request, "sibtc.html", {"form" : AddressForm()})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    print("In Index function")
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)
    print(page)
    paginator = Paginator(book_list, 3)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'books':books})


# from django.views import View

# class NewView(View):
#     def get(self, request):
#         return HttpResponse('get response')
    
#     def post(self, request):
#         return HttpResponse('post response')
    
#     def put(self, request):
#         return HttpResponse('put response')
    
#     def patch(self, request):
#         return HttpResponse('patch response')
    
#     def delete(self, request):
#         return HttpResponse('delete response')


from django.views.generic.edit import CreateView

  
class BookCreate(CreateView):  
    model = Book
    fields = '__all__'
    success_url = "/cbv-create-book/"

    # 113 - 1 hr completed
 




# import requests
# # GET_SINGLE_STUD_URL = "http://127.0.0.1:8000/api/get-student/{}/"
# GET_ALL_STUDS_URL = "http://127.0.0.1:8000/api/get-all-students"
# # CREATE_STUD_URL = "http://127.0.0.1:8000/api/create-student"

# def get_all_stud(request):
#     response = requests.request("GET", GET_ALL_STUDS_URL)
#     python_dict = response.json()       # json to python dict
#     return render(request, "student_data.html", {"data": python_dict})