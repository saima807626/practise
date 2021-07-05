import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)


#Write a program in python to generate MD5of string data
def md5():

    string = input("Enter a string to convert it into hash: ")
    hash_obj = hashlib.md5(string.encode())
    print(hash_obj.hexdigest())


md5()


#Write a program in python to generate hashes of string data using 3 algorithms from hashlib
#1st algorithm
def SHA1():

    string1 = input("Enter a string to convert it into hash: ")
    hash_obj1 = hashlib.sha1(string1.encode())
    print(hash_obj1.hexdigest())


SHA1()


#2nd algorithm
def SHA224():

    string2 = input("Enter a string to convert it into hash: ")
    hash_obj2 = hashlib.sha224(string2.encode())
    print(hash_obj2.hexdigest())


SHA224()


#3rd algorithm
def SHA384():

    string2 = input("Enter a string to convert it into hash: ")
    hash_obj2 = hashlib.sha384(string2.encode())
    print(hash_obj2.hexdigest())


SHA384()
