from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.paginator import Paginator
import pandas as pd



def Userregistation(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'User data has been created successfully.')
                form.save()
                return redirect('register')
        else:
            form = RegistrationForm()
        return render(request, 'signup.html', {'forms':form})
    else:
        return redirect('index')
    


def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserAuthentication(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse("<h5>!Something done wrong, please try again.</h5>")
        else:
            form = UserAuthentication()                
        return render(request, 'login.html', {'forms':form})
    else:
        return redirect('index')



def Index(request):
    if request.user.is_authenticated:
        return render(request, 'app/index.html')
    else:
        return redirect('auth')
    
# Reports Start

def Reports_Hoto(request):
    if request.user.is_authenticated:
        return render(request, 'app/reports/hoto_report.html')
    else:
        return redirect('auth')

    
class DRFReport(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            pagination_fuel_report = EnergyFuel.objects.filter(Tasks='Diesel Filling and Energy Reading').order_by('-Date_Of_Diesel_Filling')
            paginator = Paginator(pagination_fuel_report, 50, orphans=1)
            page_number = request.GET.get('page')
            data_obj = paginator.get_page(page_number)
            context = {'fuel_report':data_obj, 'all_dfr_data':pagination_fuel_report}
            return render(request, 'app/reports/energy_report_drf.html', context)
        else:
            return redirect('auth')

            
class FuelDrawnReport(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            Pagination_fuel_drawn = FuelDrawn.objects.filter().order_by('-Fuel_Drawn_Date')
            paginator = Paginator(Pagination_fuel_drawn, 50, orphans=1)
            page_number = request.GET.get('page')
            data_obj = paginator.get_page(page_number)
            context = {'fuel_drawn':data_obj}
            return render(request, 'app/reports/energy_report_fuel_drawn.html', context)
        else:
            return redirect('auth')
            
            
class EnergyReadingReport(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            pagination_fuel_report = EnergyFuel.objects.filter(Tasks='Energy Reading').order_by('-Date_Of_Diesel_Filling')
            paginator = Paginator(pagination_fuel_report, 50, orphans=1)
            page_number = request.GET.get('page')
            data_obj = paginator.get_page(page_number)
            context = {'fuel_report':data_obj, 'all_dfr_data':pagination_fuel_report}
            return render(request, 'app/reports/energy_report_diesel_reading.html', context)
        else:
            return redirect('auth')
        


class EnergyDFRFilters(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            if request.GET.get('start_date') and request.GET.get('end_date'):
                start_date = request.GET.get('start_date')
                end_date = request.GET.get('end_date')
                fuel_report = EnergyFuel.objects.filter(Tasks='Diesel Filling and Energy Reading', Date_Of_Diesel_Filling__range=(start_date, end_date)).order_by('Date_Of_Diesel_Filling')
                return render(request, 'app/reports/energy_filters.html', {'fuel_report':fuel_report})
            elif request.GET.get('start_date'):
                start_date = request.GET.get('start_date')
                fuel_report = EnergyFuel.objects.filter(Tasks='Diesel Filling and Energy Reading', Date_Of_Diesel_Filling=start_date).order_by('Date_Of_Diesel_Filling')
                return render(request, 'app/reports/energy_filters.html', {'fuel_report':fuel_report})
            elif request.GET.get('end_date'):
                end_date = request.GET.get('end_date')
                fuel_report = EnergyFuel.objects.filter(Tasks='Diesel Filling and Energy Reading', Date_Of_Diesel_Filling=end_date).order_by('Date_Of_Diesel_Filling')
                return render(request, 'app/reports/energy_filters.html', {'fuel_report':fuel_report})
            else:
                return HttpResponse('<h5>Getting some error, Please write again. Back to <a href="/reports/energy-drf/">reports</a></h5>')
        else:
            return redirect('auth')
        

class EnergyReadingFilters(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            if request.GET.get('start_date') and request.GET.get('end_date'):
                start_date = request.GET.get('start_date')
                end_date = request.GET.get('end_date')
                fuel_report = EnergyFuel.objects.filter(Tasks='Energy Reading', Date_Of_Diesel_Filling__range=(start_date, end_date)).order_by('Date_Of_Diesel_Filling')
                return render(request, 'app/reports/energy_filters.html', {'fuel_report':fuel_report})
            elif request.GET.get('start_date'):
                start_date = request.GET.get('start_date')
                fuel_report = EnergyFuel.objects.filter(Tasks='Energy Reading', Date_Of_Diesel_Filling=start_date).order_by('Date_Of_Diesel_Filling')
                return render(request, 'app/reports/energy_filters.html', {'fuel_report':fuel_report})
            elif request.GET.get('end_date'):
                end_date = request.GET.get('end_date')
                fuel_report = EnergyFuel.objects.filter(Tasks='Energy Reading', Date_Of_Diesel_Filling=end_date).order_by('Date_Of_Diesel_Filling')
                return render(request, 'app/reports/energy_filters.html', {'fuel_report':fuel_report})
            else:
                return HttpResponse('<h5>Getting some error, Please write again. Back to <a href="/reports/energy-energy-reading/">reports</a></h5>')
        else:
            return redirect('auth')
        

class FuelDrawnFilters(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            if request.GET.get('start_date') and request.GET.get('end_date'):
                start_date = request.GET.get('start_date')
                end_date = request.GET.get('end_date')
                fuel_report = FuelDrawn.objects.filter(Fuel_Drawn_Date__range=(start_date, end_date)).order_by('Fuel_Drawn_Date')
                return render(request, 'app/reports/fuel_drawn_filter.html', {'fuel_drawn':fuel_report})
            elif request.GET.get('start_date'):
                start_date = request.GET.get('start_date')
                fuel_report = FuelDrawn.objects.filter(Fuel_Drawn_Date=start_date).order_by('Fuel_Drawn_Date')
                return render(request, 'app/reports/fuel_drawn_filter.html', {'fuel_drawn':fuel_report})
            elif request.GET.get('end_date'):
                end_date = request.GET.get('end_date')
                fuel_report = FuelDrawn.objects.filter(Fuel_Drawn_Date=end_date).order_by('Fuel_Drawn_Date')
                return render(request, 'app/reports/fuel_drawn_filter.html', {'fuel_drawn':fuel_report})
            else:
                return HttpResponse('<h5>Getting some error, Please write again. Back to <a href="/reports/energy-fuel-drawn/">reports</a></h5>')
        else:
            return redirect('auth')


# {% include 'app/tables/dfr_table.html' %}

# End Reports


# Start Forms

class DieselFillingOrReadingViews(TemplateView):
    def get(self, request):
        form = DieselFillingOrReadingForm()     
        context = {'forms':form}
        return render(request, 'app/forms/atcfillingform.html', context)
        
    def post(self, request):
        form = DieselFillingOrReadingForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            global_id = form.cleaned_data['global_id']                
            tasks = form.cleaned_data['Tasks']                
            DG_Serial_Number = form.cleaned_data['DG_Serial_Number']

            glb_id = str(global_id)
            last_data_1 = EnergyFuel.objects.filter(global_id=glb_id).order_by('-id').first()

            DG_HMR_Status = form.cleaned_data['DG_HMR_Status']
            if DG_HMR_Status == 'Working':
                DG_HMR_Reading = form.cleaned_data['DG_HMR_Reading']                                                                                                                                                                                                                                                                                                                                                                                                
            else:
                DG_HMR_Reading = 0

            DG_PIU_Status = form.cleaned_data['DG_PIU_Status']
            if DG_PIU_Status == 'Working':
                Current_DG_PIU_Reading = form.cleaned_data['Current_DG_PIU_Reading']
            else:
                Current_DG_PIU_Reading = 0

            Diesel_Filling_Done = form.cleaned_data['Diesel_Filling_Done']
            Date_Of_Diesel_Filling = form.cleaned_data['Date_Of_Diesel_Filling']

            if form.cleaned_data['Diesel_Balance_Before_Filling'] == '':                
                Diesel_Balance_Before_Filling = 0
            else:
                Diesel_Balance_Before_Filling = form.cleaned_data['Diesel_Balance_Before_Filling']

            if form.cleaned_data['Fuel_Qty_Filled'] == '':
                Fuel_Qty_Filled = 0
            else:
                Fuel_Qty_Filled = form.cleaned_data['Fuel_Qty_Filled']     

            Current_Diesel_Balance = 0
            dbbf = 0
            fqf = 0
            dbbf = int(Diesel_Balance_Before_Filling)
            fqf = int(Fuel_Qty_Filled)
            Current_Diesel_Balance = dbbf + fqf
            
            EB_Meter_Status = form.cleaned_data['EB_Meter_Status']
            if EB_Meter_Status == 'Working':
                Current_EB_MTR_KWH = form.cleaned_data['Current_EB_MTR_KWH']
            else:
                Current_EB_MTR_KWH = 0

            EB_PIU_Meter_Status = form.cleaned_data['EB_PIU_Meter_Status']
            if EB_PIU_Meter_Status == 'Working':
                Current_EB_PIU_Reading = form.cleaned_data['Current_EB_PIU_Reading']
            else:
                Current_EB_PIU_Reading = 0
            
            if form.cleaned_data['Total_DC_Load'] == '':
                Total_DC_Load = 0
            else:
                Total_DC_Load = form.cleaned_data['Total_DC_Load']

            if form.cleaned_data['Total_EB_KWH_Reading_from_all_Channels'] == '':
                Total_EB_KWH_Reading_from_all_Channels = 0
            else:
                Total_EB_KWH_Reading_from_all_Channels = form.cleaned_data['Total_EB_KWH_Reading_from_all_Channels']
            Remarks = form.cleaned_data['Remarks']
            FT_ID = form.cleaned_data['FT_ID']
            FT_name = form.cleaned_data['FT_name']
            FT_mobile_no = form.cleaned_data['FT_mobile_no']
            Receipt_No = form.cleaned_data['Receipt_No']
            Card_Number = form.cleaned_data['Card_Number']
            Vehicle_Plate = form.cleaned_data['Vehicle_Plate']
            Before_Fuel_CM_Photo = form.cleaned_data['Before_Fuel_CM_Photo']
            After_Fuel_Filling_CM_Photo = form.cleaned_data['After_Fuel_Filling_CM_Photo']
            
            if last_data_1 == None:
                # This is DG_Running_HRS:
                dghr = 0
                # This is CPH:
                dieselhmrdiv = 0
                # This is KWH:
                minKWHmtr = 0
                # This is CPH approved:
                div_last_cph = 0
            else:
                last_data = EnergyFuel.objects.filter(global_id=glb_id).order_by('-id').first()
                # This is DG_Running_HRS:
                HMR_read = int(last_data_1.DG_HMR_Reading)
                hmrread = int(DG_HMR_Reading)
                if hmrread < HMR_read:
                    if DG_HMR_Status == 'Working':
                        DG_HMR_Reading = form.cleaned_data['DG_HMR_Reading']
                    else:
                        DG_HMR_Reading = 0
                # This is DG hmr:
                DG_hr = int(DG_HMR_Reading)               
                dghr_int = int(last_data.DG_HMR_Reading)
                dg_hr = (DG_hr - dghr_int)
                dghr = str(dg_hr)
                if dghr[:1] == '-':
                    hr_dg_sum = dghr[1:]
                else:
                    hr_dg_sum = dghr

                # This is CPH:
                minus = 0
                lst_d_b = int(last_data.Fuel_Qty_Filled)
                current_d_b = int(last_data.Current_Diesel_Balance)
                minus = (current_d_b - lst_d_b)
                hmr = int(hr_dg_sum)
                diesel = int(minus)
                diesel_hmr_div = 0
                if hmr == 0 or diesel == 0:
                    diesel_hmr_div = 0
                else:
                    diesel_hmr_div = (diesel / hmr)   
                dieselhmrdiv = str(round(diesel_hmr_div, 2))  
                if dieselhmrdiv[:1] == '-':
                    cph_div = dieselhmrdiv[1:]
                else:
                    cph_div = dieselhmrdiv 

                # This is KWH:
                min_KWH_mtr = 0
                lst_kwh_mtr = int(last_data.Current_EB_MTR_KWH)
                present_mtr = int(Current_EB_MTR_KWH)
                min_KWH_mtr = (present_mtr - lst_kwh_mtr)
                minKWHmtr = str(min_KWH_mtr)
                if minKWHmtr[:1] == '-':
                    KWH_mtr = minKWHmtr[1:]
                else:
                    KWH_mtr = minKWHmtr

                # This is CPH approve by CPH:
                last_cph_div = 0
                lastcph_data = SiteFixed.objects.filter(global_id=glb_id).order_by('-global_id').first()
                last_approve_cph = float(lastcph_data.last_month_approved_CPH)
                last_cph_div = (diesel_hmr_div - last_approve_cph)
                div_with_last_cph = 0
                if last_approve_cph == 0 or last_cph_div == 0:
                    div_with_last_cph = 0
                else:
                    div_with_last_cph = (last_cph_div / last_approve_cph)
                div_last_cph = str(round(div_with_last_cph, 2))
                if div_last_cph[:1] == '-':
                    approved_cph_data = div_last_cph[1:]
                else:
                    approved_cph_data = div_last_cph
        
            reg = EnergyFuel(global_id=global_id,DG_Serial_Number=DG_Serial_Number,DG_HMR_Status=DG_HMR_Status,
            DG_HMR_Reading=DG_HMR_Reading,DG_PIU_Status=DG_PIU_Status,Current_DG_PIU_Reading=Current_DG_PIU_Reading,Diesel_Filling_Done=Diesel_Filling_Done,
            Date_Of_Diesel_Filling=Date_Of_Diesel_Filling,Diesel_Balance_Before_Filling=Diesel_Balance_Before_Filling,
            Fuel_Qty_Filled=Fuel_Qty_Filled,Current_Diesel_Balance=Current_Diesel_Balance,EB_Meter_Status=EB_Meter_Status,
            Current_EB_MTR_KWH=Current_EB_MTR_KWH,EB_PIU_Meter_Status=EB_PIU_Meter_Status,Current_EB_PIU_Reading=Current_EB_PIU_Reading,
            Tasks=tasks,Total_DC_Load=Total_DC_Load,Total_EB_KWH_Reading_from_all_Channels=Total_EB_KWH_Reading_from_all_Channels,
            Remarks=Remarks,FT_ID=FT_ID,FT_name=FT_name,FT_mobile_no=FT_mobile_no,Receipt_No=Receipt_No,Card_Number=Card_Number,
            Vehicle_Plate=Vehicle_Plate,Before_Fuel_CM_Photo=Before_Fuel_CM_Photo,After_Fuel_Filling_CM_Photo=After_Fuel_Filling_CM_Photo,
            DG_Running_HRS=hr_dg_sum, CPH_CPH_Comparison_With_Last_CPH=approved_cph_data, CPH=cph_div, EB_KWH=KWH_mtr)

            messages.success(request, 'Your data has been submitted successfully.')

            reg.save()

            return redirect('atcform')
        else:
            messages.error(request, 'Somethings went wrong, Please enter correct details.')
            
            return redirect('atcform')



class FuelDrawnViews(TemplateView):
    def get(self, request):
        form = FuelDrawnFTForm()
        fuel_drawn = FuelDrawn.objects.all() 
        context = {'forms':form, 'fuel_drawn':fuel_drawn}
        return render(request, 'app/forms/atc_fuel_drawn.html', context)
        
    def post(self, request):
        form = FuelDrawnFTForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            FT_ID = form.cleaned_data['FT_ID']
            FT_name = form.cleaned_data['FT_name']
            FT_mobile_no = form.cleaned_data['FT_mobile_no']
            Cluster_Name = form.cleaned_data['Cluster_Name']
            Fuel_Drawn_Date = form.cleaned_data['Fuel_Drawn_Date']
            Card_No = form.cleaned_data['Card_No']
            City_Township_Fuel_Station = form.cleaned_data['City_Township_Fuel_Station']
            Customer = form.cleaned_data['Customer']
            Fuel_Station_Name = form.cleaned_data['Fuel_Station_Name']
            Diesel_Purchased_Qty = form.cleaned_data['Diesel_Purchased_Qty']
            Diesel_Per_Ltr_Cost_Rs = form.cleaned_data['Diesel_Per_Ltr_Cost_Rs']
            Total_Diesel_Cost_Rs = int(Diesel_Purchased_Qty) * int(Diesel_Per_Ltr_Cost_Rs)
            Receipt_No = form.cleaned_data['Receipt_No']
            Receipt_Image_Upload = form.cleaned_data['Receipt_Image_Upload']
            Vehicle_Plate = form.cleaned_data['Vehicle_Plate']
            Remarks = form.cleaned_data['Remarks']

            reg = FuelDrawn(FT_ID=FT_ID,FT_name=FT_name,FT_mobile_no=FT_mobile_no,Cluster_Name=Cluster_Name,
            Fuel_Drawn_Date=Fuel_Drawn_Date,Card_No=Card_No,City_Township_Fuel_Station=City_Township_Fuel_Station,Customer=Customer,
            Fuel_Station_Name=Fuel_Station_Name,Diesel_Purchased_Qty=Diesel_Purchased_Qty,Diesel_Per_Ltr_Cost_Rs=Diesel_Per_Ltr_Cost_Rs,
            Total_Diesel_Cost_Rs=Total_Diesel_Cost_Rs,Receipt_No=Receipt_No,Receipt_Image_Upload=Receipt_Image_Upload,
            Vehicle_Plate=Vehicle_Plate,Remarks=Remarks)

            messages.success(request, 'Your data has been submitted successfully.')

            reg.save()

            return redirect('fueldrawnform')
        else:
            messages.error(request, 'Somethings went wrong, Please enter correct details.')

            return redirect('fueldrawnform')



# End Forms    
    

class LogOut(LogoutView):
    next_page = '/accounts/authentications/'