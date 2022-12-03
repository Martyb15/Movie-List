import os, time, sys
import json
# import random
# from getkey import getkey, keys
# import cursor

sp = 0.08


def scroll(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(sp)
  print()


line = scroll(
  "Hello and welcome to the movie selector / movie rating application")


def selection():
  print("1. List All Movies")  # [DONE]
  print("2. Add a Movie")  # [DONE]
  print("3. Select a movie")
  temp = input(":")
  return temp


#ADD Function
def write_json(new_data, filename="movies.json"):
  with open(filename, "r+") as file:
    file_data = json.load(file)
    file_data["movies"].append(new_data)
    file.seek(0)
    json.dump(file_data, file, indent=4)


# Getting/ creating json data
def get_json():
  title = input("Enter the title :")
  rating = input("Enter the rating :")
  return {"title": title, "rating": rating}


def list_movies():
  with open("movies.json", "r") as file:
    file_data = json.load(file)
    print("======= Movies =======")

    for i in file_data["movies"]:
      print()
      print(i)
      # print (i['title'])
      # print(i['rating'])
      print()
    input()


# movie = {
#   "title":"avatar",
#   "rating":"8/10"
# }

# write_json(movie)

while True:
  sel = selection()
  if sel == "1":
    list_movies()
  elif sel == "2":
    write_json(get_json())

# Add  a movie to the list (database)
# List all movies in database
# Select a movie
# Change movie data (update)
# Add some ASCII art

# clear console
