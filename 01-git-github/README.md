
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

