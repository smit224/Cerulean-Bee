from os import error
from turtle import pd
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from sklearn.externals import joblib
from django.contrib.staticfiles import finders
from datetime import date
# Create your views here.

# Create your views here.
def index(request):
    error=""
    if request.method=='POST':
        em = request.POST['username']
        pas = request.POST['password']
        user = SystemUser.objects.get(username=em,password=pas)
        #print("------------",user,"-----------")
        if user:
           #print("------------user found----------")
           #login(request,user)
           error="no"
        else:
            error="yes"
    d={'error':error}    
    return render(request,'index.html',d)
    

def signup(request):
    error=""
    msg=""
    if request.method=='POST':
        
        em = request.POST['email']
        pwd = request.POST['password']
        un = request.POST['username']
        try:
           
           SystemUser.objects.create(username=un,email_id=em,password=pwd)
           error="No"
        except Exception as e:
            error="Yes"
            msg=str(e)
    d={'error':error,'msg':msg}
    print("-=-=-=-=dddd-=-=-",d)
    return render(request,'signup.html',d)

def home(request):
    
    return render(request,'home.html')

def artwork_order(request):
    print("-=-=-=-sk98rt-=-=-")
    data=ArtworkOrder.objects.all()
    d = {'data':data}
    return render(request,'artwork_order.html',d)

def employee_details(request):
    
    return render(request,'employee_details.html')

def print_order(request):
    
    return render(request,'print_order.html')

def project_cost_analysis(request):
    
    return render(request,'project_cost_analysis.html')

def add_artwork_order(request):
    
    error=""

    if request.method=='POST':
        cun = request.POST['customer_name']
        ordate = request.POST['order_date']
        cuemail = request.POST['email_id']
        appdate = request.POST['approved_date']
        phn = request.POST['phone_number']
        scpridate = request.POST['scheduled_print_date']
        disrate = float(request.POST['discount_rate'])
        totpri = float(request.POST['total_price'])
        appitem = request.POST['apparel_item']
        evename = request.POST['event_name']
        basecol = request.POST['base_color']
        thname = request.POST['theme_name']
        maxcolor = request.POST['max_colors']
        artloc1 = request.POST['art_location_01']
        desc1 = request.POST['description_01']
        cost1 = int(request.POST['cost_01'])
        emp1 = request.POST['employee_01']
        cd1 = request.POST['complete_date_01']
        col1 = request.POST['colors_01']
        artloc2 = request.POST['art_location_02']
        desc2 = request.POST['description_02']
        cost2 = request.POST['cost_02']
        emp2 = request.POST['employee_02']
        cd2 = request.POST['complete_date_02']
        col2 = request.POST['colors_02']

        
        try:
           
           ArtworkOrder.objects.create(customer_name=cun, email_id=cuemail, phone_number=phn, discount_rate=disrate, order_date=ordate, 
                                        approved_date=appdate, scheduled_print_date=scpridate, total_price=totpri, apparel_item=appitem,
                                        event_name=evename, base_color=basecol, theme_name=thname, max_colors=maxcolor, art_location_01=artloc1,
                                        description_01=desc1, cost_01=cost1, employee_01=emp1, complete_date_01=cd1, colors_01=col1, art_location_02=artloc2,
                                        description_02=desc2, cost_02=cost2, employee_02=emp2, complete_date_02=cd2, colors_02=col2)
           error="No"
        except:
            error="Yes"

    d={'error':error}
    # print("-------sasasasasasas-----",d)
    return render(request,'add_artwork_order.html',d)

def add_employee_work(request):
    emp_name = request.POST['employee_name']
    emp_phone = request.POST['employee_phone']
    work_type = request.POST['work_type']
    pd_date_01 = request.POST['pd_date_01']
    pd_start_time_01 = request.POST['pd_start_time_01']
    project_01 = request.POST['project_01']
    art_item_01 = request.POST['art_item_01']
    task_01 = request.POST['task_01']
    end_time_01 = request.POST['end_time_01']
    pd_date_02 = request.POST['pd_date_02']
    pd_start_time_02 = request.POST['pd_start_time_02']
    project_02 = request.POST['project_02']
    art_item_02 = request.POST['art_item_02']
    task_02 = request.POST['task_02']
    end_time_02 = request.POST['end_time_02']

    try:   
        ArtworkOrder.objects.create(employee_name=emp_name, employee_phone=emp_phone, work_type=work_type, pd_date_01=pd_date_01, pd_start_time_01=pd_start_time_01, project_01=project_01, art_item_01=art_item_01,
                                    task_01=task_01, end_time_01=end_time_01, pd_date_02=pd_date_02, pd_start_time_02=pd_start_time_02, project_02=project_02, art_item_02=art_item_02,
                                    task_02 = task_02, end_time_02=end_time_02)
        error="No"
    except:
        error="Yes"

    d={'error':error}
    return render(request,'add_employee_work.html')

def view_deatils_artwork(request,pid):
      
    art = ArtworkOrder.objects.get(customer_id=pid)
    d = {'data':art}
    return render(request,'view_deatils_artwork.html',d)


def delete_artwork(request,pid):

    data=ArtworkOrder.objects.get(customer_id=pid)
    data.delete()
    return redirect('artwork_order')

def edit_artwork_order(request,pid):
      
    error=""
    data = ArtworkOrder.objects.get(customer_id=pid)
    if request.method=='POST':
        
        cun = request.POST['customer_name']
        ordate = request.POST['order_date']
        cuemail = request.POST['email_id']
        appdate = request.POST['approved_date']
        phn = request.POST['phone_number']
        scpridate = request.POST['scheduled_print_date']
        disrate = float(request.POST['discount_rate'])
        totpri = float(request.POST['total_price'])
        appitem = request.POST['apparel_item']
        evename = request.POST['event_name']
        basecol = request.POST['base_color']
        thname = request.POST['theme_name']
        maxcolor = request.POST['max_colors']
        artloc1 = request.POST['art_location_01']
        desc1 = request.POST['description_01']
        cost1 = int(request.POST['cost_01'])
        emp1 = request.POST['employee_01']
        cd1 = request.POST['complete_date_01']
        col1 = request.POST['colors_01']
        artloc2 = request.POST['art_location_02']
        desc2 = request.POST['description_02']
        cost2 = request.POST['cost_02']
        emp2 = request.POST['employee_02']
        cd2 = request.POST['complete_date_02']
        col2 = request.POST['colors_02']

        #job.title = jt
        #job.company = com
        data.customer_name = cun
        data.email_id = cuemail
        data.phone_number = phn
        data.discount_rate = disrate
        data.order_date = ordate
        data.approved_date = appdate
        data.scheduled_print_date = scpridate
        data.total_price = totpri
        data.apparel_item = appitem
        data.event_name = evename
        data.base_color=basecol
        data.theme_name = thname
        data.max_colors = maxcolor
        data.art_location_01 = artloc1
        data.description_01 = desc1
        data.cost_01 = cost1
        data.employee_01 = emp1
        data.complete_date_01 = cd1
        data.colors_01 = col1
        data.art_location_02 = artloc2
        data.description_02 = desc2
        data.cost_02 = cost2
        data.employee_02 = emp2
        data.complete_date_02 = cd2
        data.colors_02 = col2
        try:
            data.save()
            error="No"
        except:
            error="Yes"
    d={'error':error,'data':data} 
    return render(request,'edit_artwork_order.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

