# git commit --amend --date = "2023-08-17 12:00:00""

from git import Repo
import datetime
import pytz

# Specify the path to the Git repository
repo_path = '/Users/danishgada/PycharmProjects/github'

# Open the repository
repo = Repo(repo_path)

# Get the current branch
branch = repo.active_branch

# Create a new file and add content
file_path = 'example_file.txt'
file_content = 'This is an example file created for educational purposes.'

with open(file_path, 'w') as file:
    file.write(file_content)

# Stage the changes
repo.index.add([file_path])

# Set the desired timestamp (replace with your desired date and time)
string_date = "2023-08-14 12:00:04"
desired_timestamp = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")

# Attach a timezone to the datetime object
timezone = pytz.timezone('UTC')  # Replace with your desired timezone
desired_timestamp = timezone.localize(desired_timestamp)


# # Commit the changes with the desired timestamp
# author = repo.config_writer().get_value('user', 'dan')
# committer = repo.config_writer().get_value('user', 'dan')

repo.index.commit('Add ex', commit_date=desired_timestamp)

# Push the changes to the remote repository
remote = repo.remotes.origin  # Replace 'origin' with your remote's name
remote.push(branch)
