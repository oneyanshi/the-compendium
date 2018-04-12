from django import forms
from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


# Create your models here.
class CompendiumIndexPage(Page): 
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'), 
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        capstonepages = self.get_children().live().order_by('-first_published_at')
        context['capstonepages'] = capstonepages
        return context

class CompendiumTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        capstonepages = CapstonePage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['capstonepages'] = capstonepages
        return context

class CompendiumPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'CapstonePage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class CapstonePage(Page):
    # date = models.DateField("Post date")
    name = models.CharField(max_length=250)
    summary = RichTextField(blank=True, max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=CompendiumPageTag, blank=True)
    semester = models.CharField(max_length=250)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('body'),
        index.SearchField('semester'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('semester'),
            # FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Capstone information"),
        FieldPanel('summary'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    
class CapstonePageGalleryImage(Orderable):
    page = ParentalKey(CapstonePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
