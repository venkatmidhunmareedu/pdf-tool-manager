# PDF Tool Manager (ptm)

  

PDF Tool Manager (ptm) is a versatile command-line tool for managing and manipulating PDF files. It provides a range of functionalities for merging, splitting, compressing, converting, encrypting, unlocking, and redacting PDF documents.

  

## Features

  

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

  

4. **PDF to Images**

   - **Description:** Convert each page of a PDF file into images and package them into a zip file.

   - **Flags:**

     - `-i`: Input file

     - `-o`: Output zip file path

   - **Example:**

   ```bash

     ptm pdf2images -i input.pdf -o output.zip

   ```

  

5. **Images to PDF**

   - **Description:** Convert images from a folder into a single PDF file.

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

  

## Downloads


Check the releases page to download the latest version of ptm(Only Windows version and linux version available).


## Want to Develop?  

  
Clone the repository and follow the instructions for setup:

  

```bash

git clone https://github.com/venkatmidhunmareedu/pdf-tool-manager.git

cd pdf-tool-manager

# create a virtual environment

python -m venv env_name

pip install -r requirements.txt

# build commands

pyinstaller --onefile --noconsole main.py

# this will create a .exe file under the dist folder

# use cmd to run the .exe file using the instruction above

```

  

## Todo

  

- Complete the remaining features

- More features are welcome. If you have any suggestions, please let me know via [GitHub issues](https://github.com/venkatmidhunmareedu/pdf-tool-manager/issues).

- Add more functionalities.

- Complete the docs and add more details.

- Reduce the complexity of the code.

  
  

## Contributing

  

Feel free to submit issues or pull requests to improve PDF Tool Manager.

  

## License

  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

  

---