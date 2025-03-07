from django.shortcuts import render,redirect
from django.http import HttpResponse

from .form import ContactForm,RegisterForm,StudentForm

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from email.mime.image import MIMEImage



students = [
    {"id": 1, "name": "John Doe", "class": "10A", "add": "1234 Elm St"},
    {"id": 2, "name": "Jane Smith", "class": "9B", "add": "5678 Oak St"},
    {"id": 3, "name": "Sam Wilson", "class": "10C", "add": "9101 Pine St"},
    {"id": 4, "name": "Emily Davis", "class": "11A", "add": "2345 Maple St"},
    {"id": 5, "name": "Michael Brown", "class": "12B", "add": "6789 Birch St"},
    {"id": 6, "name": "Sophia Lee", "class": "9A", "add": "1122 Cedar St"},
    {"id": 7, "name": "David Miller", "class": "11B", "add": "3344 Willow St"},
    {"id": 8, "name": "Olivia Taylor", "class": "12A", "add": "5566 Pinewood St"},
    {"id": 9, "name": "Liam Martinez", "class": "10B", "add": "7788 Redwood St"},
    {"id": 10, "name": "Ava Wilson", "class": "9C", "add": "9900 Fir St"},
    {"id": 11, "name": "James Harris", "class": "10A", "add": "1234 Oakwood St"},
    {"id": 12, "name": "Isabella Clark", "class": "11C", "add": "3456 Hickory St"},
    {"id": 13, "name": "Mason Lewis", "class": "12C", "add": "7890 Aspen St"},
    {"id": 14, "name": "Mia White", "class": "9B", "add": "1357 Poplar St"},
    {"id": 15, "name": "Ethan Jackson", "class": "10C", "add": "2468 Sequoia St"},
    {"id": 16, "name": "Amelia Robinson", "class": "11A", "add": "3690 Chestnut St"},
    {"id": 17, "name": "Alexander Carter", "class": "12B", "add": "4812 Cedarwood St"},
    {"id": 18, "name": "Charlotte Evans", "class": "10B", "add": "5924 Ash St"},
    {"id": 19, "name": "Benjamin Walker", "class": "9A", "add": "6036 Redwood Dr"},
    {"id": 20, "name": "Harper King", "class": "11C", "add": "7148 Maplewood St"},
]


def index(request):
    return HttpResponse("Welcome Students")

def greeting(request,name):
    return HttpResponse("Welcome "+name)

def indexPage(request):

    page_name = 'Sony Site'
    title = 'Index'
    return render(request,"index.html",{"title":title,'name':page_name})


from .models import AboutModel
def about(request):
    text = AboutModel.objects.first().text

    return render(request,'about.html',{'text':text})

def find(request,num):
    if 0 < num < 4 :
        user_name = students[num - 1]
        return render(request,"index.html",{'name':user_name})
    else:
        user_name = "User NOT Fount"
        return render(request,"index.html",{'name':user_name})

def show_contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
    
        name = request.POST.get('name')
        email = request.POST.get('email')
        add = request.POST.get('add')
        
        if form.is_valid():
            response = HttpResponse("Form Submited ")
            return response
        
        return render(request,'contact.html',{'name':name,'email':email,'add':add})
    
    return render(request,'contact.html')

def index2(request):
    return render(request,"index2.html",{"students":students})

def home(req):
    return render(req,"home.html")

def projects(req):
    return HttpResponse("Projects")

def show_products(req):


    return render(req,"products.html",{"products":students})

def findbyid(req,id):
    student_detail = None
    for student in students :
        if student.get('id') == id :
            student_detail = student

    return render(req,'studentbyid.html',{'student':student_detail})

def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            return redirect("students:index")
    else:
        form = RegisterForm()
    return render(req,"register.html",{'form':form})

def student_reg(req):

    form = StudentForm()

    if req.method == 'POST' :
        form = StudentForm(req.POST)

        if form.is_valid():
            student = form.save(commit=False)
            send_email_with_image(req,student)
            student.save()
    
            return redirect("students:index")

    return render(req,'studentReg.html',{'form':form})

from django.core.mail import send_mail
def send_my_email(req):

    to = ['sumayya7202@gmail.com','anishsony1999@gmail.com','unniyabes12@gmail.com','sarathrahi077@gmail.com']
    subject = "Testing mail"
    text = "This message maybe show a test message from python django class"
    html = "<p style='color:red'> this is a <strong>test</strong> email </p>"

    send_mail(
        from_email="thamannasajeevan@gmail.com",
        message=text,
        subject= subject,
        recipient_list=to,
        html_message=html
        )
    return HttpResponse("Mail Send")

def send_email_with_image(req,student):
    subject = 'Test Email with  Image'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [student.email]

    msg = EmailMultiAlternatives(subject, "Message", from_email, recipient_list)

    html_content = f'''
    <html>
    <body>
        <h1>Vanakam D {student.name} </h1>
        <img src="cid:image1" alt="Image" width="200px"/>
    </body>
    </html>
    '''
    msg.attach_alternative(html_content, "text/html")

    image_path = './software-testing-course-scopeindia-2.jpg'

    with open(image_path, 'rb') as img:
        image = MIMEImage(img.read())
        image.add_header('Content-ID', '<image1>')

        msg.attach(image)


    msg.send()


