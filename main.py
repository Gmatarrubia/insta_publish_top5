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
work_folder = 'pics'
num_of_pics = 1

def get_the_images(urls):
    os.mkdir(work_folder)
    pic_num = 0
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(work_folder, str(pic_num) + '_' + image_path), 'wb') as f:
                f.write(response.content)
            pic_num += 1
            print(f'Successfully downloaded.')
        else:
            print(f'Failed to download {url}. Status code: {response.status_code}.')
            exit(1)


def publish_the_images(prompt, hastags):
    credential = Credentials()
    images = sorted(os.listdir(work_folder))
    # Prepend folder to all the files
    aux_images = [os.path.join(work_folder,s) for s in images]
    images = aux_images

    caption = 'Crafted by Dall-E. 🤖 \n\r' \
                + 'Prompt: ' + prompt + "\n\r\n\r" \
                + 'Follow me for inspiration and push your imagination. ' \
                + 'Learn more about prompts and styles. \n\r\n\r' \
                + 'More content in my profile, check it out!.' \
                + 'I read your comments. What do you like the most? ✍ 👀 \n\r\n\r' \
                + '#top5 #DallE #IA #daily #prompt #art #design #midjourney #stabledifussion' \
                + ' #generativedesign #generativeartist '

    for hastag in hastags:
        caption += (' #' + str(hastag))

    bot = Bot()
    bot.login(username=credential.username,
            password=credential.password)

    if len(images) == 1:
        # Publish the photo with caption
        print("Uploading the picture...")
        bot.upload_photo(images[0], caption=caption)
    elif len(images) > 1:
        # Publish the carrousel of photos with caption
        print("Uploading " + str(len(images)) + " pictures...")
        bot.upload_album(images, caption=caption)
    else:
        print("Error in the number of pics.")
        exit(1)

    # Logout from your account
    print("Picture uploaded successfully.")
    bot.logout()

def askHastags ():
    hastags = []
    while True:
        hastag = input('Enter a hastag (or press Enter to finish): ')
        if hastag:
            hastags.append(hastag)
        else:
            break
    return hastags

def clean_env():
    folders = ['config', work_folder]
    for f in folders:
        try:
            rmtree(f)
        except:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls', nargs='+',
                        help='url from the bing image creator')
    parser.add_argument('--prompt', action='store', type=str,
                        help='continue to the next target on error')

    args = parser.parse_args()

    clean_env()
    hastags = askHastags()
    get_the_images(args.urls)
    publish_the_images(str(args.prompt), hastags)
    print("Action complete.")

if __name__ == "__main__":
    main()
    exit(0)
