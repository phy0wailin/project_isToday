from dataclasses import dataclass
from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    result = now.day == 14 and now.month == 3
    return render(request,"say/index.html", {
        "message": str(result).upper()
    })