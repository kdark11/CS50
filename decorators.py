def announce(f):
    def wrapper():
        print("about to run function...")
        f()
        print("Done running function.")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()