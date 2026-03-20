import os
import subprocess

def find_and_open():
    filename = input("🔍 Enter the filename (e.g., main.py): ").strip()
    search_root = "F:\\" # here you can change the root directory to search in, e.g., "C:\\", "D:\\", etc.
    
    print(f"⏳ Searching for {filename} on drive {search_root}... This might take some time.")
    
    matches = []
    
    # Walk through the directory tree and find all matches
    for root, dirs, files in os.walk(search_root):
        if filename in files:
            full_path = os.path.join(root, filename)
            matches.append(full_path)

    if not matches:
        print("❌ File not found.")
        return

    # here we have one or more matches
    if len(matches) == 1:
        chosen_path = matches[0]
    else:
        # if find multiple matches, ask user to choose
        print(f"\n📂 Found many same name files '{filename}':")
        for i, path in enumerate(matches, 1):
            print(f"{i}. {path}")
        
        choice = int(input("\n🔢 Choose a file to open: "))
        chosen_path = matches[choice - 1]

    # Magic: open in VS Code
    print(f"🚀 Opening in VS Code: {chosen_path}")
    try:
        # command works if 'code' is in PATH, otherwise it will throw an error
        os.startfile(chosen_path)
    except Exception as e:
        print(f"❌ Failed to open in VS Code. Error: {e}")

if __name__ == "__main__":
    find_and_open()