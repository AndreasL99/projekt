import argparse
from cryptography.fernet import Fernet
import logging

# Konfigurera loggning för att spara loggar i UTF-8
log_handler = logging.FileHandler("verktygslåda.log", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logging.basicConfig(level=logging.INFO, handlers=[log_handler])

def load_key(keyfile):
    """Laddar krypteringsnyckel från en angiven fil."""
    try:
        with open(keyfile, 'rb') as file:
            key = file.read()
        logging.info(f"Krypteringsnyckel laddades från filen '{keyfile}'.")
        return key
    except Exception as e:
        logging.error(f"Fel vid laddning av krypteringsnyckel från '{keyfile}': {e}")
        raise

def encrypt_file(key, filename):
    """Krypterar innehållet i en fil med angiven krypteringsnyckel."""
    try:
        fernet = Fernet(key)
        with open(filename, 'rb') as file:
            data = file.read()
        encrypted = fernet.encrypt(data)
        with open(filename, 'wb') as file:
            file.write(encrypted)
        print(f"{filename} är nu krypterad.")
        logging.info(f"Filen '{filename}' krypterades.")
    except Exception as e:
        print(f"Fel vid kryptering av fil: {e}")
        logging.error(f"Fel vid kryptering av fil '{filename}': {e}")

def decrypt_file(key, filename):
    """Dekrypterar innehållet i en fil med angiven krypteringsnyckel."""
    try:
        fernet = Fernet(key)
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted = fernet.decrypt(encrypted_data)
        with open(filename, 'wb') as file:
            file.write(decrypted)
        print(f"{filename} är nu dekrypterad.")
        logging.info(f"Filen '{filename}' dekrypterades.")
    except Exception as e:
        print(f"Fel vid dekryptering av fil: {e}")
        logging.error(f"Fel vid dekryptering av fil '{filename}': {e}")

def main():
    """Huvudfunktion för att hantera kryptering och dekryptering."""
    parser = argparse.ArgumentParser(description="Krypteringsverktyg")
    parser.add_argument("operation", choices=["kryptera", "dekryptera"], help="Välj operation: kryptera eller dekryptera")
    parser.add_argument("keyfile", help="Filen som innehåller krypteringsnyckeln")
    parser.add_argument("filename", help="Filen som ska krypteras eller dekrypteras")
    args = parser.parse_args()

    try:
        key = load_key(args.keyfile)
        if args.operation == "kryptera":
            encrypt_file(key, args.filename)
        elif args.operation == "dekryptera":
            decrypt_file(key, args.filename)
    except Exception as e:
        print(f"Ett fel inträffade: {e}")
        logging.error(f"Ett fel inträffade under {args.operation} operationen: {e}")

if __name__ == "__main__":
    main()
