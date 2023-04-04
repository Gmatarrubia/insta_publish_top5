#!/usr/bin/python3
from instabot import Bot
import requests
import argparse
import os
from bs4 import BeautifulSoup
from shutil import rmtree

# Import your custom credentials
# Modify the class Credentials with your values
from credentials import Credentials

image_path = 'image.jpg'

def get_the_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded.')
    else:
        print(f'Failed to download {url}. Status code: {response.status_code}.')
        exit(1)


def publish_the_image(prompt, hastags):
    credential = Credentials()
    image_path = 'image.jpg'

    caption = 'Crafted by Dall-E generative IA art. 🤖 \n' \
                + 'Prompt: ' + prompt + "\n" \
                + 'Follow me for inspiration. Push your imagination.' \
                + 'Learn more about prompts and styles.' \
                + 'More content in my profile, check it out!.' \
                + 'I read your comments. What do you like the most? ✍ 👀 \n' \
                + '#top5 #DallE #IA #daily #prompt #art #design'

    for hastag in hastags:
        caption += (' #' + str(hastag))

    bot = Bot()
    bot.login(username=credential.username,
            password=credential.password)

    # Publish the photo with caption
    print("Uploading the picture...")
    bot.upload_photo(image_path, caption=caption)

    # Logout from your account
    print("Picture uploaded successfully.")
    bot.logout()

def clean_env():
    try:
        rmtree('config')
    except:
        pass
    try:
        rmtree('image.jpg.REMOVE_ME')
    except:
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', action='store', type=str,
                        help='url from the bing image creator')
    parser.add_argument('--prompt', action='store', type=str,
                        help='continue to the next target on error')

    args = parser.parse_args()

    hastags = []
    while True:
        hastag = input('Enter a hastag (or press Enter to finish): ')
        if hastag:
            hastags.append(hastag)
        else:
            break

    clean_env()
    get_the_image(str(args.url))
    publish_the_image(str(args.prompt), hastags)
    print("Action complete.")

if __name__ == "__main__":
    main()
