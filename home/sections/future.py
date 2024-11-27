from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class FutureCTABlock(blocks.StructBlock):
    future_cta = blocks.CharBlock(required=False)
    future_cta_url = blocks.URLBlock(required=False)

    class Meta:
        label = "Future CTA"  

class FutureSection(blocks.StructBlock):
    future_title = blocks.TextBlock(required=False)
    future_description = blocks.TextBlock(required=False)
    future_image = ImageChooserBlock(required=False)
    future_image_url = blocks.URLBlock(required=False)  
    future_cta_section = FutureCTABlock()

    class Meta:
        template = "sections/future/future.html" 
        label = "Future Section" 
