import os, random, shutil, string, logging
from pathlib import Path
from instabot import Bot
from config import username, password, post_caption


def reset_config():
    try:
        shutil.rmtree("./config")
    except FileNotFoundError:
        pass



def get_image():
    global image_to_upload
    images = [x.name for x in Path("./images/").iterdir() if x.is_file()]

    image_to_upload = random.choice(images)

    if len(images) == 0:
        raise Exception("Please make sure your images directory contains image files")

    return image_to_upload


def move_image_to_used():
    os.rename(f"./images/{image_to_upload}" + ".REMOVE_ME", f"./images/{image_to_upload}")

    generated_sku = ''.join(random.choice(string.ascii_letters) for i in range(10))

    file_extension = os.path.splitext(f"./images/{image_to_upload}")

    used_images_directory = "./images/used/"

    if not os.path.exists(used_images_directory):
        os.makedirs(used_images_directory)

    shutil.move(f"./images/{image_to_upload}", f"{used_images_directory}{generated_sku}{file_extension[1]}")

if __name__ == "__main__":
    reset_config()

    get_image()

    bot = Bot()

    bot.login(username = username,
            password = password)


    bot.upload_photo(f"./images/{image_to_upload}", caption=random.choice(post_caption))

    move_image_to_used()

