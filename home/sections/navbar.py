from wagtail import blocks
from wagtail.images.blocks import ImageBlock

class NavbarItemsBlock(blocks.StructBlock):
    navbar_item_title = blocks.TextBlock(required=False)
    navbar_item_has_child = blocks.BooleanBlock(required=False, default=False)
    navbar_item_id = blocks.CharBlock(required=False)

class NavbarSection(blocks.StructBlock):
    navbar_title = blocks.TextBlock(required=False)
    navbar_logo = ImageBlock(required=False)
    navbar_logo_url = blocks.URLBlock(required=False)
    navbar_items = blocks.ListBlock(NavbarItemsBlock())
    navbar_cta_text =  blocks.CharBlock(required=False)
    navbar_cta_url = blocks.URLBlock(required=False)

    class Meta:
        template = "sections/navbar/navbar.html"
        label = "Navbar"
    
    def __str__(self):
        return "Navbar"



