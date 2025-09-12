### 1. How to Use `.gitignore`
In Git, `.gitignore` is a file used to specify which files and directories Git should **ignore** when tracking changes. This is useful for excluding files that don't need to be versioned (e.g., build files, temporary files, IDE configurations, or sensitive information).

1.1 **Create a `.gitignore` file:**
   - In the root directory of your Git repository, create a `.gitignore` file. If the file doesn’t already exist, you can create one manually or by running:
     ```bash
     touch .gitignore
     ```

1.2. **Add patterns to `.gitignore`:**
   - Inside the `.gitignore` file, you can specify files, directories, or patterns that Git should ignore. Common patterns include:
   
     - **Ignore specific files**:
       ```plaintext
       secret.txt
       ```
     - **Ignore all files with a specific extension** (e.g., `.log` files):
       ```plaintext
       *.log
       ```
     - **Ignore entire directories** (e.g., `node_modules`):
       ```plaintext
       node_modules/
       ```
     - **Ignore files or directories recursively**:
       ```plaintext
       temp/*
       ```
     - **Ignore files starting with a dot** (hidden files on Unix-like systems):
       ```plaintext
       .env
       .DS_Store
       ```
     - **Ignore everything except certain files** (using negation `!`):
       ```plaintext
       *.log
       !important.log
       ```

1.3. **Examples of a typical `.gitignore` file:**

   For a Node.js project, it might look like this:
   ```plaintext
   node_modules/
   npm-debug.log
   .env
   .DS_Store
   ```

   For a Python project:
   ```plaintext
   __pycache__/
   *.pyc
   .env
   ```

1.4. **Apply `.gitignore` changes:**
   - Once you’ve edited your `.gitignore` file, Git will ignore the files and directories you've specified. However, if you've already tracked those files in a previous commit, Git will still keep track of them.
   - To **remove previously tracked files** that should be ignored, you can use:
     ```bash
     git rm --cached <file>
     ```
     This will remove the file from version control while leaving it in your working directory.

1.5. **Check if `.gitignore` is working:**
   - You can use `git status` to see which files are being tracked and which are ignored. Ignored files won’t show up in the output of `git status`.

### Notes:
- `.gitignore` files are usually committed to the repository, so other developers working on the same project will have the same ignore rules.
- You can also find useful `.gitignore` templates for various programming languages and frameworks at [GitHub’s gitignore repository](https://github.com/github/gitignore).


### 2. **`git restore`**
   - The `git restore` command is used to **restore files in your working directory** to a particular state, typically from a commit, a branch, or the staging area.
   - Common usage:
     - **Restore file(s) to the last committed state:**
       ```bash
       git restore <file>
       ```
     - **Discard all changes in the working directory:**
       ```bash
       git restore .
       ```
     - **Restore a file from a specific commit:**
       ```bash
       git restore --source <commit_hash> <file>
       ```
   - It’s often used to undo changes in your working directory or unstaged changes.

### 3. **`git reset`**
   - The `git reset` command is used to **undo commits** and move the HEAD to a previous state. It can also be used to change the staging area.
   - There are three main types of resets:
     - **Soft Reset** (`--soft`): Moves the HEAD to the specified commit but **keeps changes in the working directory and staging area**.
       ```bash
       git reset --soft <commit_hash>
       ```
     - **Mixed Reset** (`--mixed`, default): Moves the HEAD to the specified commit and **unstages files** but **keeps changes in the working directory**.
       ```bash
       git reset --mixed <commit_hash>
       ```
     - **Hard Reset** (`--hard`): Moves the HEAD to the specified commit and **discards changes in both the working directory and staging area**.
       ```bash
       git reset --hard <commit_hash>
       ```
   - It’s used for undoing commits, and you can choose whether to keep or discard changes.

### 4. **`git revert`**
   - The `git revert` command creates a **new commit** that **undoes the changes** made in a previous commit, leaving the history intact. This is safer for shared repositories because it doesn’t alter commit history.
   - Common usage:
     - **Revert a specific commit:**
       ```bash
       git revert <commit_hash>
       ```
     - This will create a new commit that effectively reverses the changes introduced by the specified commit.
   - It’s ideal when you want to "undo" a commit in a way that preserves history (especially useful when working with shared repositories).

### Summary:
- **`git restore`**: Used to discard changes in the working directory or stage files.
- **`git reset`**: Used to undo commits, modify the staging area, or even discard changes.
- **`git revert`**: Creates a new commit that undoes the changes of a previous commit, preserving history.

Each command has its own use case depending on whether you want to discard, unstage, or preserve history.

# **5. Git Alias**  

Git aliases are shortcuts for Git commands, making your workflow faster and easier. Instead of typing long commands, you can create simple aliases like `git co` instead of `git checkout`.  

---

## **5.1 How to Create a Git Alias**  
Use `git config` to create an alias:  

### **Global Aliases (Works in all repositories)**  
```bash
git config --global alias.co checkout   # Now `git co` = `git checkout`
git config --global alias.br branch    # `git br` = `git branch`
git config --global alias.ci commit    # `git ci` = `git commit`
git config --global alias.st status    # `git st` = `git status`
```

### **Local Aliases (Works only in the current repository)**  
```bash
git config alias.last 'log -1 HEAD'  # Shows the last commit
```

---

## **5.2 Where Aliases Are Stored**  
- **Global aliases** are saved in your **`.gitconfig`** file (located in your home directory):  
  - **Linux/Mac:** `~/.gitconfig`  
  - **Windows:** `C:\Users\YourUsername\.gitconfig`  

- **Local aliases** are stored in the repository's `.git/config` file  

You can directly edit this file to add/remove aliases in the `[alias]` section.  

Example `.gitconfig` snippet:  
```ini
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
```

---

## **5.3 Useful Beginner-Friendly Aliases**  

### **Basic Shortcuts**  
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

### **Log Shortcuts**  
```bash
# Short log format  
git config --global alias.lg "log --oneline --graph"  

# Show last commit  
git config --global alias.last 'log -1 HEAD'  
```

### **Undo & Fix Mistakes**  
```bash
# Unstage a file (keeps changes)  
git config --global alias.unstage 'reset HEAD --'  

# Discard changes in a file  
git config --global alias.discard 'checkout --'  

# Soft undo last commit (keeps changes in staging)  
git config --global alias.undo 'reset --soft HEAD^'  
```

### **Stash Shortcuts**  
```bash
git config --global alias.ss 'stash save'  
git config --global alias.sl 'stash list'  
git config --global alias.sp 'stash pop'  
```

---

## **5.4 How to See All Your Aliases**  
```bash
git config --get-regexp alias  # Lists all aliases
```

---

## **5.5 How to Remove an Alias**  
```bash
git config --global --unset alias.co  # Removes `git co` alias
```

---

## **5.6 Example: Using Aliases in Daily Workflow**  
Before Aliases:  
```bash
git checkout -b new-feature
git add .
git commit -m "Add new feature"
git log --oneline --graph
```

After Aliases:  
```bash
git co -b new-feature
git add .
git ci -m "Add new feature"
git lg
```

---

### **In Short**  
- **`git config --global alias.X Y`** → Creates shortcut `git X` for `git Y`  
- **Aliases are stored in `.gitconfig`** (global) or `.git/config` (local)  
- **Useful for common commands** (`status`, `checkout`, `commit`)  
- **View aliases** with `git config --get-regexp alias`  
- **Remove aliases** with `git config --global --unset alias.X`  

# 6. Branching

- 3 Ways to create a branch

  - git branch second
  - list branches: git branch
  - switch branches: git checkout another_branch
  - another cmd to switch: git switch another_branch
  - no switch and checkout: 
    - create and switch: 
      - git checkout -b another_branch (in older versions of git)
      - git switch -c anothor_branch (in newer versions of git)
    - git push -u oring another_branch
  -  Delete branch
    - git branch -D branch_name
      - you can't delete the branch in which you are working, first checkout and then delete
  - git merge feature_branch, you are currently in main branch

    
# **6. Branching: Create, Switch, Merge & Delete Branches**

Branches let you work on different features or fixes without affecting the main code. Here's a complete guide to managing branches.

## **6.1 Creating Branches (3 Ways)**
1. **Basic branch creation** (doesn't switch to it):
   ```bash
   git branch feature-login
   ```

2. **Create and switch immediately (old method)**:
   ```bash
   git checkout -b feature-login
   ```

3. **Create and switch (new method - Git 2.23+)**:
   ```bash
   git switch -c feature-login
   ```

## **6.2 Switching Between Branches**
- **Traditional method**:
  ```bash
  git checkout main
  ```

- **Modern method (Git 2.23+)**:
  ```bash
  git switch main
  ```

- **List all branches** (asterisk shows current branch):
  ```bash
  git branch
  ```

## **6.3 Pushing Branches to Remote**
```bash
git push -u origin feature-login  # -u sets upstream tracking
```

## **6.4 Merging Branches**
1. First switch to the target branch (usually main):
   ```bash
   git switch main
   ```

2. Then merge your feature branch:
   ```bash
   git merge feature-login
   ```

3. If conflicts occur:
   ```bash
   # Resolve conflicts manually, then:
   git add .
   git commit
   ```

## **6.5 Deleting Branches**
- **Delete local branch** (after merging):
  ```bash
  git branch -d feature-login
  ```

- **Force delete unmerged branch**:
  ```bash
  git branch -D feature-login
  ```

- **Delete remote branch**:
  ```bash
  git push origin --delete feature-login
  ```

**Important**: You can't delete the branch you're currently on. First switch to another branch:
```bash
git switch main
git branch -d feature-login
```

## **6.6 Typical Workflow Example**
1. Create and switch to new branch:
   ```bash
   git switch -c feature-payment
   ```

2. Make changes and commit:
   ```bash
   git add .
   git commit -m "Add payment processing"
   ```

3. Push to remote:
   ```bash
   git push -u origin feature-payment
   ```

4. When done, merge to main:
   ```bash
   git switch main
   git merge feature-payment
   ```

5. Clean up (optional):
   ```bash
   git branch -d feature-payment
   git push origin --delete feature-payment
   ```

### **Key Takeaways**
- Use `git switch -c` for creating+switching (modern)
- Always merge to main from the main branch
- Delete branches safely after merging
- Remember you can't delete your current branch

Branches keep your work organized and manageable! 🌿

# **7. Git Amend: Edit Your Last Commit**

The `git commit --amend` command lets you modify your most recent commit instead of creating a new one. This is useful for:
- Fixing typos in commit messages
- Adding forgotten files to the last commit
- Making small changes without cluttering history

## **7.1 Basic Usage**
```bash
# 1. First, stage any new changes you want to add:
git add .

# 2. Amend the commit (opens editor to edit message):
git commit --amend
```

## **7.2 Changing Just the Commit Message**
```bash
git commit --amend -m "New improved commit message"
```

## **7.3 Important Notes**
**Never amend commits that have been pushed to a shared repository**  
- This changes the commit hash and can cause problems for others  
- Only amend local commits that haven't been pushed yet  

## **7.4 When to Use Amend**
- Forgot to add a file to last commit  
- Need to fix a typo in commit message  
- Made a small change right after committing  

---

# **8. Git Clone: Copying Repositories**

Always use `git clone` instead of downloading ZIP files because:
- ZIPs don't include the `.git` folder (no version control)
- You lose all commit history and branch information

## **8.1 Basic Cloning**
```bash
# Clone the main branch of a repository
git clone https://github.com/user/repo.git
```

## **8.2 Cloning Specific Branches**
```bash
# Clone a specific branch only
git clone --branch feature/login https://github.com/user/repo.git
```

## **8.3 Cloning into a Different Folder**
```bash
git clone https://github.com/user/repo.git my-project-folder
```

## **8.4 Cloning Submodules Too**
```bash
git clone --recurse-submodules https://github.com/user/repo.git
```

## **8.5 Key Differences: Clone vs Download**
| Feature        | `git clone` | ZIP Download |
|---------------|------------|-------------|
| Keeps git history | ✅ Yes | ❌ No |
| Includes all branches | ✅ Yes | ❌ No |
| Easy to update | ✅ Yes (git pull) | ❌ No |
| Maintains remotes | ✅ Yes | ❌ No |

**Remember:** Always clone instead of downloading to get the full Git functionality!



# **9. Git Fetch vs. Pull: Updating Your Repository**

## **9.1 Git Fetch: Safe Checking of Remote Changes**
```bash
git fetch
```
- **What it does**: Downloads all changes from remote but doesn't merge them
- **Why use it**:
  - Safely check what others have pushed
  - Review changes before merging
  - Doesn't affect your working directory
- **What happens**:
  - Updates remote-tracking branches (origin/main)
  - Doesn't change your local branches

## **9.2 Git Pull: Fetch + Merge**
```bash
git pull
```
- **What it does**: Fetches AND automatically merges changes
- **Equivalent to**:
  ```bash
  git fetch
  git merge origin/main
  ```
- **Danger**: Can create merge conflicts if you have uncommitted changes

## **9.3 Pull with Rebase (Cleaner History)**
```bash
git pull --rebase
```
- **Why better**:
  - Puts your commits on top of others'
  - Avoids unnecessary merge commits
  - Keeps history linear
- **Equivalent to**:
  ```bash
  git fetch
  git rebase origin/main
  ```

## **9.4 Key Differences**
| Command | Action | Safe? | Affects Working Dir? |
|---------|--------|-------|----------------------|
| `fetch` | Downloads changes | ✅ Yes | ❌ No |
| `pull` | Downloads + merges | ❌ Risk of conflicts | ✅ Yes |
| `pull --rebase` | Downloads + rebases | ⚠️ Careful with conflicts | ✅ Yes |

## **9.5 Best Practices**
1. **Before pushing**: Always `fetch` first to check for remote changes
2. **Clean history**: Prefer `pull --rebase` over regular pull
3. **With local changes**:
   ```bash
   git stash        # Save your changes
   git pull         # Update
   git stash pop    # Reapply changes
   ```

**Remember**: 
- `fetch` = look before you leap
- `pull` = get changes immediately
- `pull --rebase` = keep history clean



# **10. Git Diff: Comparing Changes**

Git Diff helps you see exactly what changes you've made in your code. Here are the most useful variations:

## **10.1 Basic Comparisons**

```bash
# Show unstaged changes (working directory vs index)
git diff

# Show staged changes (index vs last commit)
git diff --staged
# or (older Git versions)
git diff --cached
```

## **10.2 Comparing Specific Things**

```bash
# Compare working directory with a specific commit
git diff commit-hash

# Compare two branches
git diff branch1..branch2

# Compare two specific commits
git diff commit1..commit2
```

## **10.3 Helpful Output Formats**

```bash
# Show only names of changed files
git diff --name-only

# Show changes in a word-by-word format (easier to read)
git diff --word-diff
# or with colors
git diff --color-words

# Show changes side-by-side
git diff --color-words --word-diff-regex="[^[:space:]]|([[:alnum:]]|UTF-8)"
```

## **10.4 Limiting Comparisons**

```bash
# Show changes only in a specific file
git diff filename

# Show changes for a specific directory
git diff dirname/

# Show changes made in the last hour
git diff 'HEAD@{1 hour ago}'
```

## **10.5 Visualizing Changes**

For a more visual representation, you can use:
```bash
# Use a GUI diff tool (configure first)
git difftool
```

## **10.6 Common Workflow Examples**

1. **Before staging files**:
   ```bash
   git diff  # See what you've changed
   ```

2. **After staging but before committing**:
   ```bash
   git diff --staged  # Review what will be committed
   ```

3. **Checking what will be pushed**:
   ```bash
   git diff origin/main..HEAD  # Compare local with remote
   ```

## **10.7 Pro Tip**

Create handy aliases in your `.gitconfig`:
```ini
[alias]
    changes = diff --name-only
    word-diff = diff --word-diff
```

Remember: Git Diff is your best friend for understanding exactly what changes you're about to commit or push!


# 11. Skip Staging Area

git commit -a -m "Skip staging area"

git commit <file_name> -m "Commit message"


# 12. Git Stash

Store changes in a temporary area without commit? 

Store changes in a temporary area that you haven't committed after the previous commit

helps in working multiple branches

git stash list

git stash apply

# 13. Colloboration
Credential Manager


# 14. README
sheilds.io


# 15. GitHub Actions

# Workflows
Event: Triggers
Job: Tasks/Set of steps
Step: Single tasks
Runner: Virtual Machine | GitHub hosted/self hosted


Workflow execution flow: Event occurs --> Workflow start --> Jobs execute in paralle(by default)


# Create first workflow

<!-- Workflow name -->
name: my_workflow

<!-- Event -->
on: 
  push:
    branches: [main]
<!-- on any puch in main branch do the jobs-->


jobs:
<!-- job name demo its variable -->
  demo: 
  <!-- the runner -->
    runs-on: ubuntu-latest  

  <!-- Tasks for runner -->
    steps:
      - name: Greetings
        run: echo "Hello biruu"


# Schduling Workflows

name: Schedular

on: 
  schedule:
    <!-- Command Run ons: Minutes Hourse Day Week -->
    - crons: "0 0 * * *"

jobs:
  run-scripts:
    runs-on: ubunte-latest

    steps:
      - name: print message
      run: echo "Schedular triggered"


# Disabling workflows

name: disable workflow

on:
  disable:
    branches: [main]

jobs:
  disable:
    runs-on: ubuntu-latest


    steps:
      - name: disabling
        run: echo "workflow disabled"


### Click on 3 dots in right corner and click on disable workflow


# Caching & Artifacts
Caching: Fast the workflow execution
Artifacts: Save the build and debug, download or deploy

# Job Concurrency
Make a build of the latest commit


# 16. Generating SSH Keys

We can link multiple github accounts at a time on a single system by generating multiple ssh keys.

This eliminates the process of manually configuring the email, user name, and updating the credential manager


In simple ek laptop pe multiple github accounts k saath kaam kar sakte and woh b https se ziada secure



ssh-keygen -t ed25519 -C "githubemail"
public key and private key

### MUST DO TASK



