from django.urls import path
from .views import *

urlpatterns=[
    path('first/',first),
    path('second/',second),
    path('third/',third),
    path('another/',another),
    path('fourth/',fourth),
    path('fifth/',fifth),
    path('register/',register),
    path('loginpage/',loginpage),
    path('employee/',employee),
    path('check/',check),
    path('display/',display),
    path('employdisplay/',employdisplay),
    path('fileupload/',fileupload),
    path('card/',card),
    path('filedisplay/',filedisplay),
    path('carddisplay/',carddisplay),
    path('edit/<int:id>',edituser),
    path('delete/<int:id>',deleteuser),
    path('edit1/<int:id>',employedit),
    path('delete1/<int:id>',employdelete),
    path('editproduct/<int:id>',editproduct),
    path('deleteproduct/<int:id>',deleteproduct),
    path('editcard/<int:id>',editcard),
    path('deletecard/<int:id>',deletecard),

    path('index/',index),
    path('logo/',logo),
    path('Registration/',Registration),

    path('xamfile/',xamfile),
    path('xamdisplay/',xamdisplay),
    path('edit2/<int:id>',editxam),
    path('delete2/<int:id>',deletexam),





]