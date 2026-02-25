# 🛡 Web Technology Detector

A cybersecurity-focused web application that detects technologies used by any website and identifies potential security vulnerabilities with actionable recommendations.

---

## 🚀 Quick Start

### 1. Clone / extract the project
```bash
cd web-tech-detector
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
python run.py
```

### 5. Open your browser
Navigate to **http://localhost:5000**

---

## 📁 Project Structure

```
web-tech-detector/
├── run.py                        # Entry point
├── requirements.txt
├── README.md
│
├── backend/
│   ├── app.py                    # Flask API + route handlers
│   ├── modules/
│   │   ├── discovery.py          # Tech fingerprinting, SSL, headers, ports
│   │   └── security.py           # Vulnerability detection & recommendations
│   └── utils/
│       ├── validators.py         # URL validation
│       └── pdf_report.py         # ReportLab PDF generation
│
├── database/
│   └── db.py                     # SQLite ORM helpers
│
└── frontend/
    └── templates/
        └── index.html            # Single-page cybersecurity UI
```

---

## 🔌 API Endpoints

| Method | Endpoint          | Description                        |
|--------|-------------------|------------------------------------|
| POST   | `/scan`           | Run a full scan on a URL           |
| GET    | `/history`        | List all past scans                |
| GET    | `/scan/<id>`      | Get full JSON data for a scan      |
| GET    | `/report/<id>`    | Download PDF report for a scan     |

### Example: POST /scan
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"url": "https://wordpress.org"}'
```

### Sample Response
```json
{
  "success": true,
  "data": {
    "id": 1,
    "url": "https://wordpress.org",
    "risk_level": "High",
    "technologies": {
      "CMS": ["WordPress"],
      "Frontend Framework": ["jQuery"],
      "Server": ["Nginx"],
      "Analytics": ["Google Analytics"]
    },
    "ssl_info": {
      "ssl_valid": true,
      "issuer": "Let's Encrypt",
      "expiry_date": "2025-06-01",
      "days_remaining": 96,
      "protocol": "TLSv1.3"
    },
    "headers_info": {
      "missing": [
        {"name": "Content-Security-Policy", "severity": "High"},
        {"name": "Permissions-Policy", "severity": "Low"}
      ],
      "present": [
        {"name": "Strict-Transport-Security", "value": "max-age=31536000"}
      ]
    },
    "ports_info": {
      "open": [{"port": 80, "service": "HTTP"}, {"port": 443, "service": "HTTPS"}],
      "risky_open": []
    },
    "vulnerabilities": [...],
    "recommendations": [...]
  }
}
```

---

## ✨ Features

- **Technology Detection** — CMS, frontend frameworks, servers, analytics, CDN, backend languages
- **SSL Certificate Analysis** — validity, issuer, expiry date, days remaining, protocol version
- **Security Headers Audit** — checks for HSTS, CSP, X-Frame-Options, XCTO, Referrer-Policy, Permissions-Policy
- **Port Scanner** — TCP connect scan on 17 common ports, flags risky ones
- **Vulnerability Engine** — maps findings to structured vulnerability records with severity levels
- **Recommendation Engine** — actionable remediations sorted by severity with external references
- **Scan History** — SQLite persistence, browse and re-load any past scan
- **PDF Export** — styled report generated with ReportLab
- **Cyberpunk UI** — dark theme with grid background, scan-line animation, glow effects
- **Input Validation** — blocks localhost/loopback, normalises URLs without scheme

---

## ⚙️ Configuration

Edit the constants at the top of each module to tune behaviour:

- `TIMEOUT` in `discovery.py` — HTTP/SSL request timeout (default: 10s)
- `COMMON_PORTS` in `discovery.py` — add/remove ports to scan
- `SECURITY_HEADERS` in `discovery.py` — extend the list of headers to audit
- `FINGERPRINTS` in `discovery.py` — add new technology signatures

---

## 📦 Dependencies

| Package      | Purpose                      |
|--------------|------------------------------|
| flask        | Web framework                |
| flask-cors   | Cross-origin requests        |
| requests     | HTTP client                  |
| beautifulsoup4 | HTML parsing               |
| lxml         | Fast HTML parser backend     |
| builtwith    | Additional tech fingerprints |
| reportlab    | PDF generation               |

---

## ⚠️ Legal Notice

Only scan websites you own or have explicit permission to test. Unauthorised scanning may violate computer misuse laws.
