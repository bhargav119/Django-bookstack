from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    try:
        template_data = {}
        template_data['title'] = 'Books Store'
        return render(request, 'home/index.html', {'template_data': template_data})
    except Exception as e:
        logger.error(f"Error loading home index: {str(e)}")
        return render(request, 'home/index.html', {'template_data': {'title': 'Books Store', 'error': 'An error occurred loading the page.'}})

def about(request):
    try:
        template_data = {}
        template_data['title'] = 'About'
        return render(request, 'home/about.html', {'template_data': template_data})
    except Exception as e:
        logger.error(f"Error loading about page: {str(e)}")
        return render(request, 'home/about.html', {'template_data': {'title': 'About', 'error': 'An error occurred loading the page.'}})