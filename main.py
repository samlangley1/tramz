import os, random, shutil, string
from pathlib import Path
from instabot import Bot
from config import username, password, post_caption

if __name__ == "__main__":
    try:
        shutil.rmtree("./config")
    except FileNotFoundError:
        pass

    images = [x.name for x in Path("./images/").iterdir() if x.is_file()]

    image_to_upload = random.choice(images)

    if len(images) == 0:
        raise Exception("Please make sure your images directory contains image files")


    bot = Bot()

    bot.login(username = username,
            password = password)


    bot.upload_photo(f"./images/{image_to_upload}", caption=post_caption)

    os.rename(f"./images/{image_to_upload}" + ".REMOVE_ME", f"./images/{image_to_upload}")

    generated_sku = ''.join(random.choice(string.ascii_letters) for i in range(10))

    file_extension = os.path.splitext(f"./images/{image_to_upload}")

    used_images_directory = "./images/used/"

    if not os.path.exists(used_images_directory):
        os.makedirs(used_images_directory)

    shutil.move(f"./images/{image_to_upload}", f"{used_images_directory}{generated_sku}{file_extension[1]}")

