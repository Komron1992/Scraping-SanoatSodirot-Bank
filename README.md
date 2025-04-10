# 💱 Currency Parser from eskhata.com

A simple Python script that scrapes the current exchange rates for USD, EUR, and RUB from [eskhata.com](https://eskhata.com/), the official site of Eskhata Bank.

The script uses `requests`, `fake-useragent`, and `BeautifulSoup` for HTML parsing.

---

## 🚀 Features

- 📊 Retrieves current exchange rates for:
  - US Dollar (USD)
  - Euro (EUR)
  - Russian Ruble (RUB)
- ✅ Parses buy, sell, and NBT rates
- 💻 Easy to run and extend

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/eskhata-currency-parser.git
cd eskhata-currency-parser
2. Install dependencies
Using requirements.txt:

pip install -r requirements.txt
Or install manually:

pip install requests fake-useragent beautifulsoup4 lxml

🧪 Usage
Simply run the script:

python eskhata.py

You’ll get a result like this:
{
  'usd': {'currency': 'US Dollar', 'buy': '10.90', 'sell': '11.10', 'nbt': '11.00'},
  'eur': {'currency': 'Euro', 'buy': '11.80', 'sell': '12.00', 'nbt': '11.90'},
  'rur': {'currency': 'Russian Ruble', 'buy': '0.12', 'sell': '0.14', 'nbt': '0.13'}
}

🛠 Built With
Python 3
requests
fake-useragent
beautifulsoup4
lxml

⚠️ Notes
If the HTML structure of eskhata.com changes, the script may need to be updated.
fake-useragent may occasionally fail. If so, you can replace it with a static user-agent string.

👨‍💻 Author
Telegram: @kemeron1992
GitHub: github.com/Komron1992