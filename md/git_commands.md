# Git Commands Cheat

| Git Command                           | Description                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------------------------|
| `git checkout <branch_name>`          | Switch to the `<branch_name>` branch.                                                       |
| `git branch <branch_name>_copy`       | Create a new branch named `<branch_name>_copy` as a copy of the current branch.             |
| `git checkout main`                   | Switch to the `main` branch.                                                                |
| `git branch -D <branch_name>`         | Force delete the local branch `<branch_name>`.                                              |
| `git fetch origin <branch_name>`      | Fetch updates for the remote branch `<branch_name>` without merging them into any local branch. |
| `git checkout -b <branch_name> origin/<branch_name>` | Create a new local branch `<branch_name>` based on the remote branch `origin/<branch_name>` and switch to it. |


# Git Commands Cheat

| Git Command                                  | Description                                                                                          |
|----------------------------------------------|------------------------------------------------------------------------------------------------------|
| `git init`                                   | Initialize a new Git repository in the current directory.                                            |
| `git clone <repository_url>`                 | Clone a remote repository to your local machine.                                                    |
| `git add <file>`                             | Stage changes of a specific file for the next commit.                                                |
| `git add .`                                  | Stage all changes in the current directory for the next commit.                                      |
| `git commit -m "<message>"`                  | Commit staged changes with a descriptive message.                                                    |
| `git status`                                 | Show the status of the working directory and staging area.                                           |
| `git log`                                    | Show the commit history of the current branch.                                                       |
| `git log --oneline`                          | Display a condensed commit history with one commit per line.                                         |
| `git branch`                                 | List all local branches.                                                                             |
| `git branch <new_branch>`                    | Create a new branch named `<new_branch>`.                                                           |
| `git checkout <branch_name>`                 | Switch to the `<branch_name>` branch.                                                               |
| `git checkout -b <new_branch>`               | Create a new branch `<new_branch>` and switch to it.                                                 |
| `git merge <branch_name>`                    | Merge `<branch_name>` into the current branch.                                                      |
| `git fetch`                                  | Fetch changes from the remote repository without merging them into the current branch.              |
| `git pull`                                   | Fetch and merge changes from the remote repository into the current branch.                         |
| `git push`                                   | Push committed changes to the remote repository.                                                    |
| `git push -u origin <branch_name>`           | Push a new branch `<branch_name>` to the remote repository and set it as the upstream branch.        |
| `git stash`                                  | Temporarily save uncommitted changes for later use.                                                 |
| `git stash pop`                              | Apply the most recent stashed changes and remove them from the stash.                               |
| `git reset --hard <commit_hash>`             | Reset the current branch to a specific commit, discarding all changes after that commit.            |
| `git diff`                                   | Show differences between the working directory and the staging area.                                |
| `git diff <branch_name>`                     | Compare the current branch with `<branch_name>`.                                                    |
| `git rebase <branch_name>`                   | Reapply commits from the current branch on top of `<branch_name>` commits.                          |
| `git remote -v`                              | Display the URLs of remote repositories.                                                            |
| `git tag <tag_name>`                         | Create a new tag `<tag_name>` for the current commit.                                               |
| `git rm <file>`                              | Remove a file from the working directory and stage the deletion.                                    |
| `git clean -f`                               | Remove untracked files from the working directory.                                                  |
| `git cherry-pick <commit_hash>`              | Apply the changes from a specific commit to the current branch.                                     |
| `git reflog`                                 | Show a history of all changes made to the local repository, including branch switches and resets.   |
| `git show --name-only <commit_hash>`         | Show the metadata and list of files changed in a specific commit.                                   |
