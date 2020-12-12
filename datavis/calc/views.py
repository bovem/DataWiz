from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, FileResponse
from django.utils.encoding import smart_str

from .models import Data
import csv
import os
from .utils import *
from .loader import Loader
import json
from .exporter import Exporter
from .var_dict import VarDict
from .processor import Processor
from .cleaner import Cleaner
# from .modules.cleaner import *
# from .var_dict import VarDict


def home(request):
    path = "./media/"
    lst = os.listdir(path)

    context = getContext()

    return render(request, 'home.html', context=context)


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
        context['currentCell'] = 'loader'
        dump_to_pkl(context, 'context')
        # return render(request, 'home.html', context=context)
        return redirect('/')

def file_upload(request):
    # l = Loader()
    uploaded_file = []
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        save_file(uploaded_file)

        context = getContext()
        print(context['files'])
        context['loaderMsg'] = "File successfully loaded"
        context['currentCell'] = 'loader'
        # return render(request, 'home.html', context=context)
        # redirect('/abc')
    return HttpResponse(status=200)


def cleaner(request):
    if request.method == 'GET':
        return redirect('/')
    operation = request.POST['operation']
    cellname = request.POST['cellname']
    var_name = request.POST['varname']
    new_var_name = request.POST['new_varname']
    inplace = False
    if new_var_name == None or new_var_name == '':
        inplace = True

    
    opdata = load_json('opdata')
    set_cell_data(opdata, cellname, 'varname', var_name)
    # set_cell_data(opData, cellname, 'operation', operation)
    set_cell_data(opdata, cellname, 'new_varname', new_var_name)
    dump_to_json(opdata, 'opdata')
    
    vardict = load_pkl('vardict')
    c = Cleaner(vardict)

    if operation == "remove-null-value":
        c.remove_null(var_name, inplace, new_var_name)
    elif operation == "fill-mean":
        c.fill_mean(var_name, inplace, new_var_name)
    elif operation == "fill-median":
        c.fill_median(var_name, inplace, new_var_name)
    elif operation == "fill-forward":
        c.fill_forward(var_name, inplace, new_var_name)
    elif operation == 'fill-backward':
        c.fill_backward(var_name, inplace, new_var_name)
    
    operation_msg = 'Operation has been applied successfully'
    set_cell_data(opdata, cellname, 'msg', operation_msg)

    context = getContext()
    context['currentCell'] = cellname
    context['opdata'] = opdata

    return render(request, 'home.html', context)

def transformer(request):
    varname = request.POST['varname']
    new_varname = request.POST['new_varname']
    col_name = request.POST['col_name']
    operation = request.POST['operation']
    cell_name = request.POST['cellname']

    opdata = load_json('opdata')

    set_cell_data(opdata, cell_name, 'varname', varname)
    set_cell_data(opdata, cell_name, 'new_varname', new_varname)
    set_cell_data(opdata, cell_name, 'col_name', col_name)
    # set_cell_data(opData, cell_name, 'operation', operation)

    dump_to_json(opdata, 'opdata')
    var_dict = load_pkl('vardict')
    p = Processor(var_dict)
    if operation == 'one-hot-encoding':
        p.onehotencoder(varname, col_name, True, new_varname)
    elif operation == 'normalizer':
        p.normalize(varname, col_name, True, new_varname)
    elif operation == 'standardizer':
        p.standardizer(varname, col_name, True, new_varname)
    
    operation_msg = 'Operation has been applied successfully'
    set_cell_data(opdata, cell_name, 'msg', operation_msg)
    dump_to_pkl(p.vardict, 'vardict')
    context = getContext()
    context['opdata'] = opdata
    context['currentCell'] = cell_name
    return render(request, 'home.html', context)


def viewer(request):
    var_name = request.POST['varname']
    cellname = request.POST['cellname']
    vardict = load_pkl('vardict')
    print(cellname)
    if var_name != None:
        df = find_in_vardict(vardict, var_name)['data']
        opdata = load_json('opdata')
        set_cell_data(opdata, cellname, 'varname', var_name)
        header = [col for col in df.columns]
        data = [[df.iloc[i][col] for col in df.columns]
                for i in range(len(df))]

        context = load_pkl('context')
        context['currentCell'] = cellname
        context['headers'].update({cellname : header})
        context['data'].update({cellname: data})
        
        dump_to_pkl(context, 'context')
        dump_to_json(opdata, 'opdata')
    return redirect('/')
    # return render(request,'home.html', context=context)


def exporter(request):
    vardict = load_pkl('vardict')
    e = Exporter(vardict)

    varname = request.POST['varname']
    filename = request.POST['filename']
    file_type = request.POST['filetype']

    if file_type == 'json':
        e.export_json(varname, filename)
    elif file_type == 'csv':
        e.export_csv(varname, filename)

    with open('./media/downloads/'+filename + '.'+file_type, 'r') as fh:
        download_file = fh.read()
    response = HttpResponse(
        download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(
        filename+'.'+file_type)

    return response

def joiner(request):
    varname1 = request.POST.get('varname')
    varname2 = request.POST.get('varname-2')
    new_varname = request.POST.get('new_varname')
    cellname = request.POST.get('cellname')

    opdata = load_json('opdata')
    set_cell_data(opdata, cellname, 'varname', varname1)
    set_cell_data(opdata, cellname, 'varname2', varname2)
    set_cell_data(opdata, cellname, 'new_varname', new_varname)

    setContext('cellname', cellname)
    vardict = load_pkl('vardict')
    c = Cleaner(vardict)
    c.joiner(varname1, varname2, True,new_varname)
    dump_to_pkl(c.vardict,'vardict')
    dump_to_json(opdata, 'opdata')

    return redirect('/')


def show_table(request):
    v = load_pkl('vardict')
    varname = request.GET.get('varname')
    data = v.show_data(varname)
    # data = json.dumps(data)
    data = data.reset_index().to_json(orient='split')
    
    data = json.loads(data)
    # html_file = open('./templates/tale.html','w')
    # html_file.write(data)
    # html_file.close()
    # return HttpResponse(data) 
    return render(request, 'tale.html', {'data':data.values})


def addCleaner(request):
    addCell('cleaner')
    return redirect('/')

def addJoiner(request):
    addCell('joiner')
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


def addExporter(request):
    addCell('exporter')
    return redirect('/')

def resetAll(request):
    # vardict = load_pkl('vardict')
    vardict = VarDict()
    dump_to_pkl(vardict, 'vardict')
    opdata = []
    dump_to_json(opdata, 'opdata')
    context = {}
    context['headers'] = {}
    context['data'] = {}
    dump_to_pkl(context, 'context')

    return redirect('/')