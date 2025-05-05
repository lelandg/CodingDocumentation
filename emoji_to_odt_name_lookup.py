import requests
import pandas as pd
from odf.opendocument import OpenDocumentText
from odf.text import P, H
from odf.table import Table, TableRow, TableCell
from odf.style import Style, TextProperties, TableCellProperties

EMOJI_TEST_URL = "https://unicode.org/Public/emoji/15.0/emoji-test.txt"

def fetch_data(url):
    return requests.get(url).text.splitlines()

def parse_emojis(lines):
    emojis = []
    group = ""
    for line in lines:
        if line.startswith("# group:"):
            group = line.split(":")[1].strip()
        elif line and not line.startswith("#"):
            code, desc = line.split("#")
            codepoints = code.split(";")[0].strip()
            emoji_char, *name = desc.strip().split()
            name = ' '.join(name)
            hex_code = " ".join([f"U+{cp}" for cp in codepoints.split()])
            dec_value = int(codepoints.replace(" ", "0x"), 16) if len(codepoints.split()) == 1 else None
            win_input = f"Alt+{dec_value}" if dec_value and dec_value <= 255 else f"Type {codepoints.replace(' ', '')}, then Alt+X"
            html_entity = " ".join([f"&#x{cp};" for cp in codepoints.split()])
            emojis.append({
                "Group": group,
                "Emoji": emoji_char,
                "Name": name,
                "Code Point": hex_code,
                "Windows Input": win_input,
                "HTML Entity": html_entity,
                "macOS Input": "⌃⌘Space → type name and select"
            })
    return pd.DataFrame(emojis)

df = parse_emojis(fetch_data(EMOJI_TEST_URL))

# Create ODT
doc = OpenDocumentText()

h1style = Style(name="H1", family="paragraph")
h1style.addElement(TextProperties(fontsize="20pt", fontweight="bold"))
doc.styles.addElement(h1style)

h2style = Style(name="H2", family="paragraph")
h2style.addElement(TextProperties(fontsize="17pt", fontweight="bold"))
doc.styles.addElement(h2style)

cellstyle = Style(name="Cell", family="table-cell")
cellstyle.addElement(TableCellProperties(border="0.74pt solid #000"))
doc.styles.addElement(cellstyle)

doc.text.addElement(H(outlinelevel=1, stylename=h1style, text="Emoji Alt Key Combinations (with Names)"))

for group_name, group_df in df.groupby("Group"):
    doc.text.addElement(H(outlinelevel=2, stylename=h2style, text=group_name))
    tbl = Table()
    header = TableRow()
    for col in group_df.columns:
        cell = TableCell(stylename=cellstyle)
        cell.addElement(P(text=col))
        header.addElement(cell)
    tbl.addElement(header)

    for _, row in group_df.iterrows():
        tr = TableRow()
        for col in group_df.columns:
            cell = TableCell(stylename=cellstyle)
            cell.addElement(P(text=row[col]))
            tr.addElement(cell)
        tbl.addElement(tr)

    doc.text.addElement(tbl)

doc.save("emojis_with_names.odt")
print("Saved emojis_with_names.odt")
