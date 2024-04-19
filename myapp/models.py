from django.db import models

class hospital(models.Model):
     Name = models.CharField(max_length=100,null=True)

class model_1(models.Model):
    hospital_Name = models.CharField(max_length=100,null=True)
    patient_Name = models.CharField(max_length=100,null=True)
    doctor_Name = models.CharField(max_length=100,null=True)
    Disease= models.CharField(max_length=100,null=True)
    specilization= models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=100,null=True)
    weight=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100,null=True)
    def _str_(self):
        return self.patient_Name

class model_2(models.Model):
    hospital_Name1 = models.CharField(max_length=100,null=True)
    patient_Name1 = models.CharField(max_length=100,null=True)
    doctor_Name1 = models.CharField(max_length=100,null=True)
    Disease1= models.CharField(max_length=100,null=True)
    specilization1= models.CharField(max_length=100,null=True)
    age1=models.CharField(max_length=100,null=True)
    weight1=models.CharField(max_length=100,null=True)
    gender1=models.CharField(max_length=100,null=True)
    qualification1=models.CharField(max_length=100,null=True)

    def _str_(self):
        return self.patient_Name

class model_3(models.Model):
    hospital_Name2 = models.CharField(max_length=100,null=True)
    patient_Name2 = models.CharField(max_length=100,null=True)
    doctor_Name2 = models.CharField(max_length=100,null=True)
    Disease2= models.CharField(max_length=100,null=True)
    specilization2= models.CharField(max_length=100,null=True)
    age2=models.CharField(max_length=100,null=True)
    weight2=models.CharField(max_length=100,null=True)
    gender2=models.CharField(max_length=100,null=True)
    qualification2=models.CharField(max_length=100,null=True)
    def _str_(self):
        return self.patient_Name