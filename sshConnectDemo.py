import paramiko as paramiko
import csv
from utilities.configurations import *
# Start Connection
username = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['Server']['port']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

# Run commands -command
#stdin,stdout,stderr = ssh.exec_command("ls -a")
stdin,stdout,stderr = ssh.exec_command("cat demofile")
#print(stdout.readlines())
lines = stdout.readlines()
print(lines[1])

#Upload files
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchFiles/script.py"
sftp.put(localPath,destinationPath)

destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath,destinationPath)

#Trigger the Batch commands
stdin,stdout,stderr = ssh.exec_command("python script.py")

#Download the file to local system,
sftp.get("loanasa.csv","outputFiles/loanasa.csv")

#Parse Output file CSV
with open("outputFiles/loanasa.csv") as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    for row in csvReader:
        if row[0] == "32321":
           assert row[1] == "approved"



ssh.close()




