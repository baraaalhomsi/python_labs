def validate_title(value: str) -> str:
    if not value or not isinstance(value, str) or value.strip() == "":
        raise ValueError("Title cannot be empty and must be a string.")
    return value.strip()

def validate_author(value: str) -> str:
    if not value or not isinstance(value, str) or value.strip() == "":
        raise ValueError("Author name cannot be empty.")
    return value.strip()

def validate_price(value: float) -> float:
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

def validate_file_size(value: float) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError("File size must be a number.")
    if value <= 0:
        raise ValueError("File size must be greater than zero.")
    return float(value)

def validate_duration(value: float) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError("Duration must be a number.")
    if value <= 0:
        raise ValueError("Duration must be greater than zero.")
    return float(value)

def validate_isbn(value: str) -> str:
    if not value or not isinstance(value, str) or value.strip() == "":
        raise ValueError("ISBN cannot be empty.")
    cleaned = value.strip().replace("-", "")
    if len(cleaned) not in [10, 13]:
        raise ValueError("ISBN must be 10 or 13 digits long.")
    return value.strip()