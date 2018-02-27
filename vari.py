import tbapy


def setapikey():
    global apikey
    apikey = 'fWFSAeNa3VxZUdVJhaXgAXjnM9mfLBmbw1bbOrviglJBtJxmcUTANIMpECdWSSwU'
    return apikey


def frc(points, matchCount):
    output = round(points / matchCount, 2)
    return output


def createlink(matchkeystring, linktext):
    link = "<a href=https://www.thebluealliance.com/match/" + matchkeystring + " target='_blank'>" + linktext +\
           "</a>"
    return link


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
