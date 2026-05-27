import pdfplumber
import os

def convert_pdf_to_markdown(pdf_path, output_md_path):
    print(f"Starting conversion: {pdf_path}...")
    
    # Check if the PDF actually exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file {pdf_path} was not found.")
        return

    markdown_content = []

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Loop through every page by its page number
        for index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            
            if text:
                # Add a clean Markdown header to separate pages visually
                markdown_content.append(f"\n<!-- Page {index} -->\n")
                markdown_content.append(text)
            else:
                # If extract_text() returns None, the page is likely a scanned image
                markdown_content.append(f"\n<!-- Page {index}: [No text found / Scanned Image] -->\n")

    # Combine all the collected pages into one massive string
    full_text = "\n".join(markdown_content)

    # Write the string out to a Markdown file
    with open(output_md_path, "w", encoding="utf-8") as md_file:
        md_file.write(full_text)
        
    print(f"Success! Saved Markdown to: {output_md_path}")

# --- How to run it ---
# Replace these paths with your actual filenames
pdf_input = "[Input file.pdf]"
markdown_output = "[output file.md]"

convert_pdf_to_markdown(pdf_input, markdown_output)