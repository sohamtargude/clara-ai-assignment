import os
import json

# read transcript
with open("data/demo_bens_electric.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

# create account memo
memo = {
    "account_id": "account_1",
    "company_name": "Ben's Electric",
    "services_supported": [
        "electrical repair",
        "service calls",
        "troubleshooting",
        "EV charger installation",
        "panel upgrades",
        "residential electrical work",
        "commercial electrical work"
    ],
    "integration_constraints": "Uses Jobber CRM",
    "notes": "Extracted from demo call transcript"
}

# create agent spec
agent = {
    "agent_name": "Clara Agent - Bens Electric",
    "voice_style": "professional",
    "version": "v1",
    "system_prompt": "You are Clara, an AI answering assistant for an electrical services company."
}

# create folders
base = "outputs/accounts/account_1/v1"
os.makedirs(base, exist_ok=True)

# save memo
with open(base + "/memo.json", "w") as f:
    json.dump(memo, f, indent=2)

# save agent
with open(base + "/agent.json", "w") as f:
    json.dump(agent, f, indent=2)

print("Demo pipeline executed successfully.")