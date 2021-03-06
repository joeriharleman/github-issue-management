# Python script for simple Github Issue Management
I had a use case where I needed to close a bunch of stale issues. I ended up manually closing some more recent ones, all that remained were stale issues. This is why there's no filtering or querying for issues, this script simply takes all open issues that are not PRs in a repository and comments on them with a simple message and then closes them. I wrote this simple Python script because I like writing code every once in a while, so this is by no means perfect. Also, yes, I'm aware there's a 1000 libraries and scripts that can do this better than me.

## Features
* Uses PAT for authentication
* Outputs all issues in the console
* Can close about 1 issue every 5 seconds (rate limiting), you can remove this easily if you don't want this.
* It distinguishes between PRs and regular issues.

## Usage
1. Open `github.py` and fill in all variables in the script.
2. Create a virtual environment:
```shell
venv create
```

3. Activate the new virtual environment:
```shell
source bin/activate
```

4. Install Python dependencies:
```shell
pip install -r requirements.txt
```

5. Mark as executable:
```shell
chmod +x github.py
```

6. Execute script:
```shell
./github.py
```