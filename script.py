import json

while True:
    file = input("Please enter your JSON file path: ")

    try:
        with open(file, "r") as fr:
            # Data taken as dictionary
            data = json.load(fr)

        importantData = set()
        field = input("Choose the type of field: ")
        for entry in data['results']:
            value = entry.get(field)
            if value:
                importantData.add(value)

        print(importantData);

        repeat = input("Scan again? (Y/N) ").upper()
        if repeat == "Y":
            continue
        elif repeat == "N":
            break
    except:
        print("Error Scanning File")
        continue

