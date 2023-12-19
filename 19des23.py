def is_white_square(file, rank):
    """
    Check if the given chess position corresponds to a white square on the chessboard.
    """
    file_index = ord(file) - ord('a')  # Convert file to index (0-7)
    return (file_index + rank) % 2 == 0

def read_chess_position():
    while True:
        try:
            position = input("Masukan koordinat papan catur: ").strip().lower()

            # Check if the input is a valid chess position
            if len(position) != 2 or not position[0].isalpha() or not position[1].isdigit():
                raise ValueError("Input tidak valid")

            file, rank = position[0], int(position[1])

            # Check if the file is a valid chess file (a-h)
            if file not in 'abcdefgh':
                raise ValueError("Invalid file. Please enter a valid chess position.")

            # Check if the rank is a valid chess rank (1-8)
            if rank < 1 or rank > 8:
                raise ValueError("Invalid rank. Please enter a valid chess position.")

            return file, rank
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    file, rank = read_chess_position()
    square_color = "white" if is_white_square(file, rank) else "black"
    print(f"The position {file}{rank} is on a {square_color} square.")
