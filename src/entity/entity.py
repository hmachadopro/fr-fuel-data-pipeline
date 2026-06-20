from sqlalchemy import (
    Column, Integer, String, DateTime, Text, Numeric, func
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#Table Raw

class Raw(Base):
    __tablename__ = 'raw'
    # --- Clé technique et traçabilité (ajoutées par nous, absentes de l'API) ---
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(Integer, nullable=False)  # correspond au "id" de l'API
    ingested_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # --- Champs plats simples ---
    cp = Column(String(5), nullable=True)
    pop = Column(String(5), nullable=True)
    adresse = Column(String(255), nullable=True)
    ville = Column(String(255), nullable=True)
    departement = Column(String(100), nullable=True)
    code_departement = Column(String(5), nullable=True)
    region = Column(String(100), nullable=True)
    code_region = Column(String(5), nullable=True)
    # --- latitude/longitude brutes (string, format API, sans virgule) ---
    # Volontairement non castées ici : c'est le travail de Staging/dbt
    latitude_raw = Column(String(30), nullable=True)
    longitude_raw = Column(String(30), nullable=True)
    # --- Champs JSON imbriqués mais envoyés comme STRING par l'API ---
    # Stockés tels quels, sans parsing
    horaires = Column(Text, nullable=True)
    services = Column(Text, nullable=True)
    prix = Column(Text, nullable=True)
    rupture = Column(Text, nullable=True)
    # --- Champs JSON natifs renvoyés directement structurés par l'API ---
    geom = Column(JSONB, nullable=True)
    carburants_disponibles = Column(JSONB, nullable=True)
    carburants_indisponibles = Column(JSONB, nullable=True)
    services_service = Column(JSONB, nullable=True)
    # --- Prix et dates de mise à jour déjà aplatis par l'API, par carburant ---
    gazole_maj = Column(DateTime(timezone=True), nullable=True)
    gazole_prix = Column(Numeric(10, 3), nullable=True)
    sp95_maj = Column(DateTime(timezone=True), nullable=True)
    sp95_prix = Column(Numeric(10, 3), nullable=True)
    e85_maj = Column(DateTime(timezone=True), nullable=True)
    e85_prix = Column(Numeric(10, 3), nullable=True)
    gplc_maj = Column(DateTime(timezone=True), nullable=True)
    gplc_prix = Column(Numeric(10, 3), nullable=True)
    e10_maj = Column(DateTime(timezone=True), nullable=True)
    e10_prix = Column(Numeric(10, 3), nullable=True)
    sp98_maj = Column(DateTime(timezone=True), nullable=True)
    sp98_prix = Column(Numeric(10, 3), nullable=True)
    # --- Informations de rupture, aplaties par carburant ---
    e10_rupture_debut = Column(DateTime(timezone=True), nullable=True)
    e10_rupture_type = Column(String(50), nullable=True)
    sp98_rupture_debut = Column(DateTime(timezone=True), nullable=True)
    sp98_rupture_type = Column(String(50), nullable=True)
    sp95_rupture_debut = Column(DateTime(timezone=True), nullable=True)
    sp95_rupture_type = Column(String(50), nullable=True)
    e85_rupture_debut = Column(DateTime(timezone=True), nullable=True)
    e85_rupture_type = Column(String(50), nullable=True)
    gplc_rupture_debut = Column(DateTime(timezone=True), nullable=True)
    gplc_rupture_type = Column(String(50), nullable=True)
    gazole_rupture_debut = Column(DateTime(timezone=True), nullable=True)
    gazole_rupture_type = Column(String(50), nullable=True)
    # --- Champs texte variables (parfois liste ';' séparée, parfois absents) ---
    carburants_rupture_temporaire = Column(Text, nullable=True)
    carburants_rupture_definitive = Column(Text, nullable=True)
    # --- Horaires (incohérents en structure selon les stations) ---
    horaires_automate_24_24 = Column(String(10), nullable=True)
    horaires_jour = Column(Text, nullable=True)