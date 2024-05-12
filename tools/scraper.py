import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scipy.interpolate import interp1d 

def scraper(chromedriver_path):
    """Get the Daily Treasury Par Yield Curve Rates from the U.S Department of The Treasury Website."""

    url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2024"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('headless')

    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)

    interest_xml = driver.find_element("xpath", '//*[@id="block-hamilton-content"]/div/div/div[3]/table')
    interest_text = interest_xml.text.split('\n')

    nrow = len(interest_text) - 1
    ncol = len(interest_text[1].split(' '))    
    col_names = [interest_text[0][i*5:(i*5+5)] for i in range(ncol)]

    interests = pd.DataFrame(np.zeros([nrow, ncol]), columns = col_names)

    for row in range(nrow):
        interests.iloc[row, :] = interest_text[row+1].split(' ')
    for i in range(1, len(interests.columns)):
        interests[interests.columns[i]] = interests[interests.columns[i]].astype(float)

    interests.to_csv('..\data\interests_data.csv', index=False)

    x_values = [1, 2, 3, 5, 7, 10, 20, 30]
    y_values = interests.iloc[-1, -8:].values

    interpolation = interp1d(x_values, y_values)
    scraper = interpolation(range(1, 31)) / 100

    last_value = interests.iloc[-1, -1] / 100
    last_values_array = np.repeat(last_value, 30)

    scraper = np.concatenate((scraper, last_values_array))

    print('Interests data successfully collected!')
    print(scraper)

    return scraper

if __name__ == '__main__':
    chromedriver_path = 'D:\\chromedriver.exe'
    interests = scraper(chromedriver_path)