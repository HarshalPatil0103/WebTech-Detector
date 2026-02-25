# WebTech-Detector
================================================================================
                        WEB TECH DETECTOR
              A Cybersecurity Technology Fingerprinting Tool
================================================================================

  Scan any website to discover its technology stack and security weaknesses.
  Get risk scores, actionable recommendations, and downloadable PDF reports.

================================================================================
TABLE OF CONTENTS
================================================================================

  1. What Is This?
  2. Features
  3. Technologies Detected
  4. Security Checks
  5. Project Structure
  6. Requirements
  7. Installation & Setup
  8. How To Run
  9. How To Use
 10. API Reference
 11. Running Tests
 12. Responsible Use Warning
 13. Troubleshooting
 14. Author

================================================================================
1. WHAT IS THIS?
================================================================================

Web Tech Detector is a self-hosted web application built with Python (Flask)
on the backend and plain HTML/CSS/JavaScript on the frontend.

You enter a website URL, and the tool will:

  - Detect what CMS, frameworks, and server software the site uses
  - Check if the SSL certificate is valid and when it expires
  - Find missing HTTP security headers and explain why they matter
  - Scan for open ports that could be a security risk
  - Calculate an overall risk level (Low / Medium / High / Critical)
  - Give you specific, actionable steps to fix each issue found
  - Let you download a PDF report of the full scan
  - Save all your past scans so you can refer back to them

It is designed for developers auditing their own projects, students learning
about web security, and anyone who wants a quick overview of a site's security
posture before working with it.

================================================================================
2. FEATURES
================================================================================

  [+] Technology fingerprinting across 6 categories (32 technologies total)
  [+] SSL/TLS certificate validation and expiry check
  [+] Security header audit (8 headers checked)
  [+] TCP port scanner (17 common ports)
  [+] Risk scoring with Low / Medium / High / Critical levels
  [+] Detailed vulnerability list with descriptions
  [+] Actionable fix recommendations for every finding
  [+] PDF report download
  [+] Scan history saved to local SQLite database
  [+] Dark cyberpunk-themed UI with animations
  [+] SSRF protection (cannot scan localhost or private IP ranges)
  [+] Fully self-hosted, no data sent to any third-party service

================================================================================
3. TECHNOLOGIES DETECTED
================================================================================

  CMS (Content Management Systems)
  ---------------------------------
  WordPress, Joomla, Drupal, Shopify, Wix, Squarespace, Magento

  Frontend Frameworks & Libraries
  --------------------------------
  React, Vue.js, Angular, Next.js, Nuxt.js,
  jQuery, Bootstrap, Tailwind CSS

  Backend Languages
  -----------------
  PHP, Python, Node.js, Ruby on Rails, ASP.NET

  Web Servers
  -----------
  Apache, Nginx, IIS, LiteSpeed, Cloudflare

  CDN (Content Delivery Networks)
  --------------------------------
  Cloudflare, Amazon CloudFront, Fastly, jsDelivr

  Analytics & Tracking
  --------------------
  Google Analytics, Google Tag Manager, Hotjar, Intercom

  Detection works by analysing:
    - HTTP response headers
    - HTML source code and script tags
    - Meta generator tags
    - Cookie names
    - Script and stylesheet URLs

================================================================================
4. SECURITY CHECKS
================================================================================

  Security Headers Audited
  ------------------------
  The tool checks for the presence of these HTTP response headers
  and flags any that are missing:

  Header Name                   Severity   What It Protects Against
  ----------------------------  ---------  --------------------------------
  Strict-Transport-Security     High       Forces HTTPS (prevents downgrade)
  Content-Security-Policy       High       XSS and data injection attacks
  X-Frame-Options               Medium     Clickjacking attacks
  X-Content-Type-Options        Medium     MIME-sniffing attacks
  Referrer-Policy               Medium     Referrer information leakage
  Permissions-Policy            Low        Unauthorised browser feature use
  X-XSS-Protection              Low        Legacy XSS filter
  Cache-Control                 Low        Sensitive data being cached

  SSL / TLS Checks
  ----------------
    - Whether the site uses HTTPS at all
    - Whether the certificate is valid and trusted
    - Whether the certificate has expired
    - How many days until the certificate expires (warns if under 30 days)
    - Certificate issuer and subject
    - TLS protocol version in use

  Port Scanning
  -------------
  The following ports are checked via TCP connection:

  Port   Service       Risky?
  -----  -----------   ------
  21     FTP           YES - transmits data in plaintext
  22     SSH           No
  23     Telnet        YES - completely unencrypted protocol
  25     SMTP          YES - potential mail relay abuse
  53     DNS           No
  80     HTTP          No
  110    POP3          No
  143    IMAP          No
  443    HTTPS         No
  445    SMB           YES - ransomware and exploit vector
  3306   MySQL         YES - database should not be public
  3389   RDP           YES - brute-force and ransomware target
  5432   PostgreSQL    YES - database should not be public
  6379   Redis         YES - often runs with no authentication
  8080   HTTP-Alt      No
  8443   HTTPS-Alt     No
  27017  MongoDB       YES - frequently misconfigured with no auth

  Risk Scoring
  ------------
  Each finding adds to the overall risk score. The final verdict is:

    Low      - Good security posture, minor issues only
    Medium   - Some important issues to address
    High     - Significant vulnerabilities found
    Critical - Severe security problems that need immediate attention

================================================================================
5. PROJECT STRUCTURE
================================================================================

  web-tech-detector/
  |
  +-- backend/
  |   +-- app.py                  Main Flask server and all API routes
  |   +-- modules/
  |   |   +-- discovery.py        Tech detection, SSL check, header audit,
  |   |   |                       port scanning
  |   |   +-- security.py         Vulnerability analysis and recommendations
  |   |   +-- reporter.py         Alternative PDF builder (ReportLab)
  |   |   +-- scanner.py          Additional scanner utilities
  |   +-- utils/
  |   |   +-- validators.py       URL validation and SSRF protection
  |   |   +-- pdf_report.py       PDF report generator
  |   |   +-- database.py         Database helper utilities
  |   +-- tests/
  |       +-- test_validators.py  Unit tests for URL validation
  |       +-- test_security.py    Unit tests for security analysis
  |
  +-- frontend/
  |   +-- templates/
  |   |   +-- index.html          Single-page application shell
  |   +-- static/
  |       +-- css/
  |       |   +-- style.css       Dark cyberpunk UI theme
  |       +-- js/
  |           +-- app.js          All frontend JavaScript logic
  |
  +-- database/
  |   +-- db.py                   SQLite database functions
  |   +-- scans.db                Auto-created on first run
  |
  +-- requirements.txt            Python package list
  +-- README.md                   Markdown documentation
  +-- README.txt                  This file

================================================================================
6. REQUIREMENTS
================================================================================

  System Requirements
  -------------------
    - Python 3.8 or higher
    - pip (Python package manager)
    - An internet connection (to scan external websites)
    - A modern web browser (Chrome, Firefox, Edge, Safari)

  Python Packages Required
  ------------------------
  These are the only packages you need to install. Everything else used
  by this project (sqlite3, ssl, socket, re, os, json) is already built
  into Python.

  Package          Version    Purpose
  ---------------  ---------  ----------------------------------------
  flask            3.0+       Web framework and API server
  flask-cors       4.0+       Handles cross-origin browser requests
  requests         2.31+      Fetches the target website content
  beautifulsoup4   4.12+      Parses HTML for technology detection
  lxml             any        HTML parser engine for BeautifulSoup
  reportlab        4.0+       Generates downloadable PDF reports

================================================================================
7. INSTALLATION & SETUP
================================================================================

  OPTION A: Simple Install (Recommended for beginners)
  -----------------------------------------------------

  Step 1 - Open a terminal or command prompt.

  Step 2 - Navigate to the project folder:

             cd web-tech-detector

  Step 3 - Install the required Python packages:

             pip install flask flask-cors requests beautifulsoup4 lxml reportlab

  Step 4 - Done. You are ready to run the app.


  OPTION B: Virtual Environment (Recommended for developers)
  -----------------------------------------------------------
  A virtual environment keeps these packages isolated from the rest of
  your system, which is cleaner and avoids version conflicts.

  Step 1 - Navigate to the project folder:

             cd web-tech-detector

  Step 2 - Create a virtual environment:

             python -m venv venv

  Step 3 - Activate the virtual environment:

             On macOS / Linux:
               source venv/bin/activate

             On Windows:
               venv\Scripts\activate

             You will see (venv) appear at the start of your terminal prompt.
             This means the virtual environment is active.

  Step 4 - Install the required packages:

             pip install flask flask-cors requests beautifulsoup4 lxml reportlab

  Step 5 - Done. You are ready to run the app.

  To deactivate the virtual environment when you are finished:

             deactivate


================================================================================
8. HOW TO RUN
================================================================================

  Step 1 - Make sure you have completed the installation steps above.

  Step 2 - Navigate to the backend folder:

             cd web-tech-detector/backend

  Step 3 - Start the Flask server:

             python app.py

  Step 4 - You should see output similar to this:

             * Running on http://0.0.0.0:5000
             * Debug mode: on

  Step 5 - Open your web browser and go to:

             http://localhost:5000

  The application is now running. The database file (scans.db) will be
  created automatically the first time you run the app. You do not need
  to set it up manually.

  To stop the server, press CTRL + C in the terminal.

  NOTE: Leave the terminal window open while using the app. Closing it
  will shut down the server.

================================================================================
9. HOW TO USE
================================================================================

  Running a Scan
  --------------
  1. Open http://localhost:5000 in your browser.
  2. Type or paste a website URL into the input field.
     Example:  https://wordpress.org
  3. Click the SCAN button or press Enter.
  4. Wait for the scan to complete (usually 10-30 seconds).
  5. The results will appear on the same page.

  You can enter URLs with or without the protocol prefix:
    - https://example.com       (works)
    - http://example.com        (works)
    - example.com               (works, https:// is added automatically)

  Reading the Results
  -------------------
  Risk Banner      - Shows the URL, overall risk level, and score out of 100.
  Technology Stack - Cards showing every technology detected, by category.
  Security Findings - Each vulnerability found, colour-coded by severity.
  SSL / TLS        - Certificate details and validity status.
  Open Ports       - Any open ports found, with risky ones highlighted in red.
  Recommendations  - Specific steps to fix each issue, ordered by severity.

  Viewing Scan History
  --------------------
  Click the HISTORY tab in the top navigation bar to see all past scans.
  From there you can:
    - VIEW  - Open the full JSON data for any past scan in a new tab.
    - X     - Delete a scan from history permanently.

  Downloading a PDF Report
  ------------------------
  After running a scan, click the "EXPORT PDF" button at the bottom of
  the results to download a formatted PDF report of that scan.

  Starting a New Scan
  -------------------
  Click the "NEW SCAN" button to clear the results and scan a different URL.

================================================================================
10. API REFERENCE
================================================================================

  The backend runs as a REST API on port 5000. You can call these endpoints
  directly using curl, Postman, or any HTTP client.

  -----------------------------------------------------------------------
  POST /scan
  -----------------------------------------------------------------------
  Run a full scan on a URL.

  Request body (JSON):
    { "url": "https://example.com" }

  Example with curl:
    curl -X POST http://localhost:5000/scan \
         -H "Content-Type: application/json" \
         -d '{"url": "https://example.com"}'

  Success response:
    {
      "success": true,
      "data": {
        "id": 1,
        "url": "https://example.com",
        "risk_level": "Medium",
        "risk_score": 40,
        "technologies": {
          "CMS": ["WordPress"],
          "Frontend Framework": ["jQuery", "Bootstrap"],
          "Backend Language": ["PHP"],
          "Server": ["Apache"]
        },
        "ssl_info": {
          "ssl_valid": true,
          "issuer": "Let's Encrypt",
          "days_remaining": 54
        },
        "vulnerabilities": [...],
        "recommendations": [...]
      }
    }

  Error response:
    { "success": false, "error": "Invalid URL: ..." }

  -----------------------------------------------------------------------
  GET /history
  -----------------------------------------------------------------------
  Returns a list of all past scans, newest first.

  Example:
    curl http://localhost:5000/history

  -----------------------------------------------------------------------
  GET /report/<id>
  -----------------------------------------------------------------------
  Returns the full JSON data for a specific scan by its ID.

  Example:
    curl http://localhost:5000/report/1

  -----------------------------------------------------------------------
  GET /report/<id>?format=pdf
  -----------------------------------------------------------------------
  Downloads a PDF report for the scan with the given ID.

  Example:
    curl "http://localhost:5000/report/1?format=pdf" --output report.pdf

  -----------------------------------------------------------------------
  DELETE /report/<id>/delete
  -----------------------------------------------------------------------
  Permanently deletes a scan from the history database.

  Example:
    curl -X DELETE http://localhost:5000/report/1/delete

================================================================================
11. RUNNING TESTS
================================================================================

  The project includes unit tests for the URL validator and security
  analysis modules.

  To run all tests:

    cd web-tech-detector
    python -m pytest backend/tests/ -v

  To run a specific test file:

    python -m pytest backend/tests/test_validators.py -v
    python -m pytest backend/tests/test_security.py -v

  Note: pytest must be installed to run the tests:

    pip install pytest

================================================================================
12. RESPONSIBLE USE WARNING
================================================================================

  !! IMPORTANT - PLEASE READ !!

  Only scan websites that you own or have explicit written permission
  to test. Scanning websites without authorisation may violate laws
  including but not limited to:

    - The Computer Fraud and Abuse Act (CFAA) in the United States
    - The Computer Misuse Act (CMA) in the United Kingdom
    - Similar computer crime legislation in your country

  This tool is intended for:
    - Auditing your own websites and applications
    - Educational purposes and learning about web security
    - Penetration testing with proper written authorisation

  This tool is NOT intended for:
    - Scanning websites you do not own or have permission to test
    - Reconnaissance for malicious purposes
    - Any activity that violates laws or terms of service

  Built-in protections in this tool:
    - Scanning localhost is blocked
    - Scanning 127.0.0.1 and ::1 is blocked
    - Scanning private IP ranges (10.x, 192.168.x, 172.16-31.x) is blocked
    - Scanning the AWS metadata endpoint (169.254.169.254) is blocked
    - Only http:// and https:// protocols are permitted

  The author takes no responsibility for misuse of this software.

================================================================================
13. TROUBLESHOOTING
================================================================================

  Problem:  "ModuleNotFoundError: No module named 'flask'"
  Fix:      Run the install command again:
              pip install flask flask-cors requests beautifulsoup4 lxml reportlab
            If using a virtual environment, make sure it is activated first.

  -----------------------------------------------------------------------

  Problem:  "Address already in use" when starting the server
  Fix:      Another program is using port 5000. Either:
            - Stop the other program using port 5000
            - Or change the port in backend/app.py (last line):
                app.run(debug=True, host="0.0.0.0", port=5001)
              Then access the app at http://localhost:5001

  -----------------------------------------------------------------------

  Problem:  "Network error: Failed to execute 'json' on 'Response'"
  Fix:      The Flask server is not running or has crashed.
            - Check that you ran: python app.py from the backend/ folder
            - Check the terminal for any Python error messages
            - Make sure all packages are installed correctly

  -----------------------------------------------------------------------

  Problem:  Scan takes very long or times out
  Fix:      Some websites block automated requests or have slow servers.
            - Try a different URL to confirm the tool is working
            - The port scan timeout is 1 second per port by default

  -----------------------------------------------------------------------

  Problem:  SSL certificate check fails for a valid HTTPS site
  Fix:      Some servers have non-standard SSL configurations. The scan
            will still complete and return results for other checks.

  -----------------------------------------------------------------------

  Problem:  PDF download fails or produces an empty file
  Fix:      Make sure ReportLab is installed:
              pip install reportlab
            If it is installed and still failing, check the terminal for
            error messages when you click the Export PDF button.

  -----------------------------------------------------------------------

  Problem:  The browser shows a blank page at http://localhost:5000
  Fix:      - Make sure the server is running (check the terminal)
            - Try doing a hard refresh: CTRL + SHIFT + R (Windows/Linux)
              or CMD + SHIFT + R (macOS)
            - Check there are no errors in the browser console
              (press F12 and click the Console tab)

================================================================================
14. AUTHOR
================================================================================

  Web Tech Detector
  Version: 1.0

  Built as a full-stack cybersecurity learning project.

  Tech Stack:
    Backend   - Python 3.8+ with Flask
    Frontend  - Vanilla HTML, CSS, and JavaScript
    Database  - SQLite
    Detection - BeautifulSoup4 and custom regex fingerprints
    Reports   - ReportLab PDF library

  Feel free to fork, modify, and build upon this project.

================================================================================
                            END OF README
================================================================================