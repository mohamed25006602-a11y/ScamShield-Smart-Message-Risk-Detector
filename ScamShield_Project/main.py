# ==========================================
# SCAMSHIELD - SMART MESSAGE RISK DETECTOR
# MAIN PROGRAM
# ==========================================

from scamshield import scan_message


def display_banner():

    print("\n")
    print("=" * 55)
    print("          SCAMSHIELD SECURITY SYSTEM")
    print("       SMART MESSAGE RISK DETECTOR")
    print("=" * 55)


def display_report(result):

    print("\n")
    print("-" * 55)
    print("             MESSAGE SCAN REPORT")
    print("-" * 55)

    print("\nSuspicious Keywords:")

    if result["keywords"]:
        for word in result["keywords"]:
            print("  -", word)
    else:
        print("  No suspicious keywords found.")

    print("\nSuspicious URLs:")

    if result["urls"]:
        for url in result["urls"]:
            print("  -", url)
    else:
        print("  No URLs detected.")

    print("\nRisk Score:", result["risk_score"], "/ 100")

    print("Threat Level:", result["threat"])

    print("\nSecurity Advice:")
    print(result["advice"])

    print("\n" + "=" * 55)


def main():

    display_banner()

    while True:

        print("\n1. Scan a Message")
        print("2. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            message = input("\nEnter your message:\n")

            if not message.strip():
                print("\nError: Message cannot be empty.")
                continue

            result = scan_message(message)

            display_report(result)

        elif choice == "2":

            print("\nThank you for using ScamShield!")
            print("Stay Safe. Stay Alert!")
            break

        else:

            print("\nInvalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
