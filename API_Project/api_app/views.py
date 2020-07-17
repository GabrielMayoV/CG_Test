from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@csrf_exempt
def insert(request):
    if request.method == 'POST':
        data = request.body.decode('utf8')
        data = json.loads(data)
        # validaciones pendientes
        try:
            new_product = Product(name = data['name'], value = data['value'], discount_value = data['discount_value'], stock = data['stock'])
            new_product.save()
            return HttpResponse(json.dumps({'status':'OK'}), content_type = "application/json",status = 200)
        except:
            return HttpResponse(json.dumps({'status':'ERROR'}), content_type = "application/json",status = 422)

def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = {'products' : list(products.values('name','value','discount_value','stock'))}
        return JsonResponse(data)


# class insert(View):
#     def post(self,request):
#         data = request.body.decode('utf8')
#         data = json.loads(data)
#         # validaciones pendientes
#         try:
#             new_product = Product(name = data['name'],
#                                   value = data['value'],
#                                   discount_value = data['discount_value'],
#                                   stock = data['stock'])
#             new_product.save()
#             return HttpResponse(json.dumps({'status':'OK'}), content_type = "application/json",status_code = 200,safe=False)
#         except:
#             return HttpResponse(json.dumps({'status':'ERROR'}), content_type = "application/json",status_code = 422,safe=False)
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self,request, *args, **kwargs):
#         return super(insert, self).dispatch(request,*args,**kwargs)
