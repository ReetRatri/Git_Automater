import subprocess
from datetime import datetime

# file update (so git detects change)
with open("github-activity-generator/activity.txt", "a") as f:
    f.write(f"Update: {datetime.now()}\n")

commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", f"auto update {datetime.now()}"],
    ["git", "push"]
]

for cmd in commands:
    subprocess.run(cmd)

print("Done")