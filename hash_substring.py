# python3
B = 13 # random number
Q = 256 # number of charackters in input alphabet

def read_input():
    i = input() # file or simple input
    if "i" in i.lower() :
        return (input().rstrip(), input().rstrip())

    elif "f" in i.lower() :
        name = "./tests/06"
        if "a" not in name:
            with open(name, mode = 'r' ,  encoding = "utf8") as fail:
                return (fail.readline().rstrip(), fail.readline().rstrip())
        else :
            return
                
    else :
        return
# make hash
def get_hash(pattern) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B*result + ord(pattern[i])) % Q # ord - return num of character (as ASCII)
    return result

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
    

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    output = []
    global B, Q
    pattern_len = len(pattern)
    main_text_len = len(text)
    pattern_hash = get_hash(pattern)

    for i in range (0, main_text_len - pattern_len + 1):
        main_text_hash = get_hash(text[i: i + pattern_len])
        if pattern_hash == main_text_hash:
            if pattern == text[i: i + pattern_len]:
                output.append(i)
    # and return an iterable variable
   
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

