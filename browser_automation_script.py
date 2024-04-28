from selenium import webdriver
import time
import csv

def get_user_data_from_linkedin(first_name, last_name):
    # Use Selenium to automate browser interaction
    driver = webdriver.Chrome()  # You may need to adjust this path to your Chrome driver executable
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords={first_name}%20{last_name}')
    
    # Wait for page to load
    time.sleep(5)

    # Extract data
    users = driver.find_elements_by_class_name('search-result__wrapper')

    data = []
    for user in users[:5]:
        name = user.find_element_by_class_name('actor-name').text
        title = user.find_element_by_class_name('subline-level-1').text
        location = user.find_element_by_class_name('subline-level-2').text
        profile_url = user.find_element_by_tag_name('a').get_attribute('href')
        data.append({'Name': name, 'Title': title, 'Location': location, 'Profile URL': profile_url})
    
    driver.quit()
    return data

def save_to_csv(data):
    with open('linkedin_data_automation.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Title', 'Location', 'Profile URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in data:
            writer.writerow(user)

def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    data = get_user_data_from_linkedin(first_name, last_name)
    save_to_csv(data)

if __name__ == "__main__":
    main()
