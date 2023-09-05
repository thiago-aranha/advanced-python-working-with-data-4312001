# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?
totalQuakes = sum(quake["properties"]["time"] is not None
          for quake in data["features"])
print(f"Total quakes: {totalQuakes}")

# 2: How many quakes were felt by at least 100 people?
totalQuakesFelt100People = sum(quake["properties"]["felt"] is not None and
                               quake["properties"]["felt"] >= 100
                               for quake in data["features"])
print(f"Total quakes felt by at least 100 people: {totalQuakesFelt100People}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getFelt(f):
    felt = f["properties"]["felt"]
    if (felt is None):
        return 0
    return felt


feltMostPeople = max(data["features"], key=getFelt)
print("Most felt report: M" +
      str(feltMostPeople["properties"]["mag"]) + " - " + feltMostPeople["properties"]["place"] + ", reports: " + str(feltMostPeople["properties"]["felt"]))

# 4: Print the top 10 most significant events, with the significance value of each
def getSig(s):
    sig = s["properties"]["sig"]
    if (sig is None):
        return 0
    return sig

print("The 10 most significant events were:")
mostSignificant = sorted(data["features"], key=getSig, reverse=True)
for i in range(0,10):
    print(
        f"Event: {mostSignificant[i]['properties']['title']}, Significance: {mostSignificant[i]['properties']['sig']}")