# Multi-Device Activity Logger
A lightweight Python utility designed to maintain a unified activity log across different hardware environments. This tool allows for consistent tracking of progress and thoughts while switching between mobile (Android/Termux/Pydroid) and desktop (Windows/VS Code) development sessions.

## 🚀 Features
- **Automated Device Detection:** Identifies the host operating system (Windows vs. Linux/Android) using the platform module to tag the source of each entry.
- **Persistent Appending:** Uses file append mode to ensure new logs are added to the end of the ledger without risk of overwriting existing data.
- **Temporal Context:** Every entry is automatically prefixed with a precise timestamp using the datetime library.
- **Cross-Platform Compatibility:** Uses UTF-8 encoding to ensure text remains consistent when synced between different file systems.
- **Resource Management:** Implements Python's with context manager for safe and reliable file I/O.

## 📋 Technical Overview
The script captures three data points for every entry:
1. **Timestamp:** `YYYY-MM-DD HH:MM:SS`
2. **Platform:** Detected OS (e.g., Windows, Linux)
3. Message: User-defined text input.

### Example Output
`[2025-12-31 13:45:02] [Windows] Completed Git branch configuration.`

`[2025-12-31 15:10:12] [Linux] Testing logger via Termux on Infinix.`

## 🛠️ Usage
1. Run the script:
```bash
python multi_logger.py
```
2. Enter your update when prompted.
3. The entry is saved to log_file.txt in the same directory.

## 🛡️ Privacy Tip
To keep your personal logs off public repositories, add the log filename to your `.gitignore`:

```gitignore
# .gitignore
log_file.txt
```


*A simple utility for tracking the developer's journey across devices.*