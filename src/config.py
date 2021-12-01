import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SECRET_KEY = os.getenv("SECRET_KEY")
URI = os.getenv("DATABASE_URL")

if URI.startswith('postgres://'):
    URI = URI.replace('postgres://', 'postgresql://', 1)
