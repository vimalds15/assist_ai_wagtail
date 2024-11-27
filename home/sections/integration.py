from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class IntegrationSection(blocks.StructBlock):
    integration_title = blocks.TextBlock( required=False)
    integration_description = blocks.TextBlock(required=False)
    
    desktop_image = ImageChooserBlock(required=False)
    desktop_image_url = blocks.URLBlock(required=False)
    mobile_image = ImageChooserBlock(required=False)
    mobile_image_url = blocks.URLBlock(required=False)
    
    class Meta:
        template = "sections/integration/integration.html"
        label = "Integration Section"
