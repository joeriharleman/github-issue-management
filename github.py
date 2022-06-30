#!/usr/bin/python3

github_pat = "MY_TOKEN" # Github Personal Access Token (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

import math
import time
from ghapi.all import GhApi
from colorama import Fore, Style

api = GhApi(owner='OWNER', repo='REPO', token=github_pat) # Please replace OWNER and REPO with your repository info!

def fetchPagedIssues(issues = [], page = 1):
	repo_issues = api.issues.list_for_repo(state="open", per_page=100, page=page)
	issues.extend(repo_issues)
	if len(repo_issues) == 100:
		fetchPagedIssues(issues, page+1)
	return issues

def filterIssuesOnly(issues):
	issuesOnly = []
	for issue in issues:
		if not hasattr(issue, 'pull_request'):
			issuesOnly.append(issue)
	return issuesOnly

def filterPullRequestsOnly(issues):
	prsOnly = []
	for issue in issues:
		if hasattr(issue, 'pull_request'):
			prsOnly.append(issue)
	return prsOnly

def commentOnIssue(issue):
	message = """Hello @%s!

MESSAGE

Kind regards,
NAME""" % issue.user.login  # Please replace MESSAGE and NAME with an actual message and your name!
	api.issues.create_comment(issue_number=issue.number, body=message)

def closeIssue(issue):
	api.issues.update(issue_number=issue.number, state="closed")

def printIssueInfo(issue):
	msg = "#%d %s" % (issue.number, issue.title)
	print (msg, end = '')
	printTab(len(msg), tabs)

def printTab(text_length, desired = 12):
	amountOfTabs = int(math.ceil(desired - (text_length / 8)))
	tabs = 0
	while(tabs < amountOfTabs):
		print('\t', end='')
		tabs+=1

def printOk():
	print ("%sOK%s" % (Fore.GREEN, Style.RESET_ALL))

def getLongestTitleLength(issues):
	longest = 0
	for issue in issues:
		titleLength = len(issue.title)
		if titleLength > longest:
			longest = titleLength
	return longest

repo_issues = fetchPagedIssues()
issues = filterIssuesOnly(repo_issues)
prs = filterPullRequestsOnly(repo_issues)
tabs = int(math.ceil((getLongestTitleLength(repo_issues) / 8) + 1))

print("Issues for repository:")
for issue in issues:
	printIssueInfo(issue)
	commentOnIssue(issue)
	closeIssue(issue)
	printOk()
	time.sleep(5) # Prevent rate limiting

print("Total: %d issues" %(len(issues)))
print("")
print("PRs for repository:")
for pr in prs:
	printIssueInfo(pr)
	printOk() # Only print the issue and do nothing else for now.

print("Total: %d PRs" % (len(prs)))
