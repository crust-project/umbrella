import os

"""
A simple script that checks if installing a package can fix the error

Patches
- 25.9.2025.create - Create the script
"""

def main(package):
    os.system("curl -s -L -o pkgs https://raw.githubusercontent.com/crust-project/car/refs/heads/main/existing-packages.txt")
    with open("pkgs", "r") as f:
        pkgs = f.read().splitlines()
    os.remove("pkgs")
    if package in pkgs:
        print(package + " was not found, but can be installable with:")
        print("     car get " + package)
