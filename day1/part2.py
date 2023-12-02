digit_map = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}

def find_first_digit(string:str):
    lowest_position = len(string)
    first_digit = ""
    for digit in digit_map:
        position = string.find(digit)
        if position == 0: return digit_map[digit] # return early if "digit" appears at the start
        if position >=0 and position < lowest_position:
            lowest_position = position
            first_digit = digit
    return digit_map[first_digit]
            
def find_last_digit(string:str):
    highest_position = -1
    last_digit = ""
    for digit in digit_map:
        position = string.rfind(digit)
        if position >= 0:
            if position == len(string) - len(digit): return digit_map[digit] # return early if "digit" appears at the end
            if position > highest_position:
                highest_position = position
                last_digit = digit
    return digit_map[last_digit]


def solve_puzzle(puzzle_input:str):
    total = 0
    for line in puzzle_input.splitlines(keepends=False):
        total += 10*find_first_digit(line)+find_last_digit(line)
                
    return total

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))