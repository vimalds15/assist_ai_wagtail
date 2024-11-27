from wagtail import blocks

class DemoSection(blocks.StructBlock):
    demo_title = blocks.TextBlock(required=False)
    demo_description = blocks.TextBlock(required=False)
    demo_cta_text = blocks.TextBlock(required=False)
    demo_cta_url = blocks.URLBlock(required=False)

    class Meta:
        template = "sections/demo/demo.html"
        label = "Demo Section"
