
from django.shortcuts import render,redirect
from todo.models import Task

def add(request):
    if (request.method=='POST'):
        heading=request.POST['heading']
        detail=request.POST['detail']
        date=request.POST['date']
        print(heading)
        print(detail)
        print(date)


        # creating a sql quary to add data into database
        # model_class.objects.create(column_name=value)
        insert_data=Task.objects.create(heading=heading,detail=detail,date=date)
        return redirect('/')
    return render(request,'todo/add.html')

def index(request):
    content={}
    # content['data']=Task.objects.all()
    content['data']=Task.objects.filter(is_deleted="n")
    return render(request,'todo/index.html',content)


def delete(request,tid):
    record_to_be_deleted=Task.objects.filter(id=tid)
    # record_to_be_deleted.delete()
    record_to_be_deleted.update(is_deleted="y")
    return redirect("/")



def update(request,tid):
    if(request.method=='POST'):
        heading=request.POST['heading']
        detail=request.POST['detail']
        date=request.POST['date']
        record_to_be_update=Task.objects.filter(id=tid)
        record_to_be_update.update(heading=heading,detail=detail,date=date)
        return redirect('/')
    else:
        content={}
        content['data']=Task.objects.get(id=tid)
        return render(request,'todo/update.html',content)


# Create your views here.
