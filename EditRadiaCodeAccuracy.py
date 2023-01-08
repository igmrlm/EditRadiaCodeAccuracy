import csv
import sys

def remove_lines_with_high_accuracy(input_file, output_file, threshold):
    # Open the input file and output file
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        # Create a CSV reader and writer using a tab delimiter
        reader = csv.reader(in_file, delimiter='\t')
        writer = csv.writer(out_file, delimiter='\t')

        # Read and preserve the custom line at the beginning of the file
        custom_line = next(reader)
        writer.writerow(custom_line)

        # Write the header row
        writer.writerow(next(reader))

        # Initialize variables to store the accuracy values
        accuracies = []

        # Iterate over the rows in the input file
        for row in reader:
            # Check if the accuracy is above the threshold
            if float(row[4]) <= threshold:
                # If the accuracy is below the threshold, add it to the list and write the row to the output file
                accuracy = float(row[4])
                accuracies.append(accuracy)
                writer.writerow(row)

        # Calculate the average, minimum, and maximum accuracy
        avg_accuracy = sum(accuracies) / len(accuracies)
        min_accuracy = min(accuracies)
        max_accuracy = max(accuracies)

        # Print the results
        print(f'Average accuracy in output file: {avg_accuracy:.2f}')
        print(f'Minimum accuracy in output file: {min_accuracy:.2f}')
        print(f'Maximum accuracy in output file: {max_accuracy:.2f}')

# Get the input and output file paths and the accuracy threshold from the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
threshold = float(sys.argv[3])

# Call the function
remove_lines_with_high_accuracy(input_file, output_file, threshold)

# Calculate the average, minimum, and maximum accuracy in the input file
accuracies = []
with open(input_file, 'r') as in_file:
    # Create a CSV reader using a tab delimiter
    reader = csv.reader(in_file, delimiter='\t')

    # Read and ignore the custom line at the beginning of the file
    next(reader)

    # Read and ignore the header row
    next(reader)

    # Iterate over the rows in the input file
    for row in reader:
        # Add the accuracy to the list
        accuracy = float(row[4])
        accuracies.append(accuracy)

# Calculate the average, minimum, and maximum accuracy
avg_accuracy = sum(accuracies) / len(accuracies)
min_accuracy = min(accuracies)
max_accuracy = max(accuracies)

# Print the results
print(f'Average accuracy in input file: {avg_accuracy:.2f}')
print(f'Minimum accuracy in input file: {min_accuracy:.2f}')
print(f'Maximum accuracy in input file: {max_accuracy:.2f}')
