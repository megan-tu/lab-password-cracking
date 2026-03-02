import zipfile

def password_cracker():
    #with Zipfile('whitehouse_secrets.zip') as zf:
    with open("Ashley-Madison.txt", "r", encoding='utf-8', errors='ignore') as file:
        passwords = [line.strip() for line in file]
        with zipfile.ZipFile("whitehouse_secrets.zip") as zf:
            for i, password in enumerate(passwords, start=1):
                try:
                    zf.extractall(pwd=password.encode("utf-8"))
                    print(f"\nPassword found: {password}")
                    break
                except:
                    if i % 10000 == 0:
                        print(f"Attempt #{i}: currently trying '{password}'")
                    continue
            else:
                print("Password not found")
if __name__ == '__main__':
    password_cracker()