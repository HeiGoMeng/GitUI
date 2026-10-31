NameToCmd = {
    'Add': "add",
    "Pull": "pull",
    "Push": "push",
    "Commit": "commit",
    "Branch functions (inc. rebase)": "branch",
    "Merge": 'merge'
            }

windows={}

for i in NameToCmd:
    print(i[-1])

for i in range(len(NameToCmd)):
    windows[list(NameToCmd.keys())[i]] = f"{list(NameToCmd.values())[i][0].upper()}{list(NameToCmd.values())[i][1:]}Win"

print(windows)