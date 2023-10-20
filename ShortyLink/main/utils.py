import secrets
import string
from main.models import ShortenedURL

def generate_unique_short_code():
    while True:
        # Generate a random 6-character code
        short_code = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
        # Check if it's unique
        if not ShortenedURL.objects.filter(short_code=short_code).exists():
            return short_code