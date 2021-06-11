from django.http.response import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.http import  HttpResponse
from studentapp.models import Student



def home_page_view(request):
    return render(request ,'studentapp/home.html')



def add_student_view(request):
    print(request.POST) # request.POST = {'uname': ['jay'], 'umarks': ['88'], 'uroll_num': ['55']}

    if request.method == 'POST':
        uname           = request.POST.get('uname')
        umarks          = request.POST.get('umarks')
        uroll_num       = request.POST.get('uroll_num')

        obj = Student(name = uname , marks = umarks , roll_num = uroll_num)
        obj.save()
        return redirect('/student/list/')


    return render(request, 'studentapp/add_student.html')


def get_all_student_view(request):

    data = Student.objects.all()


    return render(request , 'studentapp/list_student.html' , {'data' : data })


def student_detail_view(request , id):
    obj = Student.objects.get(pk = id)

    return render(request,'studentapp/detail.html' , {'obj':obj})


def student_update_view(request, id):
    obj = Student.objects.get(pk = id)
    print(request.POST)
    if request.method == 'POST':
        obj.name = request.POST.get('uname')
        obj.marks = request.POST.get('umarks')
        obj.roll_num = request.POST.get('uroll_num')
        obj.save()
        return redirect(f'/student/detail/{obj.id}/')

    return render(request , 'studentapp/update.html' , {'obj' : obj})



def student_delete_view(request , id):
    obj = Student.objects.get(pk = id)
    if request.method == "POST":
        obj.delete()
        return redirect('/student/list/')
    return render(request , 'studentapp/delete.html' , {'obj' : obj})
    