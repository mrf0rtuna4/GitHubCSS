import logging
from core.css import adapt_css
from core.view import render_svg
from core.output import build_svg

logging.basicConfig(level=logging.INFO)


def main() -> None:
    logging.info("Starting rendering process")

    with open('tests/page.html', 'r') as f:
        html_content = f.read()
    with open('tests/style.css', 'r') as f:
        css_content = f.read()

    adapted_css_content = adapt_css(css_content)
    svg_content = render_svg(html_content, adapted_css_content)
    build_svg(svg_content, 'output.svg')
    logging.info("Rendering process complete")


if __name__ == '__main__':
    main()
