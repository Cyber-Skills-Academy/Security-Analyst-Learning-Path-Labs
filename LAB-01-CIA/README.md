# Cybersecurity Principles Lab: Understanding the CIA Triad

Welcome to the Cyber Skills Academy Cybersecurity Principles Lab! This interactive lab is designed to give you hands-on experience with the core principles of cybersecurity: Confidentiality, Integrity, and Availability, collectively known as the CIA Triad. Each section provides step-by-step instructions, guiding you through various tasks and encouraging you to reflect on these essential cybersecurity concepts.

## Prerequisites

- Basic knowledge of Python.
- Python environment set up on your machine.
- Familiarity with Git and GitHub.

## Getting Started

1. Clone this repository to your local machine using `git clone https://github.com/Cyber-Skills-Academy/Security-Analyst-Learning-Path-Labs.git`.
2. Navigate to the repository directory on your computer using `cd LAB-01-CIA`
3. Follow the detailed instructions in each part of the lab.

## Part 1: Confidentiality with Encryption

Confidentiality is about ensuring that no unauthorized individuals can access sensitive information. In this part, we'll use encryption to convert a file from a readable form to an encoded version that can only be decoded or made readable by someone who has the decryption key.

### Instructions

1. Navigate to the `part1_Encryption` folder in your terminal or command prompt.
2. Run the command `python encrypt.py`. This script performs the encryption of the `very_sensitive_data.txt` file, and you'll see an `encrypted_data.txt` file created in the directory.
   - Observe the encrypted file and note how the content is no longer readable, demonstrating the file's confidentiality.
3. Imagine you're securely transmitting this encrypted file to a trusted party. This simulates how encrypted data can be safely shared or stored, as it's unreadable without the appropriate decryption key.
4. Now, it's time to decrypt the file and return it to its original form. Run the command `python decrypt.py` to perform the decryption process.
5. Open and review the decrypted file. Confirm that the content matches the original data, verifying the process's success.

**Discuss:** Consider the role of encryption in protecting sensitive information, especially during transmission over potentially insecure networks, and how it forms a fundamental part of maintaining confidentiality in cybersecurity.

## Part 2: Integrity with Hashing

Integrity involves maintaining the accuracy and consistency of data. It's crucial that information is reliable and not altered in transit. Here, we'll use hashing to create a unique "digital fingerprint" of a file's content, which helps in detecting any unauthorized changes to the data.

### Instructions

1. Navigate to the `part2_Hashing` folder in your terminal or command prompt.
2. Run the command `python hash_file.py`. This script initially generates the SHA-256 hash of the `very_sensitive_data.txt` file and displays it.
   - Note this original hash value; it represents the intact state of the file.
3. Now, the script simulates sending the file over the network to a recipient.
4. Upon "reception", the script automatically calculates the hash of the received file and compares it with the original hash.
   - If the hashes match, the integrity of the file is intact. If not, the file might have been tampered with during transmission.
5. For the second scenario, you're prompted to modify the `very_sensitive_data.txt` file. Open the file and alter its content slightly (e.g., change a digit of a social security number or a letter in a username), then save it.
6. Return to the terminal or command prompt and press `Enter` to have the script recalculate the file's hash.
7. Observe the new hash and compare it with the original. Notice how even the slightest alteration to the file data results in a completely different hash, indicating a breach in integrity.

**Discuss:** Reflect on the crucial role of hashing in maintaining data integrity. Think about how hashing can be used to ensure the authenticity and consistency of data, particularly when it's transferred across networks or stored for long periods. Discuss the implications of a changed hash and the potential consequences in real-world scenarios.

## Part 3: Availability with Data Backup and Recovery

Availability ensures that information and systems are accessible to authorized users when they need it. One of the most common strategies to ensure availability, especially in the face of accidental deletion or data corruption, is through regular backups and having a recovery plan in place.

### Instructions

1. Navigate to the `part3_backup_recovery` folder in your terminal or command prompt.
2. Run the command `python create_backup.py`. This script creates a backup of the `very_important_file.txt` within the `data` folder by copying it to a new `backup` folder.
   - Observe how the script creates a copy of the important file, simulating a backup process.
3. Now, simulate a data loss event by manually deleting the `very_important_file.txt` from the `data` folder.
4. After simulating the data loss, run the command `python simulate_recovery.py`. This script restores the `very_important_file.txt` from the `backup` folder to the `data` folder, simulating a data recovery process.
5. Confirm that the `very_important_file.txt` has been successfully restored to the `data` folder, ensuring its availability even after an unexpected data loss.

**Discuss:** Reflect on the significance of backup and recovery strategies in maintaining data availability. Consider the potential consequences of not having backup mechanisms in place and the business impact in real-world scenarios.


## Conclusion

Congratulations on completing the Cybersecurity Principles Lab! You've gained practical insight into the CIA Triad principles, forming the cornerstone of cybersecurity practices. We encourage you to keep exploring these concepts and consider their applications in various real-world scenarios.

Cybersecurity is a field that requires continuous learning and adaptation. Stay curious, keep learning, and remember, your journey in cybersecurity is just beginning!

**Happy learning and stay safe online!**
