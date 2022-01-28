#Lab08 - Romulo Partoriza - 100753119
'''
PART 1
DEMOGRAPHICS
1. Females, age 18+
2. Males, age 18+
3. Females, age 12-17
4. Males, age 12-17
PART 2 
 Ontario
 Females
 "Self-reported physical activity, 150 minutes per week, adult (18 years and over)" 
'''
import json

# Part 1
#function loadData loads in arguments
def loadData(sex, area, indicators):
    #Dictionary is created
    dic_CharVal = {}
    with open('health_data.tsv', 'r') as file:
        for line in file:
            #For every line, each column is sperated to locate each header (age,area)
            headers = line.split('\t')
            #Finds key and values for first demographic
            if  headers[4] == sex and headers[1] == area and headers[5] == indicators:
                dic_CharVal[headers[6]] = headers[13]
        return dic_CharVal

sex = 'Females'
area = 'Ontario'
indicators = '"Self-reported physical activity, 150 minutes per week, adult (18 years and over)"'
print(loadData(sex, area, indicators))

#Part 2 - Calls loadData and outputs the data to a JSON file
with open('Demographic1.json', 'w') as file:
    json.dump(loadData(sex, area, indicators), file)