import os

"""
Autocorrect for packages.

Patches
28.9.2025.create - Create the script
"""

def levenshtein_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1,
                           dp[i][j-1]+1,
                           dp[i-1][j-1]+cost)
    return dp[m][n]

def find_best_match(requested_name, packages):
    best_match = None
    min_dist = float('inf')
    for pkg in packages:
        dist = levenshtein_distance(requested_name, pkg)
        if dist < min_dist:
            min_dist = dist
            best_match = pkg
    return best_match

def main(package):
    os.system("curl -s -L -o pkgs https://raw.githubusercontent.com/crust-project/car/refs/heads/main/existing-packages.txt")
    with open("pkgs", "r") as f:
        pkgs = f.read().splitlines()
    os.remove("pkgs")
    install = find_best_match(package, pkgs)
    print("Note: Installing " + install + " instead of " + package)
