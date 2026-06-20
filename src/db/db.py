import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# --- Sélection du fichier .env selon le contexte d'exécution ---
# APP_ENV=docker est défini dans docker-compose.yml pour le service Airflow.
# En local (Windows, hors Docker), cette variable n'existe pas : on retombe sur .env.local
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # remonte depuis src/db/db.py jusqu'à la racine

if os.environ.get("APP_ENV") == "docker":
    ENV_FILE = PROJECT_ROOT / ".env.docker"
else:
    ENV_FILE = PROJECT_ROOT / ".env.local"

load_dotenv(dotenv_path=ENV_FILE)

DB_USER = os.environ["DATA_POSTGRES_USER"]
DB_PASSWORD = os.environ["DATA_POSTGRES_PASSWORD"]
DB_HOST = os.environ["DATA_POSTGRES_HOST"]  # "localhost" en local (.env.local) ou "postgres_data" en Docker (.env.docker)
DB_PORT = os.environ.get("DATA_POSTGRES_PORT", "5432")
DB_NAME = os.environ["DATA_POSTGRES_DB"]

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session():
    """Fournit une session SQLAlchemy, à fermer après usage."""
    session = SessionLocal()
    try:
        return session
    except Exception:
        session.close()
        raise