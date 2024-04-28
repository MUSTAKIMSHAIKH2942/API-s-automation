import requests
import csv
from Enviroment import *

def get_user_data_from_linkedin(first_name, last_name):
    access_token = access_token_var
    url = f'https://api.linkedin.com/v2/people/?q=firstName:{first_name},lastName:{last_name}'
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def save_to_csv(data):
    if data:
        with open('linkedin_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Title', 'Location', 'Profile URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in data.get('elements', [])[:5]:
                writer.writerow({
                    'Name': user.get('firstName') + ' ' + user.get('lastName'),
                    'Title': user.get('headline', ''),
                    'Location': user.get('location', {}).get('name', ''),
                    'Profile URL': user.get('publicProfileUrl', '')
                })

def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    data = get_user_data_from_linkedin(first_name, last_name)
    save_to_csv(data)

if __name__ == "__main__":
    main()
