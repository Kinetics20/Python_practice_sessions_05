import re


def is_valid_email(email: str) -> bool:
    """
    Validates whether the given email address is correctly formatted.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.

    Validation rules:
    - Must contain a local part and a domain part separated by '@'.
    - Local part can include letters, digits, dots, underscores, plus, and hyphens.
    - Domain must contain at least one dot and cannot have consecutive dots.
    - The top-level domain (TLD) must have at least two characters.
    """

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$'

    match = re.match(pattern, email)
    if match:
        local_part, domain = email.rsplit("@", 1)

        if ".." in domain:
            return False

        domain_parts = domain.split(".")
        if len(domain_parts[-1]) < 2:
            return False

        return True
    return False
