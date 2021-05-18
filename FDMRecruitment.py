def main():
    while True:
        try:
            ncovert = int(input("Please Enter your Number to Convert: \n"))
        except ValueError:
            print("Invalid Input")
            continue
        if (ncovert > 0 and isinstance(ncovert, int)):
            lcdfunction(ncovert)
            break
        else:
            print("Not a Valid Integer")
        
        

def lcdfunction(convert):
    print("Addhere")

if __name__ == '__main__':
    main()