import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    for column in df.columns:
        if pd.api.types.is_string_dtype(df[column]):
            df[column] = df[column].str.strip().str.title()

    df = df.drop_duplicates()
    df = df.dropna()
    df.to_csv(output_file, index=False)
    return df


while True:
    filename = input("Enter the name of the CSV file to clean: ")

    try:
        result = clean_csv(filename, "cleaned_" + filename)
        print(result)
        print(f"Saved as cleaned_{filename}")
    except FileNotFoundError:
        print("That file was not found. Please check the filename and try again.")

    continue_cleaning = input("Do you want to clean another file? (yes/no): ").strip().lower()
    if continue_cleaning != 'yes':
        break

    