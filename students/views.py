from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
    students = Student.objects.all()
    stuForms = StudentForm()
    
    paginator = Paginator(students, 5)  # Show 5 freelancers per page
    page = request.GET.get('page')
    students = paginator.get_page(page)
    context = {
        'students': students,
        'stuForms': stuForms
    }
    return render(request, 'students/index.html', context)

def save_data(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            roll = request.POST['roll']
            city = request.POST['city']
            course = request.POST['course']
            print(sid,name,roll,city,course)
            
            # Save data
            if sid == '':
                stu = Student(name=name, roll=roll, city=city, course=course)
            else:
                stu = Student(id=sid, name=name, roll=roll, city=city, course=course)
            stu.save()

            stu = Student.objects.values()
            student_data = list(stu)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s = Student.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    



def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print('Student ID',id)
        student = Student.objects.get(pk=id)
        student_data = {'id':student.id, 'name':student.name, 'roll':student.roll, 'city':student.city, 'course':student.course}
        return JsonResponse(student_data)