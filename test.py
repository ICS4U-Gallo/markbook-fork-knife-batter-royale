def main():
    f = open("marks.txt", "r")
    #for i in range(10):
    #    f.write("Hello World\n")
    content = f.read()
    print(content)
    

if __name__ == "__main__":
    main()