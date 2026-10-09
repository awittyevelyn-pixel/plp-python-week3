# bug_hunt.py

# =====================================================================
# THE BUGGY CODE (Logic Bug: Silent Failure / Infinite Loop)
# =====================================================================
# Problem Statement: We want to collect user savings until reaching a $100 goal.
# Bug Description: The condition 'savings > 100' stops immediately because savings starts at 0.
# No error is raised, but the body never runs!

savings = 0
goal = 100

print("--- BUGGY VERSION START ---")
# BUG: Incorrect comparison operator causes loop to exit immediately without error
while savings > goal:
    savings += 20
    print(f"Added $20. Current savings: ${savings}")

print(f"Buggy loop ended. Final savings: ${savings} (Expected: $100)")
print("--- BUGGY VERSION END ---\n")


# =====================================================================
# THE FIXED CODE
# =====================================================================
# Fix Description: Change the loop condition to 'savings < goal' so it loops
# until the savings reach or exceed $100.

savings = 0
goal = 100

print("--- FIXED VERSION START ---")
while savings < goal:
    savings += 20
    print(f"Added $20. Current savings: ${savings}")

print(f"Fixed loop completed! Final savings: ${savings}")
print("--- FIXED VERSION END ---")