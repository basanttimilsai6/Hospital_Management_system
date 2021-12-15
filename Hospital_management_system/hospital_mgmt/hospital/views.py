from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hospital.forms import DoctorForm

from hospital.models import Appointment, Doctor, Patient, Suggest
from .forms import DoctorForm,PatientForm,AppointmentForm

# Create your views here.
def About(request):
    return render(request, 'about.html')

    
def Home(request):
    return render(request, 'home.html')



def Contact(request):
    return render(request, 'contact.html')

def suggest(request):
    error = ''
    if request.method == 'POST':
        ema = request.POST['ema']
        txt = request.POST['txt']
        su = Suggest(email = ema , text = txt)
        su.save()
        error = 'no'
        return redirect('/')

# def Index(request):
#     if not request.user.is_staff:
#         return redirect('login')
#     return render(request, 'index.html')


def Login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(request, username = u, password = p)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("login")  


def View_Doctor(request):
    doc = Doctor.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    context = {'doc':doc}
    return render(request, "view_doctor.html", context)





def Delete_Doctor(request, id):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.get(id = id)
    doc.delete()
    return redirect("view_doctor")





def Add_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'add_doctor.html',{'form':form})


def Update_Doctor(request,id):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.get(id = id)
    form = DoctorForm(request.POST, instance=doc)
    if form.is_valid():
        form.save()
        return redirect('view_doctor')
    return render(request, "update_doctor.html", {'doc':doc})



#Patient


def View_Patient(request):
    doc = Patient.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    context = {'doc':doc}
    return render(request, "view_patient.html", context)





def Delete_Patient(request, id):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.get(id = id)
    doc.delete()
    return redirect("view_patient")





def Add_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'add_patient.html',{'form':form})


def Update_Patient(request,id):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.get(id = id)
    form = PatientForm(request.POST, instance=doc)
    if form.is_valid():
        form.save()
        return redirect('view_patient')
    return render(request, "update_patient.html", {'doc':doc})


#appointment
def Add_Appointment(request):
    error = ''
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method =='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor2 = Doctor.objects.filter(name=d).first()
        patient2 = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor2, patient=patient2, date=date, time=time)
            error = 'no'
        except:
            error = 'yes'
    params = {'doctor1':doctor1, 'patient1':patient1,'error':error}
    return render(request,'add_appointment.html',params)




    # form = AppointmentForm(request.POST or None)
    # params = {'form':form, 'doctor':doctor, 'patient':patient}
    # if form.is_valid():
    #     form.save()
    # return render(request,'add_appointment.html',params)




def Delete_Appointment(request, id):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appointment.objects.get(id = id)
    doc.delete()
    return redirect("view_appointment")



def View_Appointment(request):
    doc = Appointment.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    context = {'doc':doc}
    return render(request, "view_appointment.html", context)

def Update_Appointment(request,id):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    doc = Doctor.objects.get(id = id)
    patient = Patient.objects.all()
    form = AppointmentForm(request.POST, instance=doc)
    params = {'form':form, 'doctor':doctor, 'patient':patient, 'doc':doc}
    
    if form.is_valid():
        form.save()
        return redirect('view_appointment')
    return render(request, "update_appointment.html", params)