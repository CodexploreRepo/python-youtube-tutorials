def cToFConverter():
    while True:
        cTemp = input("Please enter C degree: ")
        if cTemp:
            # print(type(cTemp))
            cTemp = float(cTemp)  # str to float
            fTemp = round(9*cTemp/5 + 32, 1)

            print(f"{cTemp}C is converted to {fTemp}F")
            break
        else:
            print("cTemp input is empty")
            continue


def main():
    #print("Hello World")
    cToFConverter()


if __name__ == "__main__":
    main()
