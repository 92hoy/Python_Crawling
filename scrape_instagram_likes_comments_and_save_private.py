from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_instagram_likes_comments_and_save_private(profile_url, username, password):
    # Extract the account name from the profile URL
    account_name = profile_url.split('/')[-2]

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    # Find the username and password fields, and fill them in
    username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_field.send_keys(username)
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

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
    with open('insta_{}_favorite.txt'.format(account_name), 'w') as f:
        for result in results:
            f.write('Likes: {}\nComments: {}\n\n'.format(result['likes'], result['comments']))

    # Return the results
    return results

results = scrape_instagram_likes_comments_and_save_private('https://www.instagram.com/climb__jh/', 'my_username', 'my_password')
print(results)

# 이 함수는 인스타그램 프로필 URL뿐만 아니라 로그인에 필요한 계정 아이디와 비밀번호도 매개변수로 받습니다. 
# 먼저 크롬 웹드라이버를 열고, 인스타그램 로그인 페이지로 이동합니다. 
# 그리고 username_field와 password_field를 찾아 입력한 후, 로그인 버튼을 누릅니다. 
# 이후 인스타그램 프로필 페이지로 이동하고, 게시물의 좋아요 수와 댓글 수를 파일로 저장합니다.