# 🦷 NY Dentist Lead Extractor (Automated NPI Scraper)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Production--Ready-green?style=for-the-badge)

A high-performance automated scraping solution designed to extract verified contact information for dental professionals in the New York area. This tool bridges the gap between raw government data and actionable business leads.

---

## 🚀 Key Value Proposition
This isn't just a simple script; it's a **Lead Generation Engine**. It communicates directly with the official **US NPI Registry API** to ensure 100% data integrity, bypassing the inaccuracies of manual data entry.

### 🌟 Features
* **Real-Time API Sync:** Pulls the most current records directly from federal databases.
* **Smart Name Logic:** Automatically detects and formats individual practitioners or organizational clinics.
* **Lead-Ready Formatting:** Outputs data in high-quality Excel (`.xlsx`) format with cleaned phone numbers and standardized addresses.
* **Error-Resilient:** Built-in timeout handling and connection retry logic.

---

## 🛠️ Technical Stack
* **Core:** Python 3.x
* **Data Processing:** Pandas (for structured DataFrames)
* **Networking:** Requests (with custom User-Agent headers)
* **Output Engine:** Openpyxl (Excel integration)

---

## 📊 Sample Result Preview
| Contractor Name | Full Address | Phone Number |
| :--- | :--- | :--- |
| **MODERN DENTAL NYC** | 123 Broadway, NEW YORK, NY 10001 | 2125550199 |
| **DR. SARAH SMITH** | 789 Park Ave, NEW YORK, NY 10022 | 7185550234 |

---

## ⚙️ Installation & Usage

1. **Clone the project:**
   ```bash
   git clone [https://github.com/yourusername/ny-dentist-scraper.git](https://github.com/yourusername/ny-dentist-scraper.git)
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the Extraction:**
   ```bash
   python ny_dentist_scraper.py
