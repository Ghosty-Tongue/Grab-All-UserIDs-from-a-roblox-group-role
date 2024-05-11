import requests

def get_group_id():
    group_id = input("Enter the group ID: ")
    return group_id

def display_roles(group_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}/roles"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("List of roles:")
        for index, role in enumerate(data['roles'], start=1):
            print(f"{index}. Role: {role['name']}")
    else:
        print("Failed to retrieve roles.")

def get_selected_role_number():
    while True:
        role_number = input("Enter the role number: ")
        try:
            role_number = int(role_number)
            return role_number
        except ValueError:
            print("Please enter a valid role number.")

def get_role_id(group_id, role_number):
    url = f"https://groups.roblox.com/v1/groups/{group_id}/roles"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        role_id = data['roles'][role_number - 1]['id']
        return role_id
    else:
        print("Failed to retrieve roles.")
        return None

def get_all_user_ids_for_role(group_id, role_id):
    all_user_ids = []
    url = f"https://groups.roblox.com/v1/groups/{group_id}/roles/{role_id}/users?limit=100&sortOrder=Asc"
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for user in data['data']:
                all_user_ids.append(user['userId'])
            url = data.get('nextPageCursor')
        else:
            print(f"Failed to retrieve users for role ID {role_id}")
            break
    return all_user_ids

def save_user_ids_to_file(role_name, group_id, user_ids):
    filename = f"{role_name}_{group_id}.txt"
    with open(filename, "w") as file:
        file.write(",".join(map(str, user_ids)))
    print(f"User IDs have been saved to '{filename}'")

group_id = get_group_id()

display_roles(group_id)

selected_role_number = get_selected_role_number()

role_id = get_role_id(group_id, selected_role_number)

user_ids = get_all_user_ids_for_role(group_id, role_id)

print("User IDs associated with selected role:")
print(",".join(map(str, user_ids)))

save_to_file = input("Do you want to save these user IDs to a text file? (yes/no): ")
if save_to_file.lower() == "yes":
    url = f"https://groups.roblox.com/v1/groups/{group_id}/roles"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        role_name = data['roles'][selected_role_number - 1]['name']
        save_user_ids_to_file(role_name, group_id, user_ids)
    else:
        print("Failed to retrieve roles.")
