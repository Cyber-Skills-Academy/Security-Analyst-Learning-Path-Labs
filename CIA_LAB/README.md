# Cybersecurity Principles Lab: Understanding the CIA Triad

Welcome to the Cyber Skills Academy Cybersecurity Principles Lab! This interactive lab is designed to give you hands-on experience with the core principles of cybersecurity: Confidentiality, Integrity, and Availability, collectively known as the CIA Triad. Each section provides step-by-step instructions, guiding you through various tasks and encouraging you to reflect on these essential cybersecurity concepts.

## Prerequisites

- Basic knowledge of Python.
- Python environment set up on your machine.
- Familiarity with Git and GitHub.

## Getting Started

1. Clone this repository to your local machine using `git clone <repository_url>`.
2. Navigate to the repository directory on your computer.
3. Follow the detailed instructions in each part of the lab.

## Part 1: Confidentiality with Encryption

Confidentiality is about ensuring that no unauthorized individuals can access sensitive information. In this part, we'll use encryption to convert a file from a readable form to an encoded version that can only be decoded or made readable by someone who has the decryption key.

### Instructions

1. Navigate to the `Part_1_Encryption` folder in your terminal or command prompt.
2. Run the command `python encrypt.py`. This script performs the encryption of the `very_sensitive_data.txt` file, and you'll see an `encrypted_data.txt` file created in the directory.
   - Observe the encrypted file and note how the content is no longer readable, demonstrating the file's confidentiality.
3. Imagine you're securely transmitting this encrypted file to a trusted party. This simulates how encrypted data can be safely shared or stored, as it's unreadable without the appropriate decryption key.
4. Now, it's time to decrypt the file and return it to its original form. Run the command `python decrypt.py` to perform the decryption process.
5. Open and review the decrypted file. Confirm that the content matches the original data, verifying the process's success.

**Discuss:** Consider the role of encryption in protecting sensitive information, especially during transmission over potentially insecure networks, and how it forms a fundamental part of maintaining confidentiality in cybersecurity.

## Part 2: Integrity with Hashing

Integrity involves maintaining the accuracy and consistency of data. It's crucial that information is reliable and not altered in transit. Here, we'll use hashing to create a unique "digital fingerprint" of a file's content, which helps in detecting any unauthorized changes to the data.

### Instructions

1. Navigate to the `Part_2_Hashing` folder.
2. Run the command `python hashing.py` to generate and display the hash of the `very_sensitive_data.txt` file.
   - Note this original hash value; it represents the current state of the file.
3. Now, let's simulate an unauthorized modification. Open `very_sensitive_data.txt` and make a small change to the file's content (like adding or removing a word).
4. Run the `python hashing.py` command again to generate a new hash value for the modified file.
5. Compare the new hash with the original. Even a minor change to the data causes a significant change in the hash, indicating that the file's integrity has been compromised.

**Discuss:** Reflect on the critical role of hashing in ensuring data integrity, allowing us to detect even the slightest alterations.

## Part 3: Availability with Data Backup and Recovery

Availability ensures that data is accessible to authorized users when needed. This aspect of the CIA Triad is often implemented through backup and recovery strategies, which we will explore in this section.

### Instructions

1. Navigate to the `Part_3_Availability` folder.
2. Imagine a scenario where the original data file is lost or corrupted. Such an incident can severely impact an organization's operations and data availability.
3. Run the command `python backup_recovery.py` to simulate the restoration of the file from a backup.
   - This script represents a simplified version of data recovery processes that organizations use to restore data availability.
4. Verify that the content of the restored file matches the original file, emphasizing the importance of regular backups.

**Discuss:** Consider the implications of data loss and the significance of backup and recovery strategies in maintaining data availability.

## Conclusion

Congratulations on completing the Cybersecurity Principles Lab! You've gained practical insight into the CIA Triad principles, forming the cornerstone of cybersecurity practices. We encourage you to keep exploring these concepts and consider their applications in various real-world scenarios.

Cybersecurity is a field that requires continuous learning and adaptation. Stay curious, keep learning, and remember, your journey in cybersecurity is just beginning!

**Happy learning and stay safe online!**
