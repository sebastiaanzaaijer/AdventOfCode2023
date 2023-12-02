def solve_puzzle(puzzle_input:str):
    total = 0
    for line in puzzle_input.splitlines(keepends=False):
        first_digit = None
        second_digit = None
        for character in line:
            if character.isdigit() and first_digit is None:
                first_digit = character
            if character.isdigit() and not first_digit is None:
                second_digit = character
        total += int(first_digit+second_digit)
                
    return total

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))