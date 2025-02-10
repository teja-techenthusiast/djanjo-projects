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
            return redirect('bug_list')  # Redirecting to bug list after submission
    else:
        form = BugForm()
    return render(request, 'dashboard/add_bug.html', {'form': form})


# List Bugs
def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'dashboard/bug_list.html', {'bugs': bugs})


# Upload Data
# Upload Data
def upload_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        # Validate file type
        if not file.name.endswith('.csv'):
            return render(request, 'dashboard/upload_data.html', {
                'error': 'Invalid file format. Please upload a CSV file.'
            })

        try:
            # Attempt to read the CSV file
            df = pd.read_csv(file)
            for _, row in df.iterrows():
                Bug.objects.create(
                    title=row['title'],
                    description=row['description'],
                    priority=row['priority'],
                    status=row['status'],
                    assigned_to=row['assigned_to'],
                    date_reported=datetime.strptime(row['date_reported'], '%Y-%m-%d')
                )
            return redirect('bug_list')  # Redirect to bug list on success
        except UnicodeDecodeError:
            return render(request, 'dashboard/upload_data.html', {
                'error': 'File encoding error. Please upload a valid CSV file encoded in UTF-8.'
            })
        except Exception as e:
            return render(request, 'dashboard/upload_data.html', {
                'error': f'An error occurred while processing the file: {str(e)}'
            })

    return render(request, 'dashboard/upload_data.html')


# Analytics + Charts
def analytics(request):
    total_bugs = Bug.objects.count()
    open_bugs = Bug.objects.filter(status='Open').count()
    resolved_bugs = Bug.objects.filter(status='Resolved').count()
    bugs_by_priority = Bug.objects.values('priority').annotate(count=Count('priority'))

    # Pie Chart
    labels = [b['priority'] for b in bugs_by_priority]
    sizes = [b['count'] for b in bugs_by_priority]

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['green', 'orange', 'red'])
    plt.title("Bugs by Priority")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'dashboard/analytics.html', {
        'total_bugs': total_bugs,
        'open_bugs': open_bugs,
        'resolved_bugs': resolved_bugs,
        'bugs_by_priority': bugs_by_priority,
        'chart': graphic
    })
