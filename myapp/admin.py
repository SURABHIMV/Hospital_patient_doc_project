from django.contrib import admin
from .models import hospital,model_1,model_2,model_3
from django.utils.html import format_html

# Register your models here.
class hospitalAdmin(admin.ModelAdmin):
    list_display = ['Name']
admin.site.register(hospital,hospitalAdmin)

class model11(admin.ModelAdmin):
    list_display = ['hospital_Name','patient_Name','doctor_Name','Disease','specilization','age','weight','gender','qualification']
admin.site.register(model_1,model11)

class model22(admin.ModelAdmin):
    list_display = ['hospital_Name1','patient_Name1','doctor_Name1','Disease1','specilization1','age1','weight1','gender1','qualification1']
admin.site.register(model_2,model22)
class model33(admin.ModelAdmin):
    list_display = ['hospital_Name2','patient_Name2','doctor_Name2','Disease2','specilization2','age2','weight2','gender2','qualification2']
admin.site.register(model_3,model33)