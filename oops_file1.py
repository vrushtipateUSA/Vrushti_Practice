class ABC:
    def method(self):
        print("We are in ABC class")


if __name__ == '__main__':
    obj = ABC()
    #get class name
    print("class name :", obj.__class__)

    #get module name
    print("module name :", obj.__module__)