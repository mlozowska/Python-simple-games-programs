email = input("Enter you email address: ").strip()

# slice and store username
username = email[:email.index("@")]

# slice and store domain name
domain = email[email.index("@")+1:]

# make output result using username and domain name
result = "Your username = {}\n Your domain = {}".format(username, domain)

# print the result
print(result)