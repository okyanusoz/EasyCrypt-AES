import classes
import os

print("EasyCrypt AES-256 Edition - Folder decryption\nPlease make sure the encrypted files end with .easycrypt otherwise EasyCrypt will ignore it.");
print("----KEYFILE SELECTION----");
keyfilename = input("Please enter the keyfile's name: ");
key = open(keyfilename, "rb").read();
print("");
foldername = input("Folder name: ");
if(not os.path.isdir(foldername)):
    print("Invalid folder");
    exit();
folderdata = os.listdir(foldername);
while True:
    q = input("Delete encrypted files?(yes/no): ");
    if(not q.lower() in ["yes", "no"]):
        print("Invalid choice");
        continue;
    if(q.lower() == "yes"):
        deleteoriginal = True;
    elif(q.lower() == "no"):
        deleteoriginal = False;
    break;
print("Decrypting files....\nThis may take some time depending on the folder size.");
def decryptdir(_dir):
    for i in os.listdir(_dir):
        path = os.path.join(_dir, i);
        if(os.path.isdir(path)):
            decryptdir(os.path.join(_dir, i));
            continue;
        newname = os.path.join(_dir, i.replace(".easycrypt", ""));
        if(not i.endswith(".easycrypt")):
            continue;
        try:
            classes.decryptfile(path, key, newname);
        except:
            print("Unexpected error, skipping file " + i);
            continue;
        if(deleteoriginal):
            os.remove(path);

decryptdir(foldername);
print("Done!");