from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from compendium.models import CapstonePage


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request): 
        """ This is necessary in order to obtain the items from CapstonePages""" 
        context = super(HomePage, self).get_context(request)

        # Get all the pages as a queryset
        all_resources = CapstonePage.objects.live().order_by('-first_published_at')

        # Show the first six 
        paginator = Paginator(all_resources, 6) 

        page = request.GET.get('page')

        try: 
            capstonepages = paginator.page(page)
        except PageNotAnInteger: 
            # if the page is not an integer, deliver the first page 
            capstonepages = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page of results 
            capstonepages = paginator.page(paginator.num_pages)
        # now make the capstonepages available on the template! 
        context['capstonepages'] = capstonepages
        return context 