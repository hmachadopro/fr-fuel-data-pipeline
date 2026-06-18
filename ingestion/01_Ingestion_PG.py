import requests

url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records/?lang=fr&limit=10&offset=0"
pagination = 100

response = requests.get(url)

ColumnToKeep = [
	"latitude",
	"longitude",
	"cp",
	"adresse",
	"ville",
	"geom",
	"gazole_maj",
	"gazole_prix",
	"e85_prix",
	"gplc_prix",
	"e10_prix",
	"sp95_prix",
	"sp98_prix",
	"carburants_disponibles",
	"carburants_indisponibles",
	"horaires_jour",
	"services_service"
]