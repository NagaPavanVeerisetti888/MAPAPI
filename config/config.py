import os
class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "your_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
    DB_NAME = os.getenv("DB_NAME", "your_db_name")
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://map-dev-api.azurewebsites.net/api/Access/GetUserAccessInfo')