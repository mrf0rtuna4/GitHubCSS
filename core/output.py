import os

def build_svg(svg_content: str, output_file: str) -> None:
    """
    Write SVG content to a file
    """
    with open(output_file, 'w') as f:
        f.write(svg_content)
    print(f"SVG written to {output_file}")