import tbapy
import gviz_api


def setapikey():
    global apikey
    apikey = 'fWFSAeNa3VxZUdVJhaXgAXjnM9mfLBmbw1bbOrviglJBtJxmcUTANIMpECdWSSwU'
    return apikey


def frc(points, matchcount):
    output = round(points / matchcount, 2)
    return output


def createlink(matchkeystring, linktext):
    link = "<a href=https://www.thebluealliance.com/match/" + matchkeystring + " target='_blank'>" + linktext +\
           "</a>"
    return link


def predicttable(desc, dictionary):
    data_table_predict = gviz_api.DataTable(desc)
    data_table_predict.LoadData(dictionary)

    # Data set for predictions
    jspredict = data_table_predict.ToJSCode("jspredict_data",
                                            columns_order=("Match Key", "Winner", "Blue 1", "Blue 2", "Blue 3",
                                                           "Blue Score", "Red Score", "Red 1", "Red 2", "Red 3"))
    return jspredict


tba = tbapy.TBA(setapikey())
year = "2018"
red = "red"
blue = "blue"
teamKeys = "team_keys"
event = input("Enter an event ID: ")  # 2018week0, 2018mokc2, 2018iacf
lev = "Levitate"
NA = "NA"
csvFile = ("TBA_Match_Data_%s.csv" % event)
csvFilePath = (event + "\\" + csvFile)
htmlFile = ("TBACharts_%s.html" % event)
htmlFilePath = (event + "\\" + htmlFile)
teamObjects = tba.event_teams(event, simple="true")
dictList = {}
dictChart = {}
dictPredictEmpty = {"No Match to Predict": ["None", "tie", 0, 0, 0, 0, 0, 0, 0, 0]}
