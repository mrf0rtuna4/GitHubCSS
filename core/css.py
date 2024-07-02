import cssutils

def adapt_css(css_content: str) -> str:
    """
    Adapt CSS content for rendering
    """
    sheet = cssutils.parseString(css_content)
    for rule in sheet.cssRules:
        if rule.type == rule.STYLE_RULE:
            # TODO:
            # Маке adaptive represent styles
            rule.style.removeProperty('margin')
            rule.style.removeProperty('padding')
    return sheet.cssText