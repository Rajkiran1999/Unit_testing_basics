import string

def main():

    abc = abc = string.ascii_letters + string.punctuation + string.digits + " "
    char = '('
    shiftby = 450
    print(shiftby%len(abc)) # this gives us the number of effective shifts after cancelling out all the cycles hat you inevitably make
    if shiftby > 0:
        updated_shiftby = (shiftby%len(abc))
    else: updated_shiftby = (shiftby%len(abc))
    print(abc)
    print(updated_shiftby)

    if abc.find(char) + updated_shiftby > len(abc) - 1 and shiftby > 0:
        final_idx = (len(abc) - 1) - abc.find(char)
        print(abc[final_idx])
    elif abc.find(char) + updated_shiftby < 94 and shiftby > 0:
        final_idx = abc.find(char) + updated_shiftby
        print(abc[final_idx])

    # now for the negative shift cases
    if abc.find(char) - updated_shiftby < 0 and shiftby < 0:
        final_idx = -(updated_shiftby-abc.find(char))
        print(abc[final_idx])
    
def find_char():
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    char = '('
    print(abc.find(char))


if __name__ == "__main__":
    main()
    # find_char()