from django.db import models
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
        context = super(HomePage, self).get_context(request)
        context['capstonepages'] = CapstonePage.objects.live().order_by('-first_published_at')
        return context 