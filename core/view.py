import svgwrite

def render_svg(html_content: str, css_content: str) -> str:
    """
    Render HTML and CSS content as an SVG
    """
    dwg = svgwrite.Drawing()
    dwg.add(dwg.rect(insert=(0, 0), size=(100, 100), fill='white'))
    dwg.add(dwg.html(html_content, insert=(10, 10)))
    dwg.add(dwg.style(css_content))
    return dwg.tostring()