import camelot
import csv
import os

# Path to your PDF file
file_path = 'input.pdf'

directory_path = 'input'

# Read tables from the PDF
# tables = camelot.read_pdf(file_path, pages='all', flavor='lattice')

# Path to your output CSV file
csv_file_path = 'output_3.csv'

# Function to handle multiline cells with alternate line breaks
# Function to handle multiline cells and skip all odd '\n' characters
def split_multiline_rows(rows):
    new_rows = []
    for row in rows:
        # Check if the first column contains multiline text
        if '\n' in row[0]:
            # Split the cell into lines
            lines = row[0].split('\n')
            # Combine every two lines
            combined_lines = [' '.join(lines[i:i+2]) for i in range(0, len(lines), 2)]
            # Create new rows for combined lines
            for combined_line in combined_lines:
                new_row = [combined_line] + row[1:]
                new_rows.append(new_row)
        else:
            new_rows.append(row)
    return new_rows

def process_first_column(first_col):
    lines = first_col.split('\n')
    combined_lines = [' '.join(lines[i:i+2]) for i in range(0, len(lines), 2)]
    return combined_lines

# Function to handle multiline cells in all columns
def split_multiline_rows_b(rows):
    new_rows = []
    for row in rows:
        # Process the first column
        first_col_processed = process_first_column(row[0])
        # Split remaining columns on every '\n'
        remaining_cols = [col.split('\n') for col in row[1:]]
        # Find the maximum number of parts in any column
        max_splits = max(len(first_col_processed), *[len(col) for col in remaining_cols])
        # Ensure each column has the same number of parts
        while len(first_col_processed) < max_splits:
            first_col_processed.append('')
        for col in remaining_cols:
            while len(col) < max_splits:
                col.append('')
        # Combine corresponding parts from each column
        for i in range(max_splits):
            new_row = [first_col_processed[i]] + [col[i] for col in remaining_cols]
            new_rows.append(new_row)
    return new_rows

# Write tables to CSV
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for table in tables:
#         split_rows = split_multiline_rows_b(table.data)
#         for row in split_rows:
#             writer.writerow(row)

with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            tables = camelot.read_pdf(file_path, pages='all', flavor='lattice')
            for table in tables:
                split_rows = split_multiline_rows_b(table.data)
                for row in split_rows:
                    writer.writerow(row)

print("CSV file has been created.")