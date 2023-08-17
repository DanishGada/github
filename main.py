# git commit --amend --date = "2023-08-17 12:00:00""

import subprocess

# Change to your Git repository directory
repo_directory = '/Users/danishgada/PycharmProjects/github'
# Change directory to the Git repository
for x in range(5):
    commit_message = 'amendCommits' + str(x)
    date = "2023-08-17 12:00:0" + str(x)
    subprocess.call(['git', 'commit', '--amend', '--date=' + date, '-m', commit_message], cwd=repo_directory)
    subprocess.call(['git', 'push'], cwd=repo_directory)
