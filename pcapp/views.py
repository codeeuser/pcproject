import multiprocessing
import os
import platform
import socket
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import psutil

# Create your views here.
def index(request):
    virtual_memory = psutil.virtual_memory()
    return HttpResponse("Hello, world. You're at the polls index.")

def system_info(request):
    cpu_usage = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    available_memory = virtual_memory.available
    used_memory = virtual_memory.used
    used_memory_percent = virtual_memory.percent
    total = virtual_memory.total
    return render(request, 'system_info.html', {'cpu_usage': cpu_usage, 'total': total, 'available_memory': available_memory, 'used_memory': used_memory, 'used_memory_percent': used_memory_percent})    

def system_info_json(request):
    computer_name = platform.node()
    system_name = platform.system()
    
    if (system_name=='Windows'):
        system_version = platform.uname().version
        system_release = platform.uname().release
        system_architecture = platform.uname().machine
    else:    
        system_version = os.uname().version
        system_release = os.uname().release
        system_architecture = os.uname().machine

    
    num_cores = multiprocessing.cpu_count()

    cpu_usage = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    net_io_counters = psutil.net_io_counters()

    available_memory = virtual_memory.available
    used_memory = virtual_memory.used
    used_memory_percent = virtual_memory.percent
    total_memory = virtual_memory.total

    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    packets_sent = net_io_counters.packets_sent
    packets_recv = net_io_counters.packets_recv
    errin = net_io_counters.errin
    errout = net_io_counters.errout
    dropin = net_io_counters.dropin
    dropout = net_io_counters.dropout

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    data = {
        "system": {
            "computer_name": computer_name,
            "system_name": system_name,
            "system_version": system_version,
            "system_release": system_release,
            "system_architecture": system_architecture,
            "num_cores": num_cores,
        },
        "propeties": {
            "cpu_usage": cpu_usage,
            "available_memory": available_memory,
            "used_memory": used_memory,
            "used_memory_percent": used_memory_percent,
            "total_memory": total_memory,
        },
        "network": {
            "bytes_sent": bytes_sent,
            "bytes_recv": bytes_recv,
            "packets_sent": packets_sent,
            "packets_recv": packets_recv,
            "errin": errin,
            "errout": errout,
            "dropin": dropin,
            "dropout": dropout,
        },
        "host": {
            "hostname": hostname,
            "ip_address": ip_address,
        },
    }
    print(data)
    return JsonResponse(data, safe=False)