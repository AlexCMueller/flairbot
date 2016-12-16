roleListFile = open("roleList.txt", 'r') # Open role list file
roleList = roleListFile.read().splitlines() # Get role list from file

token = "REDACTED" # bot token
serverid = "249837317362155520" # server bot is to operate in
operatorRole = "Bot Commander" # role name for operator
