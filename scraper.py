from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--start-maximised")
options.add_argument("--use-gl=egl")
#options.add_argument("--headless")

# instantiate driver, go to main page, instantiate next page button
with webdriver.Chrome(options=options) as driver:
    mainpage = driver.get('https://tol.allchemy.net/s7gen/')
    next_page = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/span[2]/button[2]")

    for i in range(1000):
        next_page.click()

        # instantiate chart
        for x in range(1, 13):
            xpath = '/html/body/div[1]/div/div[2]/div[2]/p/div['
            xpath += str(x)
            xpath += ']'
            find_molecules = driver.find_elements(By.XPATH, xpath)

            for individual_molecule in find_molecules:
                individual_molecule.click()
                individual_molecule_info = driver.page_source
                sleep(1)

                # instantiate paths for each molecule, record RXs
                all_paths = driver.find_elements(By.XPATH, '/html/body/div[2]/div[5]/div[1]/span/button')
                for single_path in all_paths:
                    single_path.click()
                    sleep(1)
                    scraped_pathway = driver.page_source
                    with open('output.csv', 'a+') as info_file:
                        info_file.write(scraped_pathway)
                    sleep(1)

            # instantiate close button, return to main page
            close_molecule = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/center/button')
            close_molecule.click()
            sleep(1)

print('Closing in 20 seconds.')
sleep(20)
driver.close()
