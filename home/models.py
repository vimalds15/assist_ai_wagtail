from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from .sections import header,navbar,hero,experience,unlimited,categories,future,integration,demo



class HomePage(Page):
    body = StreamField([
        ('header', header.HeaderSection()),
        ('navbar', navbar.NavbarSection()),
        ('hero', hero.HeroSection()),
        ('experience', experience.ExperienceSection()),
        ('unlimited', unlimited.UnlimitedSection()),
        ('categories', categories.CategoriesSection()),
        ('future', future.FutureSection()),
        ('integration', integration.IntegrationSection()),
        ('demo',demo.DemoSection())
    ],block_counts = {'header':{'max_num':1}},
    null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]
