from logging.config import fileConfig
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from alembic import context

from app.core.config import settings
from app.db.models.base import Base  # Make sure this imports all models

# Alembic Config object
config = context.config

# Set DB URL from .env via config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


from sqlalchemy import create_engine

def run_migrations_online():
    connectable = create_engine(  # <-- SYNC engine here
        settings.DATABASE_URL.replace("+asyncpg", ""),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

        with context.begin_transaction():
            context.run_migrations()


# Decide which mode to run
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
