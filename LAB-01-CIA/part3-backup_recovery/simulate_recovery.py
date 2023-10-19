import shutil
import os

def simulate_recovery():
    # Define the source and destination paths
    source = 'backup/very_important_file.txt'
    destination = 'data/very_important_file.txt'

    # Restore the file to the data folder
    shutil.copy2(source, destination)
    print(f'File restored from {source} to {destination}')

if __name__ == "__main__":
    simulate_recovery()
