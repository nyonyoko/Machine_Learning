def detect_delimiter(filename):
    with open(filename, 'r') as file:
        # Read the first line of the file
        first_line = file.readline()
        # Count occurrences of common delimiters
        delimiters = [',', '\t', ';', '|', ':', ' ']
        delimiter_counts = {delimiter: first_line.count(delimiter) for delimiter in delimiters}
        # Find the delimiter with the highest count
        detected_delimiter = max(delimiter_counts, key=delimiter_counts.get)
    return detected_delimiter

# Detect the delimiter of a CSV file
filename = '/Users/leoyaoair23/MacAirLeoYao/Spring 2024/fml/project/regression/dataSet/movieTitles.csv'
detected_delimiter = detect_delimiter(filename)
print("Detected delimiter:", detected_delimiter)
