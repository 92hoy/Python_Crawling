from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_instagram_likes_comments_public(profile_url):
    # Extract the account name from the profile URL
    account_name = profile_url.split('/')[-2]

    # Initialize the Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the Instagram profile page
    driver.get(profile_url)

    # Wait for the page to load
    time.sleep(2)

    # Find all the post links on the page
    post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')

    # Loop through each post link and scrape the number of likes and comments
    results = []
    for post_link in post_links:
        # Click on the post link
        post_link.click()

        # Wait for the post page to load
        time.sleep(2)

        # Find the number of likes and comments
        likes = driver.find_element(By.XPATH, '//span[@class="sqdOP yWX7d     _8A5w5   "]')
        comments = driver.find_element(By.XPATH, '//span[@class="sqdOP yWX7d     _8A5w5   "][2]')

        # Append the number of likes and comments to the results list
        results.append({'likes': likes.text, 'comments': comments.text})

        # Close the post page
        close_button = driver.find_element(By.XPATH, '//div[@class="                   Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              "]')
        close_button.click()

        # Wait for the post page to close
        time.sleep(1)

    # Close the Chrome WebDriver
    driver.quit()

    # Write the results to a file
    with open('insta_{}_favorite_public.txt'.format(account_name), 'w') as f:
        for result in results:
            f.write('Likes: {}\nComments: {}\n\n'.format(result['likes'], result['comments']))

    # Return the results
    return results



scrape_instagram_likes_comments_public('https://www.instagram.com/climb__jh/')
