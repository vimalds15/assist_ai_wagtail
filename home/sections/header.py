from wagtail import blocks
from wagtail.images.blocks import ImageBlock

class ProductBlock(blocks.StructBlock):
    product_title = blocks.CharBlock()  
    product_description = blocks.TextBlock() 
    product_url = blocks.URLBlock(required=False, default="https://www.happyfox.com/")
    product_image = ImageBlock(required=False)
    product_image_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "snippet"
        label = "Products"
    
    def __str__(self):
        return self.product_title

# class CategoryBlock(blocks.StructBlock):
#     category_name = blocks.CharBlock()
#     products = blocks.ListBlock(ProductBlock())

#     class Meta:
#         icon = "folder-open"
#         label = "Category"


class HeaderSection(blocks.StructBlock):
    header_logo = ImageBlock();
    header_logo_url = blocks.URLBlock();
    header_cta = blocks.CharBlock();

    header_products = blocks.ListBlock(ProductBlock())

    class Meta:
        template = "sections/header/header.html"
        label = "Header"
    
    def __str__(self):
        return "Header"



