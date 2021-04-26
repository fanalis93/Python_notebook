def main():
    # Lambda function to check if a given vaue is from 10 to 20.
    test = lambda x : True if (x > 10 and x < 20) else False
    # Check if given numbers are in range using lambda function
    print(test(12))
    print(test(3))
    print(test(24))

    check = lambda x : x > 10 and x < 20
    # Check if given numbers are in range using lambda function
    print(check(12))
    print(check(3))
    print(check(24))

    converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)
    print('convert 5 to : ', converter(5))
    print('convert 13 to : ', converter(13))
    print('convert 23 to : ', converter(23))
    

if __name__ == '__main__':
    main()