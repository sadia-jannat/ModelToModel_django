from django.shortcuts import redirect,render, get_object_or_404
from django.views import View

# all models and forms name add korar jonno * use kora jay
from .models import *
from .forms import *

#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse,json
from django.contrib import messages

#query ar jonno
from django.db.models import Q

# Create your views here.
#Now here view will create by class base view.previous all tasks use function base view.
class PersonDetails(View):
    
    def get(self, request, *args):
        
        allpersons=Person.objects.all()        #allpersons is main Person models ar details

        oneperson=Person.objects.get(id=1)     #oneperson is get id=1 person
        a=oneperson.personaddress              #model ar lower case name personaddress + use all person details variable.OnetoOne from Person to PersonAddress
        b_city=a.city
        c_stress=a.street_address

        
        persons=Person.objects.get(id=2)
        for personinterests in persons.interests.all():
            print(personinterests)
            print(personinterests.id)
        
        #persons means person id+details and personaddress holo model name but have to write lowercase.
        #person address ta nibo model neber por.(city) ar name
        personaddressdetails=persons.personaddress      
        address=personaddressdetails.city 
        street=personaddressdetails.street_address
        print("address :", address)   
        print("street :", street)
        
        print("name :",persons)
        print("name_id :",persons.id)
        #print("street_address :", persons.street_address)
        #try to range for total pk of personinterest.solve by terminal.but not solve by html
        nums=personinterests.id         #interest koyta ase Person model ar 2 no jon
        for num in range(nums):
            print(num)                   #koy ta interest tar num print hoy
       
        for kk in Person.objects.all():  #all person koy jon tadr name print hoy 
            print(kk)
            print(kk.pk)
            kkk=range(kk.pk)             #range(0,7) output mane 8 jon person ase
            print(kkk)
            for knum in kkk:
                print(knum)
        #cityofall= allpersons.personaddress   

        context={'persons':persons,
                 'personinterests':personinterests,
                 
                 'num':num,
                 'address':address,

                 'allpersons':allpersons,
                 'a':a,
                 'kk':kk,
                 
                 }
        
        return render(request, 'index.html', context)
    
class OneDetails(View):
    def get(self, request, id, *args):
        fe=Person.objects.get(id=id)
        fee=fe.personaddress
        context={'fee':fee}
        return render(request, 'one_by_one.html', context)
        
    
            