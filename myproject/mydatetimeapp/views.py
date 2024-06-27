from django.shortcuts import render
import pytz
from datetime import datetime,timedelta
def current_datetime(request):
    utc=pytz.utc
    ist=pytz.timezone('Asia/Kolkata')
    datetime_utc=datetime.now(utc)
    datetime_ist=datetime.now(ist)
    formatted_utc=datetime_utc.strftime("%Y-%m-%d %H:%M:%S%Z%z")
    formatted_ist=datetime_ist.strftime("%Y-%m-%d %H:%M:%S%Z%z")
    context={
        'utc':formatted_utc,
        'ist':formatted_ist
    }
    return render(request,'current_datetime.html',context)
    
