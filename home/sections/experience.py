from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class ExperienceSection(blocks.StructBlock):
    experience_title = blocks.TextBlock(required=False)
    experience_subtitle = blocks.TextBlock(required=False)
    experience_question = blocks.TextBlock(required=False )
    experience_answer = blocks.TextBlock(required=False)
    experience_image = ImageChooserBlock(required=False)
    experience_image_url = blocks.URLBlock(required=False)
    image_alt_text = blocks.CharBlock(required=False, help_text="Optional alt text for the image")

    class Meta:
        template = "sections/experience/experience.html"
        label = "Experience Section"
