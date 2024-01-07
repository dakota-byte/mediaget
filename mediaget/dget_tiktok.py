# usage:
# python tiktok.py $URL

# Imports
import requests, os, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from moviepy.editor import VideoFileClip

# Helpers
    
def find_mp4_file():
    # current_directory = os.path.join(os.getcwd(), "tiktoks")
    for file_name in os.listdir("/tmp/"):
        if file_name.endswith("tiktok.mp4"):
            return os.path.join("/tmp/", file_name)
    return None 

def convert_mp4_to_mov(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', preset='ultrafast', threads=4, fps=video_clip.fps)
    video_clip.close()

def download_mp4_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def selenium_get_mov(url):
    driver = webdriver.Chrome()
    

    driver.get("https://ssstik.io/en")

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.ID, value="main_page_text")
    submit_button = driver.find_element(by=By.CLASS_NAME, value="pure-button-primary")

    text_box.send_keys(url)
    submit_button.click()

    get_button = driver.find_element(by=By.LINK_TEXT, value="Without watermark")

    download_link = get_button.get_attribute("href")

    download_mp4_file(download_link, "/tmp/output_tiktok.mp4")
    mp4_file = find_mp4_file()
    convert_mp4_to_mov(mp4_file, "/home/kali/Desktop/tiktok.mov")
    os.remove(mp4_file)

    driver.quit()

selenium_get_mov(sys.argv[1])
