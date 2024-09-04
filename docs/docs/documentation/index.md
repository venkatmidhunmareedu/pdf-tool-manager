## Usage Guide

1. **Merge**
   - **Description:** Merge multiple PDF files into a single document.
   - **Flags:**
     - `-i`: Input file paths (multiple allowed)
     - `-o`: Output file path
   - **Example:**
     ```bash
     ptm merge -i input1.pdf -i input2.pdf -o output.pdf
     ```

2. **Splitoe**
   - **Description:** Split a PDF file into separate files for odd and even pages, and package them into a zip file.
   - **Flags:**
     - `-i`: Input file
     - `-o`: Output zip file path
   - **Example:**
     ```bash
     ptm splitoe -i input.pdf -o output.zip
     ```

3. **Compress**
   - **Description:** Compress a PDF file to reduce its size while optimizing the quality.
   - **Flags:**
     - `-i`: Input file
     - `-o`: Output PDF file path
   - **Example:**
     ```bash
     ptm compress -i input.pdf -o output.pdf
     ```

4. **PDF to Images (Development in progress)**
   - **Description:** Convert each page of a PDF file into images and package them into a zip file.
   - **Flags:**
     - `-i`: Input file
     - `-o`: Output zip file path
   - **Example:**
     ```bash
     ptm pdf2images -i input.pdf -o output.zip
     ```

5. **Images to PDF (Development in progress)**
   - **Description:** Convert images from a folder into a single PDF file.(Development in progress)
   - **Flags:**
     - `-i`: Input folder path
     - `-o`: Output PDF file path
   - **Example:**
     ```bash
     ptm images2pdf -i input -o output.pdf
     ```

6. **Encrypt PDF**
   - **Description:** Encrypt a PDF file with a password.
   - **Flags:**
     - `-i`: Input file
     - `-p`: Password
     - `-o`: Output PDF file path
   - **Example:**
     ```bash
     ptm encryptpdf -i input.pdf -p password -o output.pdf
     ```

