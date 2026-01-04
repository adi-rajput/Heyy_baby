import os
import random
import subprocess
from datetime import datetime, timedelta

def run(cmd, env=None):
    subprocess.run(cmd, shell=True, check=True, env=env)

TOTAL_DAYS = 220
TOTAL_COMMITS = 250
MAX_PER_DAY = 4

commit_messages = [
    "refactor logic",
    "minor fixes",
    "update utils",
    "cleanup",
    "improve structure",
    "optimize flow",
    "update docs",
    "small enhancement"
]

# -----------------------------
# Step 1: Generate distribution
# -----------------------------
days = [0] * TOTAL_DAYS
remaining = TOTAL_COMMITS

while remaining > 0:
    i = random.randint(0, TOTAL_DAYS - 1)
    if days[i] < MAX_PER_DAY:
        days[i] += 1
        remaining -= 1

random.shuffle(days)

# -----------------------------
# Step 2: Create commits
# -----------------------------
base_env = os.environ.copy()
start_date = datetime.now()

for day_index, commits_today in enumerate(days):
    if commits_today == 0:
        continue

    date = start_date - timedelta(days=day_index)

    for _ in range(commits_today):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_time = date.replace(
            hour=hour,
            minute=minute,
            second=second
        ).strftime("%Y-%m-%d %H:%M:%S")

        with open("activity.txt", "a") as f:
            f.write(f"{commit_time}\n")

        run("git add .")

        env = base_env.copy()
        env["GIT_AUTHOR_DATE"] = commit_time
        env["GIT_COMMITTER_DATE"] = commit_time

        msg = random.choice(commit_messages)
        run(f'git commit -m "{msg}"', env=env)
