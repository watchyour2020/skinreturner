from MojangAPI import Client
from mojang import MojangAPI
import urllib.request
import asyncio
import sys
import os.path
import os
import time
import glob
import re

is_folder = False #Change this to True if you want to save this in a folder.
folder_reset = False #This will reset the specified folder every time this script ran. Note: Wont work without is_folder on.
render_mc = True #It renders the skin you asked for and saves it in the specified folder or the directory of the python file.
if is_folder == True:
  folder = 'Users' #Folder you want yo save the file. If is_folder is False, do not change this.
else:
  folder = '' #Dont change this pls

async def main():
  if is_folder == True:
   if folder_reset == True:
    if os.path.isdir(folder):
     if not os.listdir(folder) == []:
      for root, dirs, files in os.walk(folder):
       for file in files:
        os.remove(os.path.join(root, file))

  username = 'Minecraft' #The Username of The Minecraft User
  user = await Client.User.createUser(username)
  uuid = MojangAPI.get_uuid(username)
  profile = await user.getProfile()
  if os.path.isfile(f"{username}.png"):
   print(f"Profile {username} already exists.")
   print("Overwrite?")
   overwrite = input("Y or N?:")
   if overwrite == "Y":
    os.remove(f"{username}.png")   
    if is_folder == True:
     urllib.request.urlretrieve(profile.skin, f"{folder}\\{username}.png"),
    else:
     urllib.request.urlretrieve(profile.skin, f"{username}.png")
   elif overwrite == "N":
    time.sleep(2)
    exit()
  else:
   if is_folder == True:
    urllib.request.urlretrieve(profile.skin, f"{folder}\\{username}.png"),
   else:
    urllib.request.urlretrieve(profile.skin, f"{username}.png")
   if render_mc == True:
     if is_folder == True:
      urllib.request.urlretrieve(f"https://crafatar.com/renders/body/{uuid}", f"{folder}\\{username}_render.png")
     else:
      urllib.request.urlretrieve(f"https://crafatar.com/renders/body/{uuid}", f"{username}_render.png")
   else:
     if is_folder == True:
      urllib.request.urlretrieve(profile.skin, f"{folder}\\{username}.png")
     else:
      urllib.request.urlretrieve(profile.skin, f"{username}.png")
  print(f"Profile {username}, is succesfully saved.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())