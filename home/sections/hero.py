from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeroTextBlock(blocks.StructBlock):
    hero_text = blocks.TextBlock(required=False)
    hero_subtext = blocks.TextBlock(required=False )

    class Meta:
        icon = "title"
        label = "Hero Text Block"

class HeroImageBlock(blocks.StructBlock):
    hero_image = ImageChooserBlock(required=False)
    hero_image_url = blocks.URLBlock(required=True)
    image_width = blocks.IntegerBlock(required=False, default=677)
    image_height = blocks.IntegerBlock(required=False, default=519)

    class Meta:
        icon = "image"
        label = "Hero Image Block"

class HeroCTAInputBlock(blocks.StructBlock):
    input_placeholder = blocks.CharBlock(required=False, default="Enter your work email")
    cta_text = blocks.CharBlock(required=False, default="Get a Demo")

    class Meta:
        icon = "form"
        label = "Hero CTA Input Block"

class HeroVideoCTABlock(blocks.StructBlock):
    video_cta_text = blocks.CharBlock(required=False, default="Watch the video")
    video_image = ImageChooserBlock(required=False)
    video_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "media"
        label = "Hero Video CTA Block"

class HeroSection(blocks.StructBlock):
    hero_text_section = HeroTextBlock()
    hero_image_section = HeroImageBlock()
    hero_cta_section = HeroCTAInputBlock()
    hero_video_cta_section = HeroVideoCTABlock()

    class Meta:
        template = "sections/hero/hero.html"
        label = "Hero"

    def __str__(self):
        return "Hero Section"
