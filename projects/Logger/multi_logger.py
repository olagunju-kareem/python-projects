# multi_logger.py - A simple logging utility for recording messages in Termux and Windows.

import datetime
import platform

def main():
    message = input('Input log message: ')
    if message:
        # Detect OS
        os_name = platform.system()
        # 'Linux' for Termux, 'Windows' for Windows OS
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('log_file.txt', 'a', encoding='utf-8') as log_file:
            commit = f"[{timestamp}] [{os_name}] {message}\n"
            log_file.write(commit)
        print('Log entry added successfully.')
    else:
        print('No message provided. Log entry not added.')

if __name__ == '__main__':
    main()