import pandas as pd

googleCsv = pd.read_csv('./google_list.csv')
nateCsv = pd.read_csv('./nate_list.csv')
zumCsv = pd.read_csv('./zum_list.csv')

queryList = ""

for item in googleCsv.iloc[:].values:
    time = item[2].replace("+09:00", "")
    query = "INSERT INTO google (rank, keyword, time) VALUES (%d, '%s', '%s')\n" % (item[0], item[1], time)
    queryList += query

queryList += "\n"

for item in nateCsv.iloc[:].values:
    time = item[2][:-7]
    query = "INSERT INTO nate (rank, keyword, time) VALUES (%d, '%s', '%s')\n" % (item[0], item[1], time)
    queryList += query

queryList += "\n"

for item in zumCsv.iloc[:].values:
    time = item[2][:-7]
    query = "INSERT INTO zum (rank, keyword, time) VALUES (%d, '%s', '%s')\n" % (item[0], item[1], time)
    queryList += query

queryList += "\n"

f = open("../2020_1_Python_Noreunja_Spring/src/main/resources/data.sql", "a", encoding="utf-8")
# f = open("data.sql", "a", encoding="utf-8")
f.write(queryList)
f.close()
