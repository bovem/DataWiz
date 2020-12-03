from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Data
import csv
import os
from .utils import *
from .loader import Loader
import json
# from .var_dict import VarDict

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
    json_file = open('./calc/json_dumps/oplist.json', 'r')
    opList = json.load(json_file)
    json_file.close()

    if len(opList) == 0:
        opList = []

    media_files = getMediaFiles()
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

    # context = load_pkl('context')
    vardict = load_pkl('vardict')
    if vardict != None:
        varList = vardict.get_variables()
    else:
        varList = []
    context = {
        'files': media_files,
        'oplist': opList,
        'data': out,
        'headers': headers,
        'varlist': varList
    }
    print(opList)

    dump_to_pkl(context, 'context')
    
    # return render(request, 'home.html', {'files': lst, 'oplist': opList, 'data' :out , 'headers' : headers })
    return render(request, 'home.html',context= context )


def load_df(request):
    vardict = load_pkl('vardict')
    if vardict == None:
        l = Loader()
    else:
        l = Loader(vardict)
    if request.method == 'POST':
        filename = request.POST.get('filename')
        filetype = request.POST.get('filetype')
        varName = request.POST.get('variable')
        encoding = request.POST.get('encoding')

        l.load('./media/'+filename, varName)
        dump_to_pkl(l.vardict, 'vardict')

        context = getContext()
        context['loaderMsg'] = "File successfully loaded"
        return render(request, 'home.html', context=context)


def file_upload(request):
    # l = Loader()
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        save_file(uploaded_file)
        
        context = getContext()
        print(context['files'])
        context['loaderMsg'] = "File successfully loaded"
        return render(request, 'home.html', context=context)
        # redirect('/abc')
    return HttpResponse('uploaded')


def get_columns(request):
    obj = load_dump()
    print(obj)
    df = find_in_vardict(obj.vardict, 'test')['data']
    print(type(df))
    col_list = df.columns
    return HttpResponse(col_list)


def show_table(request):
    filename = request.GET.get('file')
    infile = open('./media/' + filename, 'r')
    reader = csv.DictReader(infile)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'table.html', {'data': out, 'headers': headers})


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
