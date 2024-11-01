import nmap
import argparse
import logging

# Konfigurera loggning för att spara loggar i UTF-8
log_handler = logging.FileHandler("verktygslåda.log", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[log_handler])

def scan_host(host):
    """Skannar en angiven värd och returnerar resultatet om det finns."""
    nm = nmap.PortScanner()
    logging.info(f"Startar skanning av värd: {host}")
    nm.scan(host, arguments='-Pn --unprivileged -v --reason')
    if host in nm.all_hosts():
        logging.info(f"Skanningsresultat mottaget för värd: {host}")
        return nm[host]
    else:
        logging.warning(f"Inga resultat hittades för värd: {host}")
        return None

def save_to_file(ip_address, result, filename):
    """Sparar skanningsresultatet för en IP-adress till en fil."""
    logging.info(f"Sparar skanningsresultatet för {ip_address} till filen '{filename}'.")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Skanningsresultatet för IP-adress: {ip_address}\n")
        if 'tcp' in result:
            for port, port_info in result['tcp'].items():
                file.write(f"Port {port}: status: {port_info['state']}, namn: {port_info['name']}\n")
        else:
            file.write("Inga tcp-portar hittades\n")
        file.write("\n")  # Lägger till en ny rad för tydlighet
    logging.info(f"Skanningsresultatet har sparats i '{filename}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Portscanner med Nmap")
    parser.add_argument("ip", help="IP-adress som ska skannas")

    args = parser.parse_args()

    # Skanna värden
    scan_result = scan_host(args.ip)

    if scan_result:
        print(f"Skanningsresultat för {args.ip}:")
        if 'tcp' in scan_result:
            for port in scan_result['tcp']:
                print(f"Port {port} status är: {scan_result['tcp'][port]['state']}, namn: {scan_result['tcp'][port]['name']}")
        else:
            print("Inga TCP-portar hittades.")

        # Spara resultat till fil
        output_file = f"{args.ip}_skanning.txt"
        save_to_file(args.ip, scan_result, output_file)
        print(f"Resultatet har sparats i {output_file}.")
    else:
        print(f"Inga resultat hittades för {args.ip}.")
