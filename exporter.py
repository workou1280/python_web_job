import csv

def save_to_file(jobs):
    file=open('jobs.csv','w',encoding='UTF-8',newline="")
    writer = csv.writer(file)
    writer.writerow(["tilte", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return