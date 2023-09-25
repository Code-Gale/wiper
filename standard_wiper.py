import os

def wipe_hard_drive(drive_path):
    try:
        with open(drive_path, 'wb') as file:
            file.seek(0, os.SEEK_END)
            drive_size = file.tell()
            num_passes = 3 #You can increase this for more thorough wiping if there's more time
            
            for _ in range(num_passes):
                file.write(os.urandom(drive_size))
                file.seek(0)
        
        print(f"Drive at {drive_path} has been securely wiped.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'drive_path' with the path to your laptop's hard drive (e.g., '/dev/sda' on Linux 'C:/Users/NameOfUser" on Windows)
drive_path = '/dev/sda'  # Please be extremely cautious and double-check the drive path!
wipe_hard_drive(drive_path)
