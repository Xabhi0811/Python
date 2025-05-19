import os
import datetime
import random
script_filename = __file__

comment = f"# Auto-generated comment at {datetime.datetime.now()} - {random.randint(1000, 9999)}\n"


with open(script_filename, "r") as file:
    lines = file.readlines()

lines.insert(1, comment)

with open(script_filename, "w") as file:
    file.writelines(lines)

commit_message = f"Auto-updated script at {datetime.datetime.now()}"
os.system("git add auto_commit.py")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")  
print("Script updated and pushed to GitHub!") 
