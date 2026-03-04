# Overview
This project implements a simple automation pipeline that converts demo call transcripts into an AI agent configuration and then updates it using onboarding information.

The goal is to simulate how Clara AI agents are configured for service businesses.

#Workflow

Pipeline A: Demo Call → Preliminary Agent

Input:
- Demo call transcript

Process:
- Extract basic business information
- Generate an initial AI agent configuration

Output:
- Account memo JSON
- Retell agent draft specification (v1)

Pipeline B: Onboarding Call → Agent Update

Input:
- Onboarding call transcript

Process:
- Extract operational configuration details
- Update the existing agent configuration

Output:
- Updated account memo JSON
- Updated Retell agent specification (v2)
- Changelog of updates
