from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


brands = []
model_names = []
screen_sizes = []
rams = []
storages = []
cpu_models = []
operating_systems = []
prices = []
ratings = []
review_counts = []
graphics_cards = []

pages_to_scrape = 8
url = 'https://www.amazon.in/s?k=laptops'

for i in range(pages_to_scrape):
    driver.get(url)
    laptop_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"))
    )

    laptop_urls = [link.get_attribute('href') for link in laptop_links]
    print("Total laptops in page:", len(laptop_urls))

    for laptop_url in laptop_urls:
        driver.get(laptop_url)

        try:
            brand = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-size-base po-break-word"]'))).text
        except:
            brand = "Laptop nomi yo'q"
        brands.append(brand)

        try:
            model_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-size-base po-break-word"]'))).text
        except:
            model_name = "Model nomi yo'q"
        model_names.append(model_name)

        try:
            screen_size = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Centimetres")]'))).text
        except:
            screen_size = "Screen size yo'q"
        screen_sizes.append(screen_size)

        try:
            graphics_card = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Graphics")]'))).text
        except:
            graphics_card = "Grafik karta yo'q"
        graphics_cards.append(graphics_card)

        try:
            ram = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "RAM")]'))).text
        except:
            ram = "RAM yo'q"
        rams.append(ram)

        try:
            storage_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Storage")]'))).text
        except:
            storage_value = "Storage yo'q"
        storages.append(storage_value)

        try:
            cpu_model_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "CPU")]'))).text
        except:
            cpu_model_value = "CPU yo'q"
        cpu_models.append(cpu_model_value)

        try:
            operating_system_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "OS")]'))).text
        except:
            operating_system_value = "OS yo'q"
        operating_systems.append(operating_system_value)

        try:
            price_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-color-price"]'))).text
        except:
            price_value = "Narxi yo'q"
        prices.append(price_value)

        try:
            rating_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-icon-alt"]'))).text
        except:
            rating_value = "Rating yo'q"
        ratings.append(rating_value)

        try:
            review_count_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="acrCustomerReviewText"]'))).text
        except:
            review_count_value = "Sharhlar yo'q"
        review_counts.append(review_count_value)
df = pd.DataFrame({
    "brand": brands,
    "model_name": model_names,
    "screen_size": screen_sizes,
    "RAM": rams,
    "storage": storages,
    "cpu_model": cpu_models,
    "operating_system": operating_systems,
    "price": prices,
    "rating": ratings,
    "review_count": review_counts,
    "graphics_card": graphics_cards
})
df.to_csv("laptopscrapy.csv", index=False)

driver.quit()
