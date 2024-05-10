from BlitzWareAuth import API
import time

# BlitzWare Python example
# Please read our docs at https://docs.blitzware.xyz/

BlitzWareAuth = API("https://api.blitzware.xyz/api",
                    "NAME", "SECRET", "VERSION")

print("\n\nConnecting...")
BlitzWareAuth.initialize()
print("Connected!")

print("\n[1] Login\n[2] Register\n[3] Upgrade\n[4] License key only\n")
option = int(input("Choose option: "))

username, email, password, two_factor_code, key = "", "", "", "", ""

if option == 1:
    username = input("\n\nEnter username: ")
    password = input("\n\nEnter password: ")
    two_factor_code = input("\n\nEnter 2FA (if enabled): ")
    if not BlitzWareAuth.login(username, password, two_factor_code):
        exit(0)
    BlitzWareAuth.log("User logged in")
elif option == 2:
    username = input("\n\nEnter username: ")
    password = input("\n\nEnter password: ")
    email = input("\n\nEnter email: ")
    key = input("\n\nEnter license: ")
    if not BlitzWareAuth.register(username, password, email, key):
        exit(0)
    BlitzWareAuth.log("User registered")
elif option == 3:
    username = input("\n\nEnter username: ")
    password = input("\n\nEnter password: ")
    key = input("\n\nEnter license: ")
    if not BlitzWareAuth.extend(username, password, key):
        exit(0)
    BlitzWareAuth.log("User extended")
elif option == 4:
    key = input("\n\nEnter license: ")
    if not BlitzWareAuth.login_license_only(key):
        exit(0)
    BlitzWareAuth.log("User login with license")
else:
    print("\n\nInvalid Selection")
    time.sleep(3)
    exit(0)

print("\nUser data:")
print("Username: " + BlitzWareAuth.user_data.username)
print("Email: " + BlitzWareAuth.user_data.email)
print("IP-address: " + BlitzWareAuth.user_data.lastIP)
print("Hardware-Id: " + BlitzWareAuth.user_data.hwid)
print("Last login: " + BlitzWareAuth.user_data.lastLogin)
print("Subscription expiry: " + BlitzWareAuth.user_data.expiryDate)

# BlitzWareAuth.download_file("2ff23a2e-80f1-486a-a117-4c0f55fb1edd")

print("\nClosing in five seconds...")
time.sleep(5)
exit(0)
