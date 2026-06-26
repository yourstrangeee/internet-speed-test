# 🚀 Internet Speed Test

A simple Python application that measures your internet connection's **download speed**, **upload speed**, and **ping** using the `speedtest-cli` library.

## ✨ Features

* 🔍 Automatically finds the best Speedtest server.
* ⬇️ Tests download speed.
* ⬆️ Tests upload speed.
* 📶 Displays ping (latency).
* 🌍 Displays server information:

  * Server Name
  * Country
  * Sponsor
  * Server ID
* ⏱️ Shows the total time taken to complete the test.
* 📊 Clean and easy-to-read terminal output.

## 📦 Requirements

* Python 3.8 or later
* `speedtest-cli`

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/internet-speed-test.git
```

Navigate to the project directory:

```bash
cd internet-speed-test
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the script:

```bash
python speed.py
```

## 📁 Project Structure

```text
internet-speed-test/
│
├── speed.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 📄 requirements.txt

```text
speedtest-cli
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

## 📄 License

This project is licensed under the MIT License.
