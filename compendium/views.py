from django.shortcuts import render
from compendium.models import CapstonePage
from wagtail.search.models import Query 

# Create your views here.

def search(request): 
    """For searching purposes""" 
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = CapstonePage.objects.live().search(search_query)
        
        # log the query so we can suggest promoted results 
        Query.get(search_query).add_hit()

    else: 
        search_results = Page.objects.none()

    
    return render(request, 'search.html', {
        'search_query': search_query,
        'search_results:', search_results
    })