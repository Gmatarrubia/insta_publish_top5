from instabot import Bot
import requests
import argparse

# Import your custom credentials
# Modify the class Credentials with your values
from credentials import Credentials

image_path = 'image.jpg'

def get_the_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {url} as {image_path}.')
    else:
        print(f'Failed to download {url}. Status code: {response.status_code}.')
        exit(1)


def publish_the_image(prompt, hastags):
    credential = Credentials()
    image_path = 'image.jpg'

    caption = 'Rate this picture from 0 to 5 ✍️....👇🏼👀. \
                Prompt: ' + prompt + ' #top5 #DallE #IA #daily'
    for hastag in hastags:
        caption.append(' #' + hastag)

    bot = Bot()
    bot.login(username=credential.username,
            password=credential.password)

    # Publish the photo with caption
    print("Uploading the picture...")
    bot.upload_photo(image_path, caption=prompt)

    # Logout from your account
    print("Picture uploaded successfully.")
    bot.logout()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', action='store', type=str, requried=True,
                        help='url from the bing image creator')
    parser.add_argument('prompt', action='store', type=str, required= True,
                        help='continue to the next target on error')

    args = parser.parse_args()

    get_the_image(str(args.url))
    publish_the_image(str(args.prompt))
    print("Action complete.")

if __name__ == main:
    main()
