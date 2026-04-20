# BulkMailer Pro

A professional Windows desktop application for sending bulk HTML emails via Gmail (SMTP or OAuth2).

---

## ✨ Features

- **Two sending modes**: Personalized (Name + Email) or Bulk (email-only)
- **Rich HTML editor** with live split-pane preview
- **Template library**: 3 built-in professional templates
- **Dynamic variables**: `{{name}}` auto-replaced per recipient
- **Gmail SMTP** (App Password) or **OAuth2** authentication
- **Progress bar** + real-time activity log
- **Start/Stop** controls
- **Adjustable delay** between emails (2–5s default)
- **Export log** to CSV or TXT
- **Email validation** before sending
- Secure credential storage (no plaintext passwords)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or newer
- Windows 10/11 (or macOS/Linux for development)

### 1. Clone / Download

```
git clone https://github.com/yourname/bulkmailer-pro
cd bulkmailer-pro
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python main.py
```

---

## 🔐 Authentication Setup

### Option A: Gmail SMTP (Easier)

1. Enable **2-Step Verification** on your Google Account
2. Go to **Google Account → Security → App Passwords**
3. Create an App Password for "Mail" + "Windows Computer"
4. Copy the 16-character password
5. In BulkMailer Pro → SMTP tab → enter your email + App Password

### Option B: Gmail OAuth2 (Recommended for production)

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project → Enable **Gmail API**
3. Create **OAuth 2.0 credentials** (Desktop App type)
4. Download `credentials.json`
5. In BulkMailer Pro → OAuth2 tab → Browse to `credentials.json`
6. Click **Sign In with Google OAuth2** → browser will open for authorization
7. Tokens are saved to `~/.bulkmailer/token.json`

---

## 📊 Excel/CSV Format

### Personalized Mode
```
| Name          | Email                  |
|---------------|------------------------|
| Alice Johnson | alice@example.com      |
| Bob Smith     | bob@example.com        |
```

### Bulk Mode
```
| user1@example.com |
| user2@example.com |
| user3@example.com |
```

Run `python create_samples.py` to generate sample files.

---

## 🎨 HTML Variables

Use `{{name}}` in both subject and HTML body:

```html
<h1>Hello {{name}},</h1>
<p>Thank you for your order!</p>
```

The subject also supports variables:
```
Welcome {{name}}! Your account is ready.
```

---

## 📦 Building the .exe (Windows)

### Method 1: Run the build script

```
build.bat
```

### Method 2: Manual PyInstaller

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller bulkmailer.spec --clean

# Output at:
# dist/BulkMailerPro/BulkMailerPro.exe
```

The `dist/BulkMailerPro/` folder is the distributable — zip it up and share.

> **Note**: Build on Windows for best results. PyInstaller creates platform-specific executables.

---

## 📁 Project Structure

```
bulk_mailer/
├── main.py                   # Entry point
├── requirements.txt          # Dependencies
├── bulkmailer.spec           # PyInstaller config
├── build.bat                 # Windows build script
├── create_samples.py         # Generate sample Excel files
├── core/
│   ├── email_sender.py       # SMTP + OAuth2 + SendWorker
│   ├── file_reader.py        # Excel/CSV parsing
│   └── storage.py            # Credential storage
└── ui/
    ├── app.py                # Main window
    ├── styles.py             # Dark theme stylesheet
    ├── login_page.py         # Auth page (SMTP / OAuth2)
    ├── dashboard.py          # Main sending interface
    └── html_editor.py        # HTML editor + preview
```

---

## 🔒 Security Notes

- SMTP App Passwords are stored with basic encoding (not encryption) in `~/.bulkmailer/config.json`
- OAuth2 tokens are stored in `~/.bulkmailer/token.json` — same security level as Chrome storing tokens
- For production deployments, consider adding OS keychain integration via `keyring` library
- Never share your `credentials.json` or `token.json` publicly

---

## ⚠️ Gmail Sending Limits

| Account Type | Daily Limit |
|---|---|
| Free Gmail | ~500/day |
| Google Workspace | ~2,000/day |

Tips to avoid blocks:
- Use the delay setting (2–5s recommended)
- Keep bounce rates low
- Warm up new sending accounts gradually
- Consider Google Workspace for higher volume

---

## 🐛 Troubleshooting

**"Authentication failed" on SMTP**
→ Check that 2FA is enabled and you're using an App Password (not your Gmail password)

**OAuth2 browser doesn't open**
→ Install: `pip install google-api-python-client google-auth-oauthlib`

**"No module named PyQt5"**
→ Run: `pip install PyQt5 PyQtWebEngine`

**Preview panel is blank**
→ Install: `pip install PyQtWebEngine`

**Build fails on macOS/Linux**
→ PyInstaller works but `.exe` is Windows-only; use the same spec to get a native binary for your OS

---

## 📄 License

MIT License — free for personal and commercial use.

## Some app interface images

<img width="1251" height="802" alt="image" src="https://github.com/user-attachments/assets/b6d5ffda-1e40-4e3c-96e1-6d8e1396ae57" />


<img width="1265" height="820" alt="image" src="https://github.com/user-attachments/assets/51616a1b-b640-43ad-bef2-f087ea4faed5" />

<img width="891" height="665" alt="image" src="https://github.com/user-attachments/assets/8139c86d-1c2c-412c-b5f6-ae67fbf18a58" />
