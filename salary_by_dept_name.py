import pandas

def salay_dept(x):

    sum_data_read = pandas.read_csv(x)
    result = sum_data_read.groupby('dept_name')['salary'].sum().reset_index()

    print("Sum of salary by department is as belows:")
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Enter the full path for data file:')


    try:
        x = input()
        print("this is your input path:" + x)
        salay_dept(x)
    except FileNotFoundError:
        print("Error! Please provide a correct path")
        exit(1)
    except:
        print("Something else went wrong")