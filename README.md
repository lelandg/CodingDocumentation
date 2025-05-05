# Coding Documentation

A documentation site for programmers, written in part by AI, to help developers learn and improve their coding skills.
Topics include AI, coding best practices, and step-by-step tutorials.

## CSV to Document Converter

This repository now includes a Streamlit application that allows you to upload a CSV file and convert it to different document formats (CSV, HTML, DOCX). The application provides options to create tables based on column values, sort and filter data, and more.

### Features

- **CSV Upload**: Upload any CSV file for processing
- **Data Preview**: View a preview of your data before conversion
- **Grouping**: Group data by any column to create separate tables for each unique value
- **Multiple Export Formats**: Download your document as CSV, HTML, or DOCX
- **Sorting**: Sort data by any column in ascending or descending order
- **Filtering**: Filter data to include only specific values from a column
- **Custom Document Title**: Set a custom title for your document

### Running the Application

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

3. Open your web browser and navigate to the URL displayed in the terminal (usually http://localhost:8501)

## Documentation Site Overview

This repository also contains a GitHub Pages site designed to provide coding documentation and resources for programmers. The site includes:

- Getting Started guides
- API Reference documentation
- Best Practices for coding
- Step-by-step Tutorials

## Purpose

This documentation site serves as a resource for developers looking to improve their coding skills and follow industry best practices. The content is designed to be clear, concise, and practical.

## Technologies Used

For the documentation site:
- HTML5
- CSS3
- GitHub Pages for hosting

For the CSV to Document Converter:
- Python 3.7+
- Streamlit - Web application framework
- Pandas - Data manipulation and analysis
- python-docx - Creating and manipulating DOCX files

## Local Development

### Documentation Site

To run the documentation site locally:

1. Clone the repository
2. Open `index.html` in your browser

No build process is required as this is a static site.

### CSV to Document Converter

To run the Streamlit application locally:

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
4. The application will open in your default web browser, or you can access it at http://localhost:8501

## Contributing

Contributions to improve the documentation are welcome. Please feel free to submit pull requests with improvements or additions.

## License

This project is available under the MIT License.
