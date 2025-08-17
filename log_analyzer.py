
import re
import os
import sys

def analyze_log(log_file_path):
    """
    Reads the specified log file and analyzes its content to search for suspicious activities based on defined keywords.

    Args:
        log_file_path (str): The full path to the log file to be analyzed.

    Returns:
        list: A list of detected suspicious activities. Each activity is a dictionary containing:
              - 'line_num': The line number where the suspicious activity was found.
              - 'line_content': The full content of the line.
              - 'reason': The reason why this line was considered suspicious (the detected keyword).
    """
    suspicious_activities = []

    # List of keywords or patterns that indicate suspicious activity.
    # This list is expandable and modifiable to suit different log types and detection needs.
    suspicious_keywords = [
        "failed password",      # Failed login attempts
        "authentication failure", # Authentication failure
        "access denied",        # Access denied
        "error",                # General errors (may indicate problems or attacks)
        "denied",               # Denied (general)
        "attack",               # General keyword for attacks
        "malware",              # Malware
        "injection",            # Injection attempts (e.g., SQL Injection)
        "scan",                 # Scan operations (e.g., port scanning)
        "probe"                 # Exploration or probing
    ]

    # Check if the log file exists
    if not os.path.exists(log_file_path):
        print(f"[!] Error: Log file not found at {log_file_path}")
        return suspicious_activities

    print(f"[*] Analyzing log file: {log_file_path}")
    # Open the log file for reading
    # encoding="utf-8" to handle different characters, errors="ignore" to avoid stopping on encoding errors
    with open(log_file_path, "r", encoding="utf-8", errors="ignore") as f:
        # Iterate over each line in the file, tracking the line number
        for line_num, line in enumerate(f, 1):
            line = line.strip() # Remove whitespace from the beginning and end of the line
            if not line: # Skip empty lines
                continue

            # Search for suspicious keywords in each line
            for keyword in suspicious_keywords:
                # re.search to search for the pattern, re.escape to treat keywords as literal characters
                # re.IGNORECASE to ignore case (upper/lower)
                # \b to ensure full word match (word boundaries)
                if re.search(r'\b' + re.escape(keyword) + r'\b', line, re.IGNORECASE):
                    suspicious_activities.append({
                        "line_num": line_num,
                        "line_content": line,
                        "reason": f"Contains suspicious keyword: ‘{keyword}’"
                    })
                    # Once a keyword is found in the line, move to the next line to avoid duplication
                    break

            # Examples of more complex patterns can be added here later
            # Example: Detecting repeated failed login attempts from the same IP
            # match = re.search(r'Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
            # if match:
            #     ip_address = match.group(1)
            #     # Here, you can track the number of failed attempts for each IP and generate an alert if it exceeds a certain limit

    return suspicious_activities

def main():
    """
    The main function of the program.
    Processes command-line arguments and runs the log analysis process.
    """
    # Check the number of command-line arguments.
    # There should be one argument after the script name, which is the log file path.
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <LOG_FILE_PATH>")
        print("Example: python log_analyzer.py /var/log/auth.log")
        sys.exit(1) # Exit the program with an error code if arguments are insufficient

    log_file = sys.argv[1] # Get the log file path from command-line arguments
    results = analyze_log(log_file) # Call the log analysis function

    # Print the results
    if results:
        print("\n[!!!] Suspicious Activities Found:")
        for activity in results:
            print(f"  Line {activity['line_num']}: {activity['line_content']}")
            print(f"    Reason: {activity['reason']}")
            print("-" * 30)
    else:
        print("\n[*] No suspicious activities found in the log file.")

# This condition ensures that the main() function will only run when the script is executed directly
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()



