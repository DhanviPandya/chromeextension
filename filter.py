def delete_lines_with_words(input_file_path, words_to_delete, output_file_path):
    # Open the input file in read mode and read all lines
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    # Create a list to hold the lines that do not contain any of the words in words_to_delete
    filtered_lines = []
    
    # Loop through each line in the file
    for line in lines:
        # Check if any of the words to delete are in the current line
        if not any(word in line for word in words_to_delete):
            filtered_lines.append(line)  # If not, keep the line

    # Write the filtered lines to a new output file
    with open(output_file_path, 'w') as file:
        file.writelines(filtered_lines)
    
    print(f"Lines containing the specified words have been deleted and saved to {output_file_path}")

# Example usage

def main():
    input_file_path = 'comments.txt'  # Replace with your input file's path
    output_file_path = 'nicecomments.txt'  # Replace with your desired output file path
    words_to_delete = ['hate', 'stupid', 'ugly','fake','ashamed','bad','suck','embarrassing','cringey','overrated','terrible', ' mess','tacky', 'give up','waste','awful','joke, right' ]  # List of words you want to filter out
    delete_lines_with_words(input_file_path, words_to_delete, output_file_path)

if __name__ == "__main__":
    main()