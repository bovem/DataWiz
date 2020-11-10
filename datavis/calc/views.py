from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
import csv 
import os
from .utils import save_file, dump_to_json, load_dump, find_in_vardict
from .loader import Loader

def home(request):
    path = "./media/"
    lst = os.listdir(path)
    return render(request, 'home.html', {'files': lst})

def file_upload(request):
    l = Loader()
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        save_file(uploaded_file)
        # Data.objects.create(upload = my_file)
        l.load('./media/' + uploaded_file.name, uploaded_file.name.split('.')[0])
        # print(l.vardict.var_dict)
        dump_to_json(l, uploaded_file.name)
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