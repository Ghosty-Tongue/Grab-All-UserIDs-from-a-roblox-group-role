# Roblox Group Role User ID Collector

This tool allows you to easily collect user IDs under a specific role in a Roblox group.

## Description

This tool simplifies the process of gathering user IDs associated with a particular role within a Roblox group. It is useful for various purposes, including moderation, analytics, and community management.

## Features

- Retrieve user IDs associated with a specified role in a Roblox group.
- Easy-to-use command-line interface.
- Ability to save user IDs to a text file for further analysis.

## Requirements

- Python 3.x
- Requests library (install via `pip install requests`)

## Usage

1. Clone the repository:

git clone https://github.com/Ghosty-Tongue/roblox-group-role-userid-collector.git

2. Navigate to the project directory:

cd roblox-group-role-userid-collector

3. Run the script:

python roblox_group_role_userid_collector.py

4. Follow the on-screen instructions to enter the group ID and select the role.
5. Optionally, choose to save the user IDs to a text file.

## Example

Here's a brief example of how to use the tool:

Enter the group ID: 123456
List of roles:
1. Role: Admin
2. Role: Moderator
3. Role: Member
Enter the role number: 2
User IDs associated with selected role:
123456789,987654321,555555555
Do you want to save these user IDs to a text file? (yes/no): yes
User IDs have been saved to 'Moderator_123456.txt'

## License

This project is licensed under the [MIT License](LICENSE).
