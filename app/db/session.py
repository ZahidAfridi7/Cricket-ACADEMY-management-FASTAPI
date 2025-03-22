from databases import Database
from app.core.config import settings

# Async Database instance
database = Database(settings.DATABASE_URL)
