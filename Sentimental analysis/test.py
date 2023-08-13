import pandas as pd
from textblob import TextBlob
import csv
from csv import writer

let = []


df = pd.read_csv("C:/Users/Tarun Samala/Documents/Tarun/VIT/SEM 3/AI/PROJECT/Sentimental analysis/testy.csv",usecols=["Write your opinion about the faculty."])




with open("C:/Users/Tarun Samala/Documents/Tarun/VIT/SEM 3/AI/PROJECT/Sentimental analysis/testy.csv") as re:

    reade = csv.reader(re)
    
    for i in reade:
        let = i[2]
    
    blob = TextBlob(let)

    sent = blob.sentiment.polarity
    
    if sent > 0:
        csv.writer(["","","","happy"])
            
    else:
        csv.writer(["","","","unhappy"])
       






