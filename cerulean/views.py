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
        try:
            user = SystemUser.objects.get(username=em,password=pas)
            #print("------------",user,"-----------")
            if user:
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}  
    print('==========',error,'===========')  
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
    artcount = ArtworkOrder.objects.all().count()
    print("=-=--=artcount-=-==-=", artcount)
    emp_work_count = EmployeeWorkDetails.objects.all().count() 
    print("=-=--=artcount-=-==-=", emp_work_count)
    print_order_count = PrintOrder.objects.all().count()
    print("=-=--=artcount-=-==-=", print_order_count) 
    project_cost_analysis_count = ProjectCostAnalysis.objects.all().count() 
    print("=-=--=artcount-=-==-=", project_cost_analysis_count)
    d={'artcount':artcount,'emp_work_count':emp_work_count,'print_order_count': print_order_count, 'project_cost_analysis_count':project_cost_analysis_count}
    return render(request,'home.html',d)

def artwork_order(request):
    print("-=-=-=-sk98rt-=-=-")
    data=ArtworkOrder.objects.all()
    d = {'data':data}
    return render(request,'artwork_order.html',d)



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

#EMPLOYEE WORK DETAILS
def employee_details(request):
    data=EmployeeWorkDetails.objects.all()
    d = {'data':data}
    print("-=-=-=-sk98rt-=-=-")
    return render(request,'employee_details.html',d)
    
    

def add_employee_work(request):
    
    error=""
    if request.method=='POST':        
        emp_name = request.POST['employee_name']
        empl_phone = request.POST['employee_phone']
        work_type = request.POST.get('work_type')
        pd_date_01 = request.POST['pd_date_01']
        pd_start_time_01 = request.POST['pd_start_time_01']
        pd_start_time_01 = pd_start_time_01 + ':00'
        project_01 = request.POST['project_01']
        art_item_01 = request.POST['art_item_01']
        task_01 = request.POST['task_01']
        end_time_01 = request.POST['end_time_01']
        end_time_01 = end_time_01 + ':00'
        pd_date_02 = request.POST['pd_date_02']
        pd_start_time_02 = request.POST['pd_start_time_02']
        pd_start_time_02= pd_start_time_02 + ':00'
        project_01 = request.POST['project_01']
        project_02 =request.POST['project_02']
        art_item_02 = request.POST['art_item_02']
        task_02 = request.POST['task_02']
        end_time_02 =request.POST['end_time_02']
        end_time_02= end_time_02 + ':00'
        
        try:   
            EmployeeWorkDetails.objects.create(employee_name=emp_name, employee_phone=empl_phone, work_type=work_type, pd_date_01=pd_date_01,pd_start_time_01=pd_start_time_01, project_01=project_01, art_item_01=art_item_01,
                                        task_01=task_01, end_time_01=end_time_01, pd_date_02=pd_date_02, project_02=project_02, art_item_02=art_item_02,
                                        task_02 = task_02, pd_start_time_02=pd_start_time_02,end_time_02=end_time_02)
            error="No"
        except Exception as e:
            print("-----",e)

    d={'error':error}
    print("-----------aaaa-------", d)
    return render(request,'add_employee_work.html',d)

def view_employee_work(request,pid):
      
    work = EmployeeWorkDetails.objects.get(employee_id=pid)
    d = {'data':work}
    return render(request,'view_employee_work.html',d)

def delete_employee_work(request,pid):

    data=EmployeeWorkDetails.objects.get(employee_id=pid)
    data.delete()
    return redirect('employee_details')


def edit_employee_work(request,pid):
      
    error=""
    data = EmployeeWorkDetails.objects.get(employee_id=pid)
    if request.method=='POST':
        
        emp_name = request.POST['employee_name']
        empl_phone = request.POST['employee_phone']
        work_type = request.POST.get('work_type')
        pd_date_01 = request.POST['pd_date_01']
        pd_start_time_01 = request.POST['pd_start_time_01']
        pd_start_time_01 = pd_start_time_01 + ':00'
        project_01 = request.POST['project_01']
        art_item_01 = request.POST['art_item_01']
        task_01 = request.POST['task_01']
        end_time_01 = request.POST['end_time_01']
        end_time_01 = end_time_01 + ':00'
        pd_date_02 = request.POST['pd_date_02']
        pd_start_time_02 = request.POST['pd_start_time_02']
        pd_start_time_02= pd_start_time_02 + ':00'
        # project_01 = request.POST['project_01']
        project_02 =request.POST['project_02']
        art_item_02 = request.POST['art_item_02']
        task_02 = request.POST['task_02']
        end_time_02 =request.POST['end_time_02']
        end_time_02= end_time_02 + ':00'

        #job.title = jt
        #job.company = com
        data.employee_name = emp_name
        data.employee_phone = empl_phone
        data.work_type = work_type
        data.pd_date_01 = pd_date_01
        data.pd_start_time_01 = pd_start_time_01
        data.project_01 = project_01
        data.art_item_01 = art_item_01
        data.task_01 = task_01
        data.end_time_01 = end_time_01
        data.pd_date_02 = pd_date_02
        data.pd_start_time_02=pd_start_time_02
        data.project_02 = project_02
        data.art_item_02 = art_item_02
        data.task_02 = task_02
        data.end_time_02 = end_time_02
        
        try:
            data.save()
            error="No"
        except:
            error="Yes"
    d={'error':error,'data':data} 
    return render(request,'edit_employee_work.html',d)

#PRINT ORDERS
def print_order(request):
    data=PrintOrder.objects.all()
    d = {'data':data}
    print("-=-=-=-sk98rt-=-=-")
    return render(request,'print_order.html',d)

def add_print_order(request):
    
    error=""
    if request.method=='POST':        
        customername = request.POST['customername']
        orderdate = request.POST['orderdate']
        emailid = request.POST['emailid']
        artdate = request.POST['artdate']
        phonenumber = request.POST['phonenumber']
        duedate = request.POST['duedate']
        setupcharge = request.POST['setupcharge']
        apparelorderdate = request.POST['apparelorderdate']
        deposit = request.POST['deposit']
        filmdate = request.POST['filmdate']
        discount = request.POST['discount']
        printdate = request.POST['printdate']
        totalcost = request.POST['totalcost']
        basecolor = request.POST['basecolor']
        vendorname = request.POST['vendorname']
        xsnumber = request.POST['xsnumber']
        xscharge = request.POST['xscharge']
        snumber = request.POST['snumber']
        scharge = request.POST['scharge']
        mnumber = request.POST['mnumber']
        mcharge = request.POST['mcharge']
        lnumber = request.POST['lnumber']
        lcharge = request.POST['lcharge']
        xlnumber = request.POST['xlnumber']
        xlcharge = request.POST['xlcharge']
        xxlnumber = request.POST['xxlnumber']
        xxlcharge = request.POST['xxlcharge']
        unitbaseprice = request.POST['unitbaseprice']
        colorcharge = request.POST['colorcharge']
        blankprice = request.POST['blankprice']
        locationsize = request.POST['locationsize']
        colorchange = request.POST['colorchange']
        colorlist = request.POST['colorlist']
        finalcost = request.POST['finalcost']
        
        
        try:   
            PrintOrder.objects.create(customername=customername, orderdate=orderdate, emailid=emailid, artdate=artdate, phonenumber=phonenumber, duedate=duedate, setupcharge=setupcharge,
                                       apparelorderdate=apparelorderdate, deposit=deposit, filmdate=filmdate, discount=discount, printdate=printdate, totalcost=totalcost, basecolor=basecolor,
                                        vendorname=vendorname, xsnumber=xsnumber, xscharge=xscharge, snumber=snumber, scharge=scharge, mnumber=mnumber, mcharge=mcharge, lnumber=lnumber, lcharge=lcharge,
                                        xlnumber=xlnumber, xlcharge=xlcharge, xxlnumber=xxlnumber, xxlcharge=xxlcharge, unitbaseprice=unitbaseprice, colorcharge=colorcharge, blankprice=blankprice, locationsize=locationsize,
                                         colorchange=colorchange, colorlist=colorlist,finalcost=finalcost)
            error="No"
        except Exception as e:
            print("-----",e)
            error="Yes"

    d={'error':error}
    print("-----------aaaa-------", d)
    return render(request,'add_print_order.html',d)

def view_print_order(request,pid):
      
    work = PrintOrder.objects.get(customer_id=pid)
    d = {'data':work}
    return render(request,'view_print_order.html',d)

def edit_print_order(request,pid):
      
    error=""
    data = PrintOrder.objects.get(customer_id=pid)
    if request.method=='POST':
        
        customername = request.POST['customername']
        orderdate = request.POST['orderdate']
        emailid = request.POST['emailid']
        artdate = request.POST['artdate']
        phonenumber = request.POST['phonenumber']
        duedate = request.POST['duedate']
        setupcharge = request.POST['setupcharge']
        apparelorderdate = request.POST['apparelorderdate']
        deposit = request.POST['deposit']
        filmdate = request.POST['filmdate']
        discount = request.POST['discount']
        printdate = request.POST['printdate']
        totalcost = request.POST['totalcost']
        basecolor = request.POST['basecolor']
        vendorname = request.POST['vendorname']
        xsnumber = request.POST['xsnumber']
        xscharge = request.POST['xscharge']
        snumber = request.POST['snumber']
        scharge = request.POST['scharge']
        mnumber = request.POST['mnumber']
        mcharge = request.POST['mcharge']
        lnumber = request.POST['lnumber']
        lcharge = request.POST['lcharge']
        xlnumber = request.POST['xlnumber']
        xlcharge = request.POST['xlcharge']
        xxlnumber = request.POST['xxlnumber']
        xxlcharge = request.POST['xxlcharge']
        unitbaseprice = request.POST['unitbaseprice']
        colorcharge = request.POST['colorcharge']
        blankprice = request.POST['blankprice']
        locationsize = request.POST['locationsize']
        colorchange = request.POST['colorchange']
        colorlist = request.POST['colorlist']
        finalcost = request.POST['finalcost']

        #job.title = jt
        #job.company = com
        data.customername = customername
        data.orderdate = orderdate
        data.emailid = emailid
        data.artdate = artdate
        data.phonenumber = phonenumber
        data.duedate = duedate
        data.setupcharge = setupcharge
        data.apparelorderdate = apparelorderdate
        data.deposit = deposit
        data.filmdate = filmdate
        data.discount=discount
        data.printdate = printdate
        data.totalcost = totalcost
        data.basecolor = basecolor
        data.vendorname = vendorname
        data.xsnumber = xsnumber
        data.xscharge = xscharge
        data.snumber = snumber
        data.scharge = scharge
        data.mnumber = mnumber
        data.mcharge = mcharge
        data.lnumber = lnumber
        data.lcharge = lcharge
        data.xlnumber = xlnumber
        data.xlcharge = xlcharge
        data.xxlnumber = xxlnumber
        data.xxlcharge = xxlcharge
        data.unitbaseprice = unitbaseprice
        data.colorcharge = colorcharge
        data.blankprice = blankprice
        data.locationsize = locationsize
        data.colorchange = colorchange
        data.colorlist = colorlist
        data.finalcost = finalcost
        
        try:
            data.save()
            error="No"
        except:
            error="Yes"
    d={'error':error,'data':data} 
    return render(request,'edit_print_order.html',d)

def view_print_order(request,pid):
      
    work = PrintOrder.objects.get(customer_id=pid)
    d = {'data':work}
    return render(request,'view_print_order.html',d)

def delete_print_order(request,pid):

    data=PrintOrder.objects.get(customer_id=pid)
    data.delete()
    return redirect('print_order')


#PROJECT COST ANALYSIS
def delete_projectcostanalysis(request,pid):

    data=ProjectCostAnalysis.objects.get(project_id=pid)
    data.delete()
    return redirect('project_cost_analysis')


def project_cost_analysis(request):
    data=ProjectCostAnalysis.objects.all()
    d = {'data':data}
    return render(request,'project_cost_analysis.html',d)

def add_project_cost_analysis(request):

    error=""
    if request.method=='POST':
        project_name = 	request.POST['project_name']
        event_name	= request.POST['event_name']
        item_name = request.POST['item_name']	
        customer_name = request.POST['customer_name']	
        phonenumber	= request.POST['phonenumber']
        mc_item_01 = request.POST['mc_item_01']	
        mc_unitcost_01	= request.POST['mc_unitcost_01']
        mc_pricecharge_01 = request.POST['mc_pricecharge_01']
        mc_units_01	= request.POST['mc_units_01']
        mc_cost_01	= request.POST['mc_cost_01']
        mc_revenue_01 = request.POST['mc_revenue_01']
        mc_item_02	= request.POST['mc_item_02']
        mc_unitcost_02	= request.POST['mc_unitcost_02']
        mc_pricecharge_02 = request.POST['mc_pricecharge_02']	
        mc_units_02	= request.POST['mc_units_02']
        mc_cost_02 = request.POST['mc_cost_02']	
        mc_revenue_02 = request.POST['mc_revenue_02']	
        totalcost_01 = request.POST['totalcost_01']	
        totalrevenue_01	= request.POST['totalrevenue_01']
        lc_item_01 = request.POST['lc_item_01']	
        lc_unitcost_01 = request.POST['lc_unitcost_01']	
        lc_pricecharge_01 = request.POST['lc_pricecharge_01']	
        lc_units_01	= request.POST['lc_units_01']
        lc_cost_01	= request.POST['lc_cost_01']
        lc_revenue_01 = str(int(lc_cost_01)*int(lc_units_01))
        lc_item_02 = request.POST['lc_item_02']	
        lc_unitcost_02 = request.POST['lc_unitcost_02']	
        lc_pricecharge_02 = request.POST['lc_pricecharge_02']	
        lc_units_02	= request.POST['lc_units_02']
        lc_cost_02	= request.POST['lc_cost_02']
        lc_revenue_02 = str(int(lc_cost_02)*int(lc_units_02))
        totalrevenue_02 = request.POST['totalrevenue_02']	
        material_charge	= request.POST['material_charge']
        artwork_fees = request.POST['artwork_fees']	
        fixed_charges = request.POST['fixed_charges']	
        total_discounts	= request.POST['total_discounts']
        net_profits = request.POST['net_profits']

        try:   
            ProjectCostAnalysis.objects.create(project_name=project_name,event_name= event_name,
                                                item_name=item_name,	
                                                customer_name=customer_name,
                                                phonenumber=phonenumber,	
                                                mc_item_01=mc_item_01,	
                                                mc_unitcost_01=mc_unitcost_01,	
                                                mc_pricecharge_01=mc_pricecharge_01,	
                                                mc_units_01=mc_units_01,	
                                                mc_cost_01=mc_cost_01,	
                                                mc_revenue_01=mc_revenue_01,	
                                                mc_item_02=mc_item_02,	
                                                mc_unitcost_02=mc_unitcost_02,	
                                                mc_pricecharge_02=mc_pricecharge_02,	
                                                mc_units_02=mc_units_02,	
                                                mc_cost_02=mc_cost_02,	
                                                mc_revenue_02=mc_revenue_02,	
                                                totalcost_01=totalcost_01,	
                                                totalrevenue_01=totalrevenue_01,	
                                                lc_item_01=lc_item_01,	
                                                lc_unitcost_01=	lc_unitcost_01,
                                                lc_pricecharge_01=lc_pricecharge_01,	
                                                lc_units_01	= lc_units_01,
                                                lc_cost_01=lc_cost_01,	
                                                lc_revenue_01 = lc_revenue_01,
                                                lc_item_02 = lc_item_02,	
                                                lc_unitcost_02 = lc_unitcost_02,	
                                                lc_pricecharge_02 = lc_pricecharge_02,	
                                                lc_units_02 = lc_units_02,	
                                                lc_cost_02 = lc_cost_02,	
                                                lc_revenue_02 = lc_revenue_02,	
                                                totalrevenue_02 = totalrevenue_02,	
                                                material_charge = material_charge,	
                                                artwork_fees = artwork_fees,	
                                                fixed_charges = fixed_charges,	
                                                total_discounts = total_discounts,	
                                                net_profits=net_profits)
            error="No"
        except Exception as e:
            print("-----",e)
            error="Yes"
    d={'error':error}
    return render(request,'add_project_cost_analysis.html',d)


def edit_project_cost_analysis(request,pid):
      
    error=""
    data = ProjectCostAnalysis.objects.get(project_id=pid)
    if request.method=='POST':
        
        project_name = 	request.POST['project_name']
        event_name	= request.POST['event_name']
        item_name = request.POST['item_name']	
        customer_name = request.POST['customer_name']	
        phonenumber	= request.POST['phonenumber']
        mc_item_01 = request.POST['mc_item_01']	
        mc_unitcost_01	= request.POST['mc_unitcost_01']
        mc_pricecharge_01 = request.POST['mc_pricecharge_01']
        mc_units_01	= request.POST['mc_units_01']
        mc_cost_01	= request.POST['mc_cost_01']
        mc_revenue_01 = request.POST['mc_revenue_01']
        mc_item_02	= request.POST['mc_item_02']
        mc_unitcost_02	= request.POST['mc_unitcost_02']
        mc_pricecharge_02 = request.POST['mc_pricecharge_02']	
        mc_units_02	= request.POST['mc_units_02']
        mc_cost_02 = request.POST['mc_cost_02']	
        mc_revenue_02 = request.POST['mc_revenue_02']	
        totalcost_01 = request.POST['totalcost_01']	
        totalrevenue_01	= request.POST['totalrevenue_01']
        lc_item_01 = request.POST['lc_item_01']	
        lc_unitcost_01 = request.POST['lc_unitcost_01']	
        lc_pricecharge_01 = request.POST['lc_pricecharge_01']	
        lc_units_01	= request.POST['lc_units_01']
        lc_cost_01	= request.POST['lc_cost_01']
        lc_revenue_01 = str(int(lc_cost_01)*int(lc_units_01))
        lc_item_02 = request.POST['lc_item_02']	
        lc_unitcost_02 = request.POST['lc_unitcost_02']	
        lc_pricecharge_02 = request.POST['lc_pricecharge_02']	
        lc_units_02	= request.POST['lc_units_02']
        lc_cost_02	= request.POST['lc_cost_02']
        lc_revenue_02 = str(int(lc_cost_02)*int(lc_units_02))
        totalrevenue_02 = request.POST['totalrevenue_02']	
        material_charge	= request.POST['material_charge']
        artwork_fees = request.POST['artwork_fees']	
        fixed_charges = request.POST['fixed_charges']	
        total_discounts	= request.POST['total_discounts']
        net_profits = request.POST['net_profits']

        #job.title = jt
        #job.company = com
        data.project_name = 	project_name
        data.event_name	= event_name
        data.item_name = item_name
        data.customer_name = customer_name
        data.phonenumber	= phonenumber
        data.mc_item_01 = mc_item_01
        data.mc_unitcost_01	= mc_unitcost_01
        data.mc_pricecharge_01 = mc_pricecharge_01
        data.mc_units_01	= mc_units_01
        data.mc_cost_01	= mc_cost_01
        data.mc_revenue_01 = mc_revenue_01
        data.mc_item_02	= mc_item_02
        data.mc_unitcost_02	= mc_unitcost_02
        data.mc_pricecharge_02 = mc_pricecharge_02	
        data.mc_units_02	= mc_units_02
        data.mc_cost_02 = mc_cost_02	
        data.mc_revenue_02 = mc_revenue_02
        data.totalcost_01 = totalcost_01
        data.totalrevenue_01	= totalrevenue_01
        data.lc_item_01 = lc_item_01
        data.lc_unitcost_01 = lc_unitcost_01
        data.lc_pricecharge_01 = lc_pricecharge_01
        data.lc_units_01	= lc_units_01
        data.lc_cost_01	= lc_cost_01
        data.lc_revenue_01 = str(int(lc_cost_01)*int(lc_units_01))
        data.lc_item_02 = lc_item_02
        data.lc_unitcost_02 = lc_unitcost_02	
        data.lc_pricecharge_02 = lc_pricecharge_02	
        data.lc_units_02	= lc_units_02
        data.lc_cost_02	= lc_cost_02
        data.lc_revenue_02 = str(int(lc_cost_02)*int(lc_units_02))
        data.totalrevenue_02 = totalrevenue_02
        data.material_charge	= material_charge
        data.artwork_fees = artwork_fees
        data.fixed_charges = fixed_charges
        data.total_discounts	= total_discounts
        data.net_profits = net_profits
        
        try:
            data.save()
            error="No"
        except:
            error="Yes"
    d={'error':error,'data':data} 
    return render(request,'edit_project_cost_analysis.html',d)

def view_project_cost_analysis(request,pid):
      
    work = ProjectCostAnalysis.objects.get(project_id=pid)
    d = {'data':work}
    return render(request,'view_project_cost_analysis.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

