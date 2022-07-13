from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()
    page.goto("https://")
    page.locator('xpath=//*[@id="navbar"]/ul/li[3]/a').click()
    page.locator('xpath=/html/body/nav/div/div[2]/ul/li[3]/ul/li/a').click()
    page.locator('xpath=/html/body/nav/div/div[2]/ul/li[3]/ul/li/ul/li[3]/a').click()
    page.locator('xpath=//*[@id="btnAtualizar"]').click()
    time.sleep(5)
    page.locator('xpath=/html/body/div[1]/form/div[2]/button[4]').click()
    time.sleep(3)
    page.locator('xpath=/html/body/div[1]/div[4]/div/div/div[2]/form/p[1]/button/i').click()
    time.sleep(3)
    page.locator('xpath=/html/body/div[1]/div[4]/div/div/div[2]/form/p[2]/button/i').click()
    time.sleep(3)
    page.locator('xpath=/html/body/div[1]/div[4]/div/div/div[3]/button').click()
    time.sleep(10)    
    print(page.title())
    navegador.close()
