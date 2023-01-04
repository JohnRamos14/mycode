#!/usr/bin/env python3
"""Challenge01 diplay only the IP addresses to the screen"""

def main():
    """runtime"""

    # display only the IP addresses to the screen.
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

    # print IP address using F-String
    print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

if __name__ == "__main__":
    main()
