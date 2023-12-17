# This is a Python script to read words from a file and print sorted word list.

def sort_words(x):

    f = open(x, "r")
    y = f.read()
    z = y.lower().split()
    z.sort()
    print(z)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Enter the full path for data file:')


    try:
        x = input()
        print("this is your input:" + x)
        sort_words(x)
    except FileNotFoundError:
        print("Please provide a correct path")
    except:
        print("Something else went wrong")





