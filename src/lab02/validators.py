def validate_title(value):
    if not value or not isinstance(value, str) or value.strip() == "":
        raise ValueError("Title cannot be empty and must be a string.")
    return value.strip()

def validate_author(value):
    if not value or not isinstance(value, str) or value.strip() == "":
        raise ValueError("Author name cannot be empty.")
    return value.strip()

def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Price must be a number.")
    if value <= 0:
        raise ValueError("Price must be greater than zero.")
    return float(value)

def validate_pages(value: int) -> int:
    if not isinstance(value, int):
        raise TypeError("Pages must be an integer.")
    if value <= 0:
        raise ValueError("Pages must be greater than zero.")
    return value