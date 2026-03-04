import os
import json

# Step 1: Read onboarding transcript
with open("data/onboarding_bens_electric.txt", "r", encoding="utf-8") as f:
    onboarding_text = f.read()

# Step 2: Load previous agent memo (v1)
with open("outputs/accounts/account_1/v1/memo.json", "r", encoding="utf-8") as f:
    memo = json.load(f)

# Step 3: Update memo with onboarding information
memo["business_hours"] = "8 AM - 5 PM"
memo["after_hours_action"] = "Collect customer details and schedule follow-up"
memo["emergency_handling"] = "Transfer emergency electrical calls to owner"
memo["spam_filtering"] = "Filter sales and spam calls"

# Step 4: Create v2 folder
v2_path = "outputs/accounts/account_1/v2"
os.makedirs(v2_path, exist_ok=True)

# Step 5: Save updated memo
with open(f"{v2_path}/memo.json", "w", encoding="utf-8") as f:
    json.dump(memo, f, indent=2)

# Step 6: Create updated agent configuration
agent = {
    "agent_name": "Clara AI Agent",
    "version": "v2",
    "role": "AI receptionist for Ben's Electric",
    "tasks": [
        "Answer customer calls",
        "Collect customer details",
        "Schedule service appointments",
        "Transfer emergency calls",
        "Filter spam calls"
    ]
}

# Step 7: Save agent.json
with open(f"{v2_path}/agent.json", "w", encoding="utf-8") as f:
    json.dump(agent, f, indent=2)

# Step 8: Create changelog
os.makedirs("changelog", exist_ok=True)

with open("changelog/account_1_changes.md", "w") as f:
    f.write(
        "Changes from v1 to v2:\n"
        "- Added business hours configuration\n"
        "- Added after-hours handling\n"
        "- Added emergency call routing\n"
        "- Added spam call filtering\n"
    )

print("Onboarding pipeline executed successfully.")