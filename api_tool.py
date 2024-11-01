import argparse
import requests
import logging

# Konfigurera loggning för att spara loggar i UTF-8
log_handler = logging.FileHandler("verktygslåda.log", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logging.basicConfig(level=logging.INFO, handlers=[log_handler])

def hämta_data_från_api(api_url):
    """Hämtar data från en angiven API-slutpunkt och sparar resultatet i en textfil."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Kontrollerar om statuskoden är 200
        data = response.json()
        
        filnamn = input("Ange filnamn för att spara datan (utan filändelse): ") + ".txt"
        with open(filnamn, 'w', encoding='utf-8') as fil:
            fil.write(str(data))
        
        print(f"Hämtad data har sparats i {filnamn}")
        logging.info(f"Data hämtades från {api_url} och sparades i '{filnamn}'.")
        
    except requests.exceptions.RequestException as e:
        print(f"Fel vid hämtning av data: {e}")
        logging.error(f"Fel vid hämtning av data från {api_url}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API-verktyg för att hämta data.")
    parser.add_argument("api_url", help="API-slutpunkt att hämta data från")
    args = parser.parse_args()
    
    hämta_data_från_api(args.api_url)
