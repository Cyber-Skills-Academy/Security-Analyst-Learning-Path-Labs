import shutil
import os

def create_backup():
    # Define the source and destination paths
    source = 'data/very_important_file.txt'
    destination = 'backup/very_important_file.txt'

    # Create a backup folder if it doesn't exist
    if not os.path.exists('backup'):
        os.makedirs('backup')

    # Copy the file to the backup folder
    shutil.copy2(source, destination)
    print(f'Backup of {source} created at {destination}')

if __name__ == "__main__":
    create_backup()
