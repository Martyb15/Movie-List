
# read data

with open("movies.json", "r") as file:
    file_data = json.load(file)
    for i in file_data["movies"]:
      print(i)