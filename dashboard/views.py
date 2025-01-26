from django.shortcuts import render, redirect
from .models import Bug
from .forms import BugForm
import pandas as pd
from django.db.models import Count
from datetime import datetime

# Home Page
def home(request):
    return render(request, 'dashboard/home.html')

# Add Bug
def add_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BugForm()
    return render(request, 'dashboard/add_bug.html', {'form': form})

# Upload Data
def upload_data(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
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
        return redirect('home')
    return render(request, 'dashboard/upload_data.html')

# Analytics
def analytics(request):
    total_bugs = Bug.objects.count()
    open_bugs = Bug.objects.filter(status='Open').count()
    resolved_bugs = Bug.objects.filter(status='Resolved').count()
    bugs_by_priority = Bug.objects.values('priority').annotate(count=Count('priority'))
    return render(request, 'dashboard/analytics.html', {
        'total_bugs': total_bugs,
        'open_bugs': open_bugs,
        'resolved_bugs': resolved_bugs,
        'bugs_by_priority': bugs_by_priority,
    })

