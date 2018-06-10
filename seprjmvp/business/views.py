from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from .forms import BusinessForm, EmployeeForm
from .models import Business, Employee
from django.shortcuts import render


# Create your views here.

def create(request):
    form = BusinessForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.owner = request.user
        post.save()
        form = BusinessForm()
        return HttpResponseRedirect('/business/create')

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('business/create_business.html', args)


def addemployee(request, business_name):
    form = EmployeeForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.business = Business.objects.get(name=business_name)
        post.user_id = post.user_id[0]
        post.save()
        form = EmployeeForm()
        return HttpResponseRedirect('/business/create')

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('business/add_employee.html', args)


def all_businesses(request):
    businesses = Employee.objects.all()

    context = {
        'businesses': businesses,
    }

    return render(request=request, template_name='business/all_businesses.html', context=context)

