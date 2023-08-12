import instaloader

# Create an instance of the Instaloader class
loader = instaloader.Instaloader()

# Load the profile of the user whose followers you want to retrieve
profile = instaloader.Profile.from_username(loader.context, 'mahesh._.sirsat')

# Retrieve and print the followers of the user
followers = [follower.username for follower in profile.get_followers()]
print(followers)

