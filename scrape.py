import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome browser")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded")
        html = driver.page_source

        return html
    finally:
        driver.quit()

def extract_body(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleanned_content = soup.get_text(separator="\n")
    cleanned_content = "\n".join(line.strip() for line in cleanned_content.splitlines() if line.strip())
    return cleanned_content

def split_dom(dom_content, max_len = 6000):
    return[
        dom_content[i:i +max_len] for i in range(0, len(dom_content), max_len)
    ]




