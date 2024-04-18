# Lists
top = ["socks", "underwear", "handkerchief"]
middle = ["T-shirts", "Pajamas", "Trousers", "Shorts"]
bottom = [30, 73, 100, 62]

print(top[0])
print(min(bottom))


import statistics as stats
print(stats.mean(bottom))


station_names = [
    "Britomart",
    "Ōrākei",
    "Meadowbank",
    "Purewa",
    "Glen Innes",
    "Tamaki",
    "Panmure",
    "Sylvia Park"
]

print(station_names)

station_names.append("new station")
print(station_names)

# Practical
station_names = [
    "Britomart",
    "Ōrākei",
    "Meadowbank",
    "Purewa",
    "Glen Innes",
    "Tamaki",
    "Panmure",
    "Sylvia Park"
]

more_eastern = ["Otahuhu", "Middlemore", "Papatoetoe", "Puhinui", "Manukau"]

station_names.extend(more_eastern)
print(station_names)