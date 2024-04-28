# API-s-automation
To check the grasp on calling API’s, automation of the browser, basic problem solving

# LinkedIn Data Scraper

This repository contains scripts to scrape user data from LinkedIn using two different methods: LinkedIn API and browser automation.

## Scripts

### LinkedIn API Script
- `linkedin_api_script.py`: This script uses LinkedIn's API to retrieve user data based on first and last names provided by the user. The data of the first 5 relevant search results is saved in a CSV file.

### Browser Automation Script
- `browser_automation_script.py`: This script automates browser interaction using Selenium to scrape user data from LinkedIn search results. Again, the data of the first 5 relevant search results is saved in a CSV file.

## Usage
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the desired script (`linkedin_api_script.py` or `browser_automation_script.py`) and follow the prompts to input first and last names.

## Dependencies
- `requests`: For making HTTP requests in the LinkedIn API script.
- `selenium`: For browser automation in the browser automation script.
- `chromedriver`: Chrome WebDriver for Selenium (download and specify the path in the script if necessary).

## Note
Remember to replace 'YOUR_ACCESS_TOKEN' in `linkedin_api_script.py` with your actual LinkedIn access token.
