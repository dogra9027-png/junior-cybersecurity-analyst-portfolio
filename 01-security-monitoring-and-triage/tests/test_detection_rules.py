
import sys
import unittest
from pathlib import Path

# Add the src directory to Python's import path
PROJECT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

from detect_suspicious_activity import (
    evaluate_alert,
    detect_success_after_brute_force
)


class TestDetectionRules(unittest.TestCase):

    # DET-001: Brute-force detection
    def test_brute_force_detection(self):
        alert = {
            "alert_id": "TEST001",
            "timestamp": "2026-11-01 09:15:00",
            "source_ip": "185.220.101.45",
            "destination_ip": "10.0.0.8",
            "event_type": "Failed Login",
            "severity": "Medium",
            "failed_attempts": "35"
        }

        findings = evaluate_alert(alert)

        self.assertEqual(findings[0]["rule_id"], "DET-001")
        self.assertEqual(findings[0]["severity"], "High")

    # DET-002: Port scanning detection
    def test_port_scan_detection(self):
        alert = {
            "alert_id": "TEST002",
            "timestamp": "2026-11-01 09:30:00",
            "source_ip": "192.168.1.30",
            "destination_ip": "10.0.0.6",
            "event_type": "Port Scan",
            "severity": "Medium",
            "failed_attempts": "0"
        }

        findings = evaluate_alert(alert)

        self.assertEqual(findings[0]["rule_id"], "DET-002")

    # DET-003: High-severity detection
    def test_high_severity_detection(self):
        alert = {
            "alert_id": "TEST003",
            "timestamp": "2026-11-01 09:40:00",
            "source_ip": "103.75.118.20",
            "destination_ip": "10.0.0.8",
            "event_type": "Failed Login",
            "severity": "High",
            "failed_attempts": "5"
        }

        findings = evaluate_alert(alert)

        self.assertEqual(findings[0]["rule_id"], "DET-003")

    # DET-004: Successful login after brute-force activity
    def test_success_after_brute_force(self):
        alerts = [
            {
                "alert_id": "TEST004",
                "timestamp": "2026-11-01 09:20:00",
                "source_ip": "185.220.101.45",
                "destination_ip": "10.0.0.8",
                "event_type": "Failed Login",
                "severity": "High",
                "failed_attempts": "35"
            },
            {
                "alert_id": "TEST005",
                "timestamp": "2026-11-01 09:22:00",
                "source_ip": "185.220.101.45",
                "destination_ip": "10.0.0.8",
                "event_type": "Successful Login",
                "severity": "Medium",
                "failed_attempts": "0"
            }
        ]

        findings = detect_success_after_brute_force(alerts)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["rule_id"], "DET-004")
        self.assertEqual(findings[0]["severity"], "Critical")

    # Normal login: no detection expected
    def test_normal_successful_login(self):
        alert = {
            "alert_id": "TEST006",
            "timestamp": "2026-11-01 10:00:00",
            "source_ip": "192.168.1.50",
            "destination_ip": "10.0.0.5",
            "event_type": "Successful Login",
            "severity": "Low",
            "failed_attempts": "0"
        }

        findings = evaluate_alert(alert)

        self.assertEqual(len(findings), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
