from django.shortcuts import render, redirect
from .models import Bug
from .forms import BugForm
import pandas as pd
from django.db.models import Count
from datetime import datetime
import matplotlib.pyplot as plt
import io
import urllib, base64


# Home Page
def home(request):
    return render(request, 'dashboard/home.html')


# Add Bug
def add_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm()
    return render(request, 'dashboard/add_bug.html', {'form': form})


# List Bugs
def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'dashboard/bug_list.html', {'bugs': bugs})


# Upload Data
def upload_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_extension = file.name.split('.')[-1].lower()

        if file_extension not in ['csv', 'xls', 'xlsx']:
            return render(request, 'dashboard/upload_data.html', {
                'error': 'Invalid file format. Please upload a CSV or Excel file.'
            })

        try:
            if file_extension == 'csv':
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            if df.empty:
                return render(request, 'dashboard/upload_data.html', {
                    'error': 'The file is empty.'
                })

            for _, row in df.iterrows():
                Bug.objects.create(
                    title=row.get('title', ''),
                    description=row.get('description', ''),
                    priority=row.get('priority', 'Low'),
                    status=row.get('status', 'Open'),
                    assigned_to=row.get('assigned_to', ''),
                    date_reported=row.get('date_reported', datetime.now())
                )

            return render(request, 'dashboard/upload_data.html', {
                'success': 'File uploaded successfully!'
            })

        except Exception as e:
            return render(request, 'dashboard/upload_data.html', {
                'error': f'An error occurred: {e}'
            })

    return render(request, 'dashboard/upload_data.html')


# Analytics View
def analytics(request):
    # Get bug data grouped by priority
    bug_data = Bug.objects.values('priority').annotate(count=Count('priority'))

    # Prepare data for the chart
    labels = [item['priority'] for item in bug_data]
    values = [item['count'] for item in bug_data]

    # Create bar chart
    plt.bar(labels, values, color='skyblue')
    plt.title('Bugs by Priority')
    plt.xlabel('Priority')
    plt.ylabel('Count')

    # Convert plot to image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'dashboard/analytics.html', {'chart': image})
