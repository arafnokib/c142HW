import csv
all_articles = []

with open("csvs/final.csv", encoding="UTF-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
    
liked_articles = []
disliked_articles = []
