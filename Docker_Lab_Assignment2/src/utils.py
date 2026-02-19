import datetime


def validate_input(name: str) -> bool:
    """
    Validates that the name is non-empty and contains only alphabetic characters.
    """
    if not name:
        return False

    return name.replace(" ", "").isalpha()


def generate_response(name: str) -> dict:
    """
    Generates a structured response with timestamp and formatted message.
    """
    timestamp = datetime.datetime.utcnow().isoformat()

    message = f"Hello {name}, welcome to the Dockerized MLOps service!"

    return {
        "message": message,
        "timestamp_utc": timestamp
    }
