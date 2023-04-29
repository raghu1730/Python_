print("This will run always")
def main():
    print("First Module's Name:{}".format(__name__))
if __name__ =="__main__":
        main()
#if __name__ == '__main__':
#    print("Run Directly")
#else:
#    print("Run from import")




#def add(a, b):
#    return a + b
#print(__name__)
#if __name__ == "__main__":
#    print(add(10,16))