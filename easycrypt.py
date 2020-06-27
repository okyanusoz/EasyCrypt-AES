import classes

print("EasyCrypt AES-256 Edition");
print("----KEYFILE SELECTION----");
keyfilename = input("Please enter the keyfile's name: ");
key = open(keyfilename, "rb").read();
print("");
while True:
    print("Menu:\n1 - Encrypt file\n2 - Decrypt file\n3 - Exit");
    try:
        option = int(input("Select an option: "));
    except:
        print("Error");
        continue;
    if(not option in [1, 2, 3]):
        continue;
    if(option == 1):
        print("Encrypt file");
        fname = input("File to encrypt(Encrypted file extension will be .easycrypt): ");
        output_filename = fname + ".easycrypt";
        classes.encryptfile(output_filename, fname, key);
        print("Done!");
    elif(option == 2):
       print("Decrypt file");
       encryptedf = input("Encrypted filename(with the extension): ");
       newfile = input("Decrypted filename: ");
       try:
           classes.decryptfile(encryptedf, key, newfile);
       except:
           print("Unexpected error. Please make sure the key is the exact key you used to encrypt the file.");
    elif(option == 3):
        exit();