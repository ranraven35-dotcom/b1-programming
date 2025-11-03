login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]

print("Checking login attempts...")
failed_counts = {}

# Count failed login attempts
for username, status in login_attempts:
    if status == "failed":
        if username in failed_counts:
            failed_counts[username] = failed_counts[username] + 1
        else:
            failed_counts[username] = 1

# Check for accounts that failed 3 or more times
for username in failed_counts:
    if failed_counts[username] >= 3:
        print("ALERT: User '" + username + "' has " + str(failed_counts[username]) + " failed login attempts")

print("Security check complete")
