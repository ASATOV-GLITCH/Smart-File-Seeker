# 🔍 Smart File Seeker (v1.0)

**Smart File Seeker** is a high-performance Python utility designed for developers who work with large-scale projects. It instantly locates files across your entire system and opens them directly in VS Code.

---

## 📖 What it does
In a cluttered development environment, finding a specific `main.py` or `config.cs` can be a headache. This tool:
1.  **Scans specified drives** (e.g., F:\ or C:\) for a target filename.
2.  **Lists all matches** with their full system paths if multiple files with the same name exist.
3.  **Launches the file** in Visual Studio Code instantly upon selection.

---

## ⚙️ How it works
The script utilizes the following logic:
* **Recursion:** Uses `os.walk` to traverse every directory in the search root.
* **User Interface:** Provides a simple Command Line Interface (CLI) for input and selection.
* **Process Management:** Uses the `subprocess` module to communicate with your OS and trigger VS Code commands.

---

## 🛠 Troubleshooting: "'code' is not recognized"

If you encounter the error:  
`'code' is not recognized as an internal or external command`  
it means the VS Code binary is not in your System Environment Variables (PATH).

### **How to fix via Environment Variables (Windows):**
1.  Click the **Start Menu** and search for **"Edit the system environment variables"**.
2.  In the System Properties window, click the **"Environment Variables..."** button.
3.  Under **"System variables"**, find the variable named **Path** and click **Edit**.
4.  Click **"New"** and add the path to your VS Code `bin` folder.  
    *Default path:* `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Microsoft VS Code\bin`
5.  Click **OK** on all windows.
6.  **Restart your Terminal or VS Code** to apply the changes.

---

## 🤝 Contributors

I am open to collaborations! If you have ideas for features like "partial name search" or "GUI integration," feel free to contribute.

* **Lead Developer:** [ASATOV-GLITCH](https://github.com/ASATOV-GLITCH)

---
*Created as part of the "Aether Trials" development workflow.*
