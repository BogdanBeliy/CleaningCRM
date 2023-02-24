from pathlib import Path

import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))