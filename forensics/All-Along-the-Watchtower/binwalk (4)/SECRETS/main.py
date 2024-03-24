import py7zr

def extract_7z(archive_file, password):
    try:
        with py7zr.SevenZipFile(archive_file, mode='r', password=password) as z:
            z.extractall()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def brute_force(archive_file, password_list):
    for password in password_list:
        print(f"Trying password: {password}")
        if extract_7z(archive_file, password):
            print(f"Password found: {password}")
            return password
    return None

def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = [line.strip() for line in file.readlines()]
    return passwords

def main():
    archive_file = 'protected_2.7z'
    password_file = 'password.txt'
    password_list = read_passwords(password_file)
    result = brute_force(archive_file, password_list)
    if result is None:
        print("Password not found in the list.")

if __name__ == "__main__":
    main()
