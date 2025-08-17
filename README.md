Simple Log Analyzer
===================

Overview:
---------
This project is a simple Python program that analyzes log files to search for suspicious activities or keywords indicating security or operational issues. It can be used to monitor system logs, application logs, or any other type of text-based log files.

Features:
---------
*   Reads and analyzes text log files.
*   Searches for specific keywords and patterns indicating suspicious activity.
*   Reports lines containing suspicious activities with line number and reason.
*   Easy to configure and modify to add new keywords or patterns.

Tools and Technologies Used:
----------------------------

1.  **Programming Language: Python**
    *   **Description:** Python is a high-level, general-purpose, and interpreted programming language. It was chosen for its ease of text processing, its ability to efficiently handle large files, and its rich libraries that support regular expressions.
    *   **Usage in Project:** Python was used to write the main program logic, including reading files line by line, applying regular expressions to search for patterns, and handling input and output.

2.  **Re Module (Built-in in Python):**
    *   **Description:** The `re` (Regular Expression) module provides support for working with regular expressions in Python. Regular expressions are sequences of characters that define a search pattern.
    *   **Usage in Project:** Used to search for suspicious keywords and patterns within each line of the log file. `re.search()` is used to find pattern matches, and `re.escape()` is used to ensure proper handling of keywords that may contain special characters in regular expressions.

3.  **Os Module (Built-in in Python):**
    *   **Description:** The `os` module provides a portable way of using operating system dependent functionality.
    *   **Usage in Project:** Used to check if the specified log file exists on the system (`os.path.exists()`) before attempting to read it, which prevents errors if the path is incorrect.

4.  **Sys Module (Built-in in Python):**
    *   **Description:** The `sys` module provides access to variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
    *   **Usage in Project:** Used to access command-line arguments (`sys.argv`) passed by the user to specify the log file path, and to exit the program (`sys.exit()`) in case of usage errors.

Requirements:
-------------
*   Python 3.x (Developed and tested on Python 3.x)

Installation:
-------------
No external libraries require installation other than those built into Python. However, it is always recommended to create a virtual environment:

1.  **Clone the Repository (if the project is on GitHub):**
    ```bash
    git clone https://github.com/kush-king249/log-analyzer.git
    cd log-analyzer
    ```

2.  **Create and Activate a Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies (if there are any future dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

Usage:
------
To run the program, use the following command in the command line:

```bash
python log_analyzer.py <LOG_FILE_PATH>
```

**Examples:**

*   Check authentication logs on a Linux system:
    ```bash
    python log_analyzer.py /var/log/auth.log
    ```

*   Check Apache logs on a Linux system:
    ```bash
    python log_analyzer.py /var/log/apache2/error.log
    ```

Contributing:
-------------
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

License:
--------
This project is licensed under the MIT License. See the `LICENSE` file (if present) for more details.

Author:
-------
Hassan Mohamed Hassan Ahmed

MIT License

Copyright (c) 2025 Hassan Mohamed Hassan Ahmed
