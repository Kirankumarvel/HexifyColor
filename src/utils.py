import webcolors

def get_hex_code(color_name):
    """
    Converts a color name to its hex code.
    Args:
        color_name (str): The name of the color.
    Returns:
        str: Hexadecimal code of the color.
    Raises:
        ValueError: If the color name is not recognized.
    """
    try:
        return webcolors.name_to_hex(color_name.lower())
    except ValueError:
        return None
