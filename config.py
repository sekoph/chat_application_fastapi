
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    
    class config:
        env_file = ".env"