import json
import os
import sys
import datetime

output_file = open('commit_arts.txt',"a")

f = open('pattern/octocat.json')

data = json.load(f)
# make sure the start date is correct

output_dates = []

# this is the width
# print(len(data))
# this is the week always 7
# print(len(data[0]))

# def display_the_output():

# iterate through each day until width
for week in range(0,len(data[0])):
    for day in range(0,7):
        times = data[day][week]
        if times == " ":
            continue
        times = int(times)
        for temp in range(times):
            output_dates.append(datetime.timedelta(weeks=week, days=day, hours=6,minutes=temp+1))



# sys.exit()
os.system("git status")
print("total commits " + str(len(output_dates)))
commit_time = []

# not make it in correct time format
start_date = datetime.datetime(year=2022, month=8, day=21)
for time in output_dates:
    temp = start_date + time
    temp = temp.strftime("%a %b %d %H:%M:%S %Y %z" +"+0545")
    print(temp)
    commit_time.append(temp)
# here we go
for indx,time in enumerate(commit_time):
    with open("commit_arts.txt","a") as f:
        f.write(f"{output_dates[indx]}\n")
    os.system(f"git add -A")
    os.system(f"git commit -m \"{indx}\" --date=\"{time}\"")

# +"%a %b %d %H:%M:%S %Y %z" acutally used format
#print(start_date.strftime("%a %b %d %H:%M:%S %Y %z" +"+0545"))
# print(output_dates)
f.close()