"""
run.py
Convenience script to start the Web Technology Detector server.
Run with: python run.py
"""
import sys
import os

# Ensure project root is on PYTHONPATH
sys.path.insert(0, os.path.dirname(__file__))

from backend.app import app

if __name__ == "__main__":
    print("=" * 60)
    print("  🛡  Web Technology Detector")
    print("  Starting server on http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, host="0.0.0.0", port=5000)
