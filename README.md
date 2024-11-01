
# Pentest Verktygslåda

Detta är en samling av flera Python-verktyg designade för penetrationstestning, organiserade i en verktygslåda med flera funktioner.

## Verktyg och användning

### 1. crypto_tool.py
Detta verktyg används för att kryptera och dekryptera filer.

**Användning:**
```bash
python crypto_tool.py kryptera <keyfile> <filename>  # Kryptera en fil
python crypto_tool.py dekryptera <keyfile> <filename>  # Dekryptera en fil
```
- `<keyfile>`: Filen som innehåller krypteringsnyckeln.
- `<filename>`: Filen som ska krypteras eller dekrypteras.

### 2. generate_tool.py
Genererar en krypteringsnyckel och sparar den i en fil.

**Användning:**
```bash
python generate_tool.py <keyfile>
```
- `<keyfile>`: Filnamnet där krypteringsnyckeln ska sparas.

### 3. port_scanner.py
Portscanner som använder Nmap för att skanna en angiven IP-adress.

**Användning:**
```bash
python port_scanner.py <ip>
```
- `<ip>`: IP-adressen som ska skannas.

### 4. api_tool.py
Hämtar data från en API-slutpunkt och sparar den i en textfil.

**Användning:**
```bash
python api_tool.py <api_url>
```
- `<api_url>`: API-URL att hämta data från.

### 5. toolbox_main.py
Huvudmenyn för verktygslådan där du kan välja att köra något av verktygen ovan.

**Användning:**
```bash
python toolbox_main.py
```
Efter att ha kört `toolbox_main.py` kommer huvudmenyn att visas, och du kan välja det verktyg du vill använda:

1. Portscanner
2. Krypteringsverktyg (med val för nyckelgenerering, kryptering, och dekryptering)
3. API-verktyg
4. Avsluta

## Loggning
Alla verktyg loggar sina aktiviteter i filen `verktygslåda.log` för felsökning och referens.

## Krav
- Python 3.x
- `cryptography`,`nmap` och `requests`-biblioteket för vissa verktyg (kan installeras med `pip install cryptography requests nmap`)

