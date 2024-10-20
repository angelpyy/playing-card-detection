import requests
import os
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

def download_main_image(url, save_dir=None):
    web_domain = os.getenv('WEB_DOMAIN')
    
    # GET request to the URL L those guys fr
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    
    # Image main source
    img = soup.find('img', id='theMainImage')
    
    # snatch that boy
    if img:
        # Get the image source
        img = img['src']
    
    # Complete image source; replace the initial dot with web domain
    # DO NOT USE REPLACE FUNCTION DEAR GOD
    img = web_domain + img[1:]
    
    # attempt to request image and download
    img_response = requests.get(img)
    
    # check request; make sure ok
    if img_response.status_code != requests.codes.ok:
        print(f'Failed to download image. Status code: {img_response.status_code}')
        return

    # dumbass bozo
    if not save_dir:
        print('No save dir provided')
        return

    # check for dir, if not create it and get img name
    os.makedirs(save_dir, exist_ok=True)
    img_name = os.path.join(save_dir, img[img.rfind('/')+1:])

    # magic?
    try:
        with open(img_name, 'wb') as file:
            file.write(img_response.content)
        print(f'Image downloaded: {img_name}')
    except IOError as e:
        print(f'Error saving image: {e}')

    # Add a small delay to be polite to the server
    time.sleep(1)
    
def main():
    url = os.getenv('URL')
    # final image = 118568
    
    # starting image
    img_num = 118517
    
    while img_num < 118569:
        # save image
        download_main_image(url, '../card_images/set')
        
        # count up to next card
        # this would be easier to do by hand cause i can change the names of the card files...
        img_num += 1
        url = url.replace(str(img_num-1), str(img_num))
    
if __name__ == '__main__':
    main()
    