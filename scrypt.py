import requests
from bs4 import BeautifulSoup

def collect_data(url):
    # Envoyer une requête HTTP à l'URL
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Parser le contenu HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraire les données souhaitées
        # Par exemple, ici on extrait tous les titres h1 de la page
        data = soup.find_all('h1')
        
        # Afficher les titres
        for item in data:
            print(item.get_text())
    else:
        print(f"Échec de la requête. Code de statut: {response.status_code}")

# URL du site web à scraper
url = 'https://example.com'

# Appeler la fonction
collect_data(url)
