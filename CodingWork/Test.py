from enum import Enum

class GitOps(Enum):
    ADD = "add"
    PULL = 'pull'
    PUSH = 'push'
    COMMIT = 'commit'
    BRANCH_FUNCTION_INC_REBASE = 'rebase'
    MERGE = 'merge'

print(GitOps[list(GitOps.__members__.keys())[1]].value)
print(GitOps['ADD'])
#windows[[x.value for x in GitOps.__members__][i]] = globals()[f"{[GitOps.__members__][i][0].upper()}{[x.value for x in GitOps.__members__][i][1:]}Win"]