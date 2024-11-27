from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class CTAItemBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=False)
    cta_text = blocks.CharBlock(required=False)
    icon_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "link"  
        label = "CTA Item" 

class UnlimitedSection(blocks.StructBlock):
    unlimited_title = blocks.TextBlock(required=False)
    unlimited_description = blocks.TextBlock(required=False)

    ctas = blocks.ListBlock(CTAItemBlock(), required=False, help_text="Add as many CTAs as you want")

    class Meta:
        template = "sections/unlimited/unlimited.html"
        label = "Unlimited Section"
