# -*- coding: utf-8 -*-

#import library
import pandas as pd

#read csv file
df = pd.read_csv('cities.csv')
df.head()

#convert to htm;
html = df.to_html()

# write html to file 
text_file = open("data.html", "w") 
text_file.write(html) 
text_file.close() 
