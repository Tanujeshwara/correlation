import csv
import plotly.express as px
import numpy as np

def plotfig(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(data_path):
    marks_percentage=[]
    days_present=[]
    with open(data_path) as f :
        reader=csv.DictReader(f)
        for row in reader:
            marks_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x":marks_percentage,"y":days_present}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Marks and Days Present :",correlation[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotfig(data_path)

setup()



