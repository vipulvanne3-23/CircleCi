from Main1 import Add, Display

def TestAdd():
    assert Add(3, 4) == 9
    print("Add Function works correctly")

if __name__ == '__main__':
    TestAdd()
    Display()  # Test Display function as well
