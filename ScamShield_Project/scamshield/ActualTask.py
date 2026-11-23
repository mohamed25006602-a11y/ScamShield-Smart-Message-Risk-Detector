# ==========================================
# SCAMSHIELD - SMART MESSAGE RISK DETECTOR
# ==========================================

import re

# Suspicious keywords database
SCAM_KEYWORDS = {
    "urgent": 15,
    "otp": 20,
    "password": 20,
    "bank account": 20,
    "click here": 15,
    "won": 10,
    "free prize": 15,
    "claim now": 15,
    "limited time": 10,
    "verify account": 20
}


# Function 1: Detect suspicious keywords
def detect_suspicious_keywords(message):

    if not isinstance(message, str):
        raise TypeError("Message must be text.")

    found_keywords = []

    text = message.lower()

    for keyword in SCAM_KEYWORDS:

        if keyword in text:
            found_keywords.append(keyword)

    return found_keywords


# Function 2: Detect suspicious URLs
def detect_suspicious_urls(message):

    if not isinstance(message, str):
        raise TypeError("Message must be text.")

    urls = re.findall(r'https?://\S+|www\.\S+', message)

    return urls


# Function 3: Calculate risk score
def calculate_risk_score(keywords, urls):

    score = 0

    for keyword in keywords:
        score += SCAM_KEYWORDS[keyword]

    if urls:
        score += 20

    return min(score, 100)


# Function 4: Classify threat level
def classify_threat(score):

    if score <= 20:
        return "LOW RISK"

    elif score <= 50:
        return "SUSPICIOUS"

    else:
        return "HIGH RISK"


# Function 5: Generate safety advice
def generate_safety_advice(threat):

    if threat == "HIGH RISK":
        return "Do not click links or share personal information."

    elif threat == "SUSPICIOUS":
        return "Verify the sender before taking action."

    else:
        return "No major warning signs detected. Stay alert."


# Function 6: Scan complete message
def scan_message(message):

    keywords = detect_suspicious_keywords(message)

    urls = detect_suspicious_urls(message)

    score = calculate_risk_score(keywords, urls)

    threat = classify_threat(score)

    advice = generate_safety_advice(threat)

    return {
        "keywords": keywords,
        "urls": urls,
        "risk_score": score,
        "threat": threat,
        "advice": advice
    }
