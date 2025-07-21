from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_currency_data_ssb():
    options = Options()
    options.add_argument('--headless')  # Run browser in headless mode (no GUI)
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    url = "https://www.ssb.tj/ru/?type=1"
    driver.get(url)
    time.sleep(3)  # Wait for the page to fully load

    # Get main data blocks
    main_blocks = driver.find_elements(By.CLASS_NAME, "main_block")
    if len(main_blocks) < 3:
        driver.quit()
        raise Exception("Not enough .main_block elements found")

    # Extract currency codes
    currency_block = main_blocks[0]
    currency_codes = [el.text.strip() for el in currency_block.find_elements(By.TAG_NAME, "p") if el.text.strip() in ["USD", "EUR", "RUB"]]

    # Extract buy rates
    buy_block = main_blocks[1]
    buy_rates = [el.text.strip() for el in buy_block.find_elements(By.TAG_NAME, "p") if el.text.strip().replace(".", "").replace(",", "").isdigit()]

    # Extract sell rates
    sell_block = main_blocks[2]
    sell_rates = [el.text.strip() for el in sell_block.find_elements(By.TAG_NAME, "p") if el.text.strip().replace(".", "").replace(",", "").isdigit()]

    # Combine the data
    rates = []
    for i in range(len(currency_codes)):
        rates.append({
            "currency": currency_codes[i],
            "buy": buy_rates[i] if i < len(buy_rates) else None,
            "sell": sell_rates[i] if i < len(sell_rates) else None
        })

    driver.quit()
    return rates

# Example usage
if __name__ == "__main__":
    data = fetch_currency_data_ssb()
    for item in data:
        print(item)
