import os

def file_manager_demo():
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}\n")
    
    folder_name = "lab_files"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"✓ Created folder: {folder_name}")
    else:
        print(f"Folder '{folder_name}' already exists")
    
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            f.write(f"This is {file_name}")
        print(f"✓ Created file: {file_name}")
    
    print(f"\n=== Files in {folder_name} ===")
    files = os.listdir(folder_name)
    for file in files:
        print(f"- {file}")
    
    old_path = os.path.join(folder_name, "file2.txt")
    new_path = os.path.join(folder_name, "renamed_file.txt")
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"\n✓ Renamed 'file2.txt' to 'renamed_file.txt'")
    
    print(f"\n=== Files after rename ===")
    files = os.listdir(folder_name)
    for file in files:
        print(f"- {file}")
    
    print(f"\n=== Cleaning up ===")
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        os.remove(file_path)
        print(f"✓ Deleted: {file}")
    
    os.rmdir(folder_name)
    print(f"✓ Removed folder: {folder_name}")
    print("\nAll cleanup completed successfully!")

file_manager_demo()
