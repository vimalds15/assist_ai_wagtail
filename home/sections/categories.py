from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class CategoryItemBlock(blocks.StructBlock):
    category_title = blocks.TextBlock(required=False)
    category_description = blocks.TextBlock(required=False)
    category_image = ImageChooserBlock(required=False)
    category_image_url = blocks.URLBlock(required=False)

    class Meta:
        icon = "image"  
        label = "Category Item"  


class CategoriesSection(blocks.StructBlock):
    categories = blocks.ListBlock(CategoryItemBlock(), required=False, help_text="Add as many categories as you want")

    class Meta:
        template = "sections/categories/categories.html" 
        label = "Categories Section"  