import argparse
from cryptography.fernet import Fernet
import logging

# Konfigurera loggning för att spara loggar i UTF-8
log_handler = logging.FileHandler("verktygslåda.log", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logging.basicConfig(level=logging.INFO, handlers=[log_handler])

def generate_key(keyfile):
    """Genererar en krypteringsnyckel och sparar den i en angiven fil."""
    try:
        key = Fernet.generate_key()
        with open(keyfile, 'wb') as file:
            file.write(key)
        print(f"Krypteringsnyckel har genererats och sparats i '{keyfile}'.")
        logging.info(f"Krypteringsnyckel genererades och sparades i '{keyfile}'.")
    except Exception as e:
        print(f"Fel vid generering av nyckel: {e}")
        logging.error(f"Fel vid generering av krypteringsnyckel: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generera en krypteringsnyckel.")
    parser.add_argument("keyfile", help="Filnamnet för att spara krypteringsnyckeln.")
    args = parser.parse_args()

    generate_key(args.keyfile)
