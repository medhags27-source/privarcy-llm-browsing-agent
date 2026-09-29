import re


PII_PATTERNS = {
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    "PHONE": r"(?<!\d)(?:\+91[-\s]?)?[6-9]\d{9}(?!\d)",

    "CREDIT_CARD": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",

    "AADHAAR": r"\b\d{4}\s\d{4}\s\d{4}\b",
}


# Detection priority: specific/longer patterns first
DETECTION_ORDER = [
    "EMAIL",
    "PHONE",
    "CREDIT_CARD",
    "AADHAAR",
]


def detect_pii(text):
    detections = []
    occupied_ranges = []

    for pii_type in DETECTION_ORDER:
        pattern = PII_PATTERNS[pii_type]

        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()

            # Skip this match if it overlaps with a PII match
            # that was already detected.
            overlaps = any(
                start < existing_end and end > existing_start
                for existing_start, existing_end in occupied_ranges
            )

            if overlaps:
                continue

            detections.append({
                "type": pii_type,
                "value": match.group(),
                "start": start,
                "end": end
            })

            occupied_ranges.append((start, end))

    return detections