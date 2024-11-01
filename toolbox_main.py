import subprocess
import logging

# Konfigurera loggning för att spara loggar i UTF-8
log_handler = logging.FileHandler("verktygslåda.log", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logging.basicConfig(level=logging.INFO, handlers=[log_handler])

def generate_key():
    """Genererar och sparar en krypteringsnyckel."""
    keyfile = input("Ange filnamnet för att spara krypteringsnyckeln (ex. nyckel_fil.key): ")
    subprocess.run(["python", "generate_key.py", keyfile])
    logging.info(f"Nyckel genererad och sparad i filen '{keyfile}'.")

def encrypt_file():
    """Krypterar en fil med en angiven krypteringsnyckel."""
    keyfile = input("Ange filnamnet på krypteringsnyckeln (ex. nyckel_fil.key): ")
    filename = input("Ange filnamnet på filen som ska krypteras: ")
    subprocess.run(["python", "crypto_tool.py", "kryptera", keyfile, filename])
    logging.info(f"Fil '{filename}' krypterad med nyckeln i '{keyfile}'.")

def decrypt_file():
    """Dekrypterar en fil med en angiven krypteringsnyckel."""
    keyfile = input("Ange filnamnet på krypteringsnyckeln (ex. nyckel_fil.key): ")
    filename = input("Ange filnamnet på filen som ska dekrypteras: ")
    subprocess.run(["python", "crypto_tool.py", "dekryptera", keyfile, filename])
    logging.info(f"Fil '{filename}' dekrypterad med nyckeln i '{keyfile}'.")

def save_text_file():
    """Sparar användarens textinmatning i en angiven fil."""
    filename = input("Ange filnamnet för att spara texten (ex. textfil.txt): ")
    text = input("Skriv in texten som ska sparas: ")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Innehållet har sparats i {filename}.")
    logging.info(f"Text sparad i filen '{filename}'.")

def run_port_scanner():
    """Skannar en IP-adress och sparar resultaten till en fil."""
    ip_address = input("Ange IP-adress som ska skannas: ")
    subprocess.run(["python", "port_scanner.py", ip_address])
    logging.info(f"Portskanning utförd för IP-adressen '{ip_address}'.")

def run_api_tool():
    """Anropar en API-URL och sparar den hämtade datan till en fil."""
    api_url = input("Ange API-URL som ska anropas: ")
    subprocess.run(["python", "api_tool.py", api_url])
    logging.info(f"API-anrop utfört mot URL: '{api_url}'.")

def main_menu():
    """Visar huvudmenyn för verktygslådan och hanterar användarens val."""
    while True:
        print("\n--- Pentest verktygslåda ---")
        print("1. Portscanner")
        print("2. Krypteringsverktyg")
        print("3. API-verktyg")
        print("4. Avsluta")
        
        choice = input("Välj ett verktyg genom att skriva ett nummer: ")
        
        if choice == '1':
            run_port_scanner()
        elif choice == '2':
            crypto_tool_menu()
        elif choice == '3':
            run_api_tool()
        elif choice == '4':
            print("Avslutar programmet...")
            logging.info("Programmet avslutades av användaren.")
            break
        else:
            print("Ogiltigt val, försök igen.")
            logging.warning("Ogiltigt val i huvudmenyn.")

def crypto_tool_menu():
    """Visar menyn för krypteringsverktyg och hanterar användarens val."""
    while True:
        print("\n--- Krypteringsverktyg ---")
        print("1. Generera nyckel")
        print("2. Kryptera en fil")
        print("3. Dekryptera en fil")
        print("4. Skapa textfil")
        print("5. Tillbaka")
        
        choice = input("Välj ett alternativ: ")
        
        if choice == '1':
            generate_key()
        elif choice == '2':
            encrypt_file()
        elif choice == '3':
            decrypt_file()
        elif choice == '4':
            save_text_file()
        elif choice == '5':
            logging.info("Användaren återgick till huvudmenyn från krypteringsverktyg-menyn.")
            break
        else:
            print("Ogiltigt val, försök igen.")
            logging.warning("Ogiltigt val i krypteringsverktyg-menyn.")

if __name__ == "__main__":
    main_menu()
