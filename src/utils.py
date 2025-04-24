import string
import random

def obfuscate_email_address(email: str) -> str:
    return "".join(
            character if character in ("@", ".")  else random.choice(string.ascii_letters + string.digits)
            for character in email
        )