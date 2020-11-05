from selenium import webdriver
import pandas as pd

#using selenium and chromedriver
chrome_path = r"C:\Users\alexo\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.billboard.com/charts/hot-100")

#scrape the data
songs_ex = driver.find_elements_by_class_name("chart-element__information__song")
artists_ex = driver.find_elements_by_class_name("chart-element__information__artist")
ranks_ex = driver.find_elements_by_class_name("chart-element__rank__number")

#turn data into lists of strings
songs= []
artists = []
ranks = []

for item in songs_ex:
	songs.append(item.text)
for item in artists_ex:
	artists.append(item.text)
for item in ranks_ex:
	ranks.append(item.text)

#write to excel
df = pd.DataFrame.from_dict({'ranks':ranks,'songs':songs,'artists':artists})
df.to_excel('billboard.xlsx',header = True, index = False)