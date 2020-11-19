from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Data
import csv 
import os
from .utils import save_file, dump_to_pkl, load_pkl, find_in_vardict, addCell
from .loader import Loader
import json

def home(request):
    path = "./media/"
    lst = os.listdir(path)

    filename = 'test.csv'
    infile = open('./media/' + filename, 'r')
    reader = csv.DictReader(infile)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    infile.close()


    opList = []
    json_file =  open('./calc/json_dumps/oplist.json', 'r')
    opList = json.load(json_file)
    json_file.close()
    print('aa' , opList)

    if len(opList) == 0:
        opList = []

    # if request.method == 'POST':
        
    #     print(opList)

    #     new_op = request.body
    #     new_op = new_op.decode('utf-8')
    #     new_op  = json.loads(new_op)
    #     new_op = new_op['cell']
    #     print(type(new_op))
    #     if len(opList) != 0:
    #         opList.append(new_op)
    #     else:
    #         opList = [new_op]
        
    #     with open('./calc/json_dumps/oplist.json','w') as json_file:
    #         json.dump(opList, json_file)

    #     print(opList)
    #     # return render(request, 'home.html', context={'files': lst, 'oplist': opList, 'data' :out , 'headers' : headers })
        
    #     return JsonResponse({'data' : 'success'})

    
    
        # return render(request, 'home.html', {'files': lst, 'oplist': opList, 'data' :out , 'headers' : headers })
    return render(request, 'home.html', context={'files': lst, 'oplist': opList, 'data' :out , 'headers' : headers })


def file_upload(request):
    l = Loader()
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        save_file(uploaded_file)
        # Data.objects.create(upload = my_file)
        l.load('./media/' + uploaded_file.name, uploaded_file.name.split('.')[0])
        # print(l.vardict.var_dict)
        dump_to_pkl(l, uploaded_file.name)
    return HttpResponse('uploaded')

def get_columns(request):
    obj = load_dump()
    print(obj)
    df = find_in_vardict(obj.vardict, 'test')['data']
    print(type(df))
    col_list = df.columns
    return HttpResponse(col_list)

def get_files(request):
    path = "./media/"
    lst = os.listdir(path)
    render_to_response('home.html', {'files': lst})

def show_table(request):
    filename = request.GET.get('file')
    infile = open('./media/' + filename, 'r')
    reader = csv.DictReader(infile)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'table.html', {'data' :out , 'headers' : headers})


def addCleaner(request): 
    addCell('cleaner')
    return redirect('/')

def addVisualizer(request): 
    addCell('visualiser')
    return redirect('/')

def addViewer(request):
    addCell('show')
    return redirect('/')

def addTransformer(request):
    addCell('transformer')
    return redirect('/')    
