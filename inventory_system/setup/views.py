from django.shortcuts import render
from django.http import HttpResponse
from . import templates
from .models import Inventory
import pandas as pd

def login(request):
    return render(request,'login.html')

def forgot_password(request):
    return render(request, 'forgot-pass.html')

def index(request):
    return render(request, 'index.html')

def people(request):
    return render(request, 'people.html')

def inventory(request):
    if request.method == 'POST' and request.FILES.get('file'):
        excel_file = request.FILES['file']
        
        # Read the uploaded Excel file into a DataFrame
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            return HttpResponse(f"Error reading Excel file: {e}", status=400)
        
        # Iterate over DataFrame rows and create Inventory objects
        for index, row in df.iterrows():
            try:
                inventory_item = Inventory.objects.create(
                    date=row['INVENTORY DATE'],
                    number=row['INVENTORY NO.'],
                    description=row['ITEM DESCRIPTION'],
                    location=row['LOCATION'],  # Assuming 'LOCATION' is a column in the Excel file
                    status=row['STATUS']       # Assuming 'STATUS' is a column in the Excel file
                )
            except Exception as e:
                return HttpResponse(f"Error creating inventory item: {e}", status=400)
        
        # Fetch all inventory items from the database
        inventory_items = Inventory.objects.all()
        
        # Render the template with inventory items
        return render(request, 'inventory.html', {'inventory_items': inventory_items})

    return render(request, 'inventory.html')
