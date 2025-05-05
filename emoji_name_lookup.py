import pandas as pd
import requests

EMOJI_TEST_URL = "https://unicode.org/Public/emoji/15.0/emoji-test.txt"
CSV_PATH = "emojis.csv"

def fetch_emoji_names(url):
    lines = requests.get(url).text.splitlines()
    emoji_dict = {}
    line_number = 0
    for line in lines:
        line_number += 1
        if line and not line.startswith("#"):
            parts = line.split("#", 1)
            if len(parts) < 2:
                print(f"Skipping line due to unexpected format at line {line_number}: {line}")
                continue

            codepoints_part = parts[0].strip()
            description_part = parts[1].strip()

            # Extract the emoji character and name from description part
            description_tokens = description_part.split()
            if not description_tokens:
                print(f"Skipping line due to empty description at line {line_number}: {line}")
                continue

            emoji_char = description_tokens[0]
            name = ' '.join(description_tokens[1:])
            if emoji_char and name:
                emoji_dict[emoji_char] = name
            else:
                print(f"Skipping line due to incomplete emoji or name at line {line_number}: {line}")

    return emoji_dict

def main():
    try:
        df = pd.read_csv(CSV_PATH, dtype=str)
    except FileNotFoundError:
        print(f"File '{CSV_PATH}' not found. Please make sure it exists.")
        return
    except Exception as e:
        print(f"Error reading '{CSV_PATH}': {e}")
        return

    # Normalize columns: strip spaces and lowercase for flexible matching
    normalized_columns = [col.strip() for col in df.columns]

    if 'Emoji' not in df.columns:
        # Try case-insensitive and stripped matching
        if any(col.strip().lower() == 'emoji' for col in df.columns):
            # Find the exact original column name
            emoji_col = next(col for col in df.columns if col.strip().lower() == 'emoji')
            print(f"Using column '{emoji_col}' as 'Emoji' column (detected by case-insensitive match).")
        else:
            print(f"The CSV file must contain an 'Emoji' column. Columns found: {list(df.columns)}. Please fix the CSV file.")
            return
    else:
        emoji_col = 'Emoji'

    if 'Name' not in df.columns:
        emoji_names = fetch_emoji_names(EMOJI_TEST_URL)
        insert_pos = df.columns.get_loc(emoji_col) + 1
        df.insert(insert_pos, 'Name', df[emoji_col].map(emoji_names).fillna(''))
        df.to_csv(CSV_PATH, index=False, quoting=1, encoding='utf-8')
        print(f"Updated '{CSV_PATH}' with a new 'Name' column.")
    else:
        print(f"'{CSV_PATH}' already has a 'Name' column. No changes made.")

if __name__ == "__main__":
    main()