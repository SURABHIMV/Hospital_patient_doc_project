from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import admin
from .models import hospital,model_1,model_2,model_3
import os
# Create your views here.
signup_data = {}
def signupPage_hospital(request):
    if request.method=='POST':
        hospitalname=request.POST.get('hospitalname')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
          signup_data[hospitalname] = password1
          print(signup_data)
          print('hospital',hospitalname,password1,password2)
          my_hospital=hospital.objects.create(Name=hospitalname)
          my_hospital.save()
          return redirect('login_hospital')
          #return HttpResponse("teacher data as been entered succesfully")
    return render(request,'signup_hospital.html')

def loginPage_hospital(request):
    if request.method=='POST':
        hospitalname=request.POST.get('hospitalname')
        password1=request.POST.get('password')
        stored_password = signup_data.get(hospitalname)
        print(hospitalname, password1)
        print('stored_password',stored_password)
        if stored_password == password1:
            if hospitalname=='hospital_1':
              return redirect('adding_doc_patients')
            elif  hospitalname=='hospital_2':
              return redirect('adding_doc_patients1')
            elif hospitalname=='hospital_3':
              return redirect('adding_doc_patients2')
        else:
            return HttpResponse("Username Or Password is incorrect")

    return render(request,'login_hospital.html')


def admin_dashboard1(request):
    models1= model_1.objects.all()
    context={'model1':models1}
    if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'add_patient':
                    patient_name = request.POST.get('patientname')
                    disease=request.POST.get('diseasename')
                    age=request.POST.get('age')
                    weight=request.POST.get('weight')
                    gender=request.POST.get('gender')
                    patient_hospital = model_1.objects.create(patient_Name=patient_name,Disease=disease,age=age,weight=weight,gender=gender)
                    patient_hospital.save()

            elif action == 'add_doctor':

                doctor_name= request.POST.get('doctorname')   
                specilization= request.POST.get('specializationname')    
                qualification= request.POST.get('qualification') 
                doctor_hospital = model_1.objects.create(doctor_Name=doctor_name,specilization=specilization,qualification=qualification)  
                doctor_hospital.save() 
    return render(request, 'adding_doc_patients.html',context)


def admin_dashboard2(request):
    
    models2= model_2.objects.all()
    context={'model2':models2}
    if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'add_patient':
                    patient_name = request.POST.get('patientname')
                    disease=request.POST.get('diseasename')
                    age=request.POST.get('age')
                    weight=request.POST.get('weight')
                    gender=request.POST.get('gender')
                    patient_hospital = model_2.objects.create(patient_Name1=patient_name,Disease1=disease,age1=age,weight1=weight,gender1=gender)
                    patient_hospital.save()

            elif action == 'add_doctor':

                doctor_name= request.POST.get('doctorname')   
                specilization= request.POST.get('specializationname')   
                qualification= request.POST.get('qualification')    
                doctor_hospital = model_2.objects.create(doctor_Name1=doctor_name,specilization1=specilization,qualification1=qualification)  
                doctor_hospital.save()    
    return render(request, 'adding_doc_patients1.html',context)


def admin_dashboard3(request):

    models3= model_3.objects.all()
    context={'model3':models3}
    if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'add_patient':
                    patient_name = request.POST.get('patientname')
                    disease=request.POST.get('diseasename')
                    age=request.POST.get('age')
                    weight=request.POST.get('weight')
                    gender=request.POST.get('gender')
                    patient_hospital = model_3.objects.create(patient_Name2=patient_name,Disease2=disease,age2=age,weight2=weight,gender2=gender)
                    patient_hospital.save()

            elif action == 'add_doctor':

                doctor_name= request.POST.get('doctorname')  
                specilization= request.POST.get('specializationname') 
                qualification= request.POST.get('qualification')       
                doctor_hospital = model_3.objects.create(doctor_Name2=doctor_name,specilization2=specilization,qualification2= qualification)  
                doctor_hospital.save()  
       
    return render(request, 'adding_doc_patients2.html',context)

