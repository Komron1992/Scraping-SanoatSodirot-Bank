# SSB Currency Parser 🇹🇯

This script uses Selenium to scrape exchange rates (USD, EUR, RUB) from the official site of **Spitamen Bank (ssb.tj)**.

## 🔧 Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver (or use `webdriver-manager`)

## 📦 Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
```
▶️ Usage
```
python ssb.py
```
📌 Output Example
```
{'currency': 'USD', 'buy': '10.50', 'sell': '10.65'}
{'currency': 'EUR', 'buy': '11.30', 'sell': '11.50'}
```
❗ Notes
Headless mode is used for faster execution and automation.

Delay (time.sleep(3)) ensures that dynamic content is fully loaded.