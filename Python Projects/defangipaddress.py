# it is used for the purpose of adding security like encryption.
# make the ip address into some other format for encryption


def ip_address(address):
    # we declare one address variable
    new_address = ""
    # split the address using split function i
    split_address = address.split(" ")
    separator = "iswasthat"
    # join is used to merge separator and the split address
    new_address = separator.join(split_address)
    return new_address


ipaddress = ip_address("1 1 0 0 0 0 2 5 6")
print(ipaddress)
