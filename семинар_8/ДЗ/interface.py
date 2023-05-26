def start ():
    path = 'phone_book.txt'

    try:
        file = open(path, 'r')
    except IOError:
        print('New data file created -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()
