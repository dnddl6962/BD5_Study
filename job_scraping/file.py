def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", "w")
  file.write("Position, Company, Location, URL\n")
  for job in jobs:
    if job['location'] != None:
      job['location'] = job['location'].replace(',', ' ')
      file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")
    else : 
      file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")
    
  
  file.close()
