# Onboarding Assistant

An interactive Python application that generates structured employee onboarding plans based on job role, department, and experience level.

**[Launch the Live App](https://noa-onboarding-assistant.streamlit.app)**

## Overview

The Onboarding Assistant helps create consistent, role-specific onboarding plans. Users can generate tasks, review responsibilities and expected outcomes, track onboarding progress, and export plans for further use.

## Features

- **Role-based planning:** Supports Project Manager, BI Analyst, and Marketing Specialist roles.
- **Department customization:** Adapts plans to the selected department.
- **Experience-level adaptation:** Tailors onboarding plans for Junior, Mid-level, and Senior employees.
- **Task details:** Includes phases, priorities, owners, instructions, and expected outcomes.
- **Progress tracking:** Mark tasks as completed and monitor overall progress.
- **Export options:** Download onboarding plans as TXT or Excel files.
- **Excel formatting:** Includes status dropdowns and conditional formatting for task tracking.
- **Interactive web interface:** Built with Streamlit.

## Technology Stack

- Python
- Streamlit
- OpenPyXL
- Git and GitHub

## How It Works

1. Select the employee's job title and department.
2. Choose the employee's experience level.
3. Generate a tailored onboarding plan.
4. Review tasks, responsibilities, and expected outcomes.
5. Track progress and export the plan.

## Implementation Notes

The current version uses predefined rules to generate onboarding plans. It does not yet use a live AI model.

## Future Improvements

- AI-powered plan generation
- Additional job roles and customizable onboarding templates
- Persistent storage for onboarding plans and progress

## Run Locally

```bash
git clone https://github.com/noashushan/onboarding-assistant.git
cd onboarding-assistant
pip install -r requirements.txt
streamlit run app.py
```

## Author

**Noa Shushan**

Developed as a portfolio project exploring workflow automation, structured planning, and interactive data-driven applications.
