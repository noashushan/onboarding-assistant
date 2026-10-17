def generate_onboarding_plan(job_title, department,experience_level):
    """Create a starter onboarding plan for a professional role."""



    role = job_title.strip().lower()
    dept = department.strip().lower()

    if role == "project manager":
        tasks = [
            {
                "phase": "Before Day 1",
                "task": "Prepare the project handover",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "List the active projects assigned to the employee.",
                    "Identify urgent deadlines and open issues.",
                    "Collect relevant files and contact details."
                ],
                "expected_outcome": "The employee has an organized starting point for their assigned projects."
            },
            {
                "phase": "Day 1",
                "task": "Agree on responsibilities and priorities",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "Explain the employee's main responsibilities.",
                    "Identify the most important tasks for the first week.",
                    "Clarify which decisions require manager approval."
                ],
                "expected_outcome": "The employee understands their responsibilities and initial priorities."
            },
            {
                "phase": "Week 1",
                "task": "Map the project workflow",
                "priority": "High",
                "owner": "New employee",
                "instructions": [
                    "Choose one active project with the manager.",
                    "Document its main stages, owners and next milestones.",
                    "List missing information and questions for the manager."
                ],
                "expected_outcome": "A basic workflow map is documented and unclear points are identified."
            },
            {
                "phase": "Week 2",
                "task": "Complete a supervised project update",
                "priority": "Medium",
                "owner": "New employee",
                "instructions": [
                    "Update one project's status using available information.",
                    "Record the next action, responsible person and open risks.",
                    "Review the update with the manager and apply feedback."
                ],
                "expected_outcome": "A project update is completed and reviewed by the manager."
            },
            {
                "phase": "Days 15-30",
                "task": "Review progress and independence",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "Review the tasks completed during onboarding.",
                    "Identify tasks the employee can perform independently.",
                    "Agree on remaining support needs and next goals."
                ],
                "expected_outcome": "Progress, remaining gaps and next goals are documented."
            }
        ]

    elif role == "bi analyst":
        tasks = [
            {
                "phase": "Before Day 1",
                "task": "Prepare access to data and reporting tools",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "Identify the data sources and tools needed for the role.",
                    "Request the appropriate access permissions.",
                    "Prepare a sample report or approved practice dataset."
                ],
                "expected_outcome": "Required access is ready or outstanding requests are identified."
            },
            {
                "phase": "Day 1",
                "task": "Understand business reporting needs",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "Review one existing business report.",
                    "Identify its audience and the questions it should answer.",
                    "Clarify unfamiliar metrics and business terms."
                ],
                "expected_outcome": "The employee can explain the purpose and audience of the selected report."
            },
            {
                "phase": "Week 1",
                "task": "Explore a sample dataset",
                "priority": "High",
                "owner": "New employee",
                "instructions": [
                    "Inspect the available columns and data types.",
                    "Check for missing values, duplicates and inconsistencies.",
                    "Record questions about fields whose meaning is unclear."
                ],
                "expected_outcome": "The employee documents the dataset structure and initial quality issues."
            },
            {
                "phase": "Week 2",
                "task": "Reproduce an existing report",
                "priority": "Medium",
                "owner": "New employee",
                "instructions": [
                    "Select a small report with the manager.",
                    "Reproduce one metric using the approved data source.",
                    "Compare the result with the existing report and investigate differences."
                ],
                "expected_outcome": "The metric is reproduced or differences are documented for review."
            },
            {
                "phase": "Days 15-30",
                "task": "Present findings and next steps",
                "priority": "Medium",
                "owner": "New employee",
                "instructions": [
                    "Summarize the work completed during onboarding.",
                    "Present one finding or data-quality issue.",
                    "Agree on the next reporting task with the manager."
                ],
                "expected_outcome": "Findings and the next agreed task are documented."
            }
        ]

    else:
        tasks = [
            {
                "phase": "Before Day 1",
                "task": "Prepare the employee's starting materials",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "List the tools and access required for the role.",
                    "Collect available work examples and reference materials.",
                    "Identify anything that still needs to be prepared."
                ],
                "expected_outcome": "Starting materials are ready or missing items are identified."
            },
            {
                "phase": "Day 1",
                "task": "Clarify responsibilities and expectations",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "Explain the main responsibilities of the role.",
                    "Agree on the first week's priorities.",
                    "Clarify who can answer questions and approve decisions."
                ],
                "expected_outcome": "The employee understands their initial responsibilities and support contacts."
            },
            {
                "phase": "Week 1",
                "task": "Complete a guided work task",
                "priority": "High",
                "owner": "New employee",
                "instructions": [
                    "Select a representative task with the manager.",
                    "Review any available instructions or examples.",
                    "Complete the task with guidance and record unanswered questions."
                ],
                "expected_outcome": "The employee completes a first task with guidance and identifies knowledge gaps."
            },
            {
                "phase": "Days 8-30",
                "task": "Review progress and remaining questions",
                "priority": "High",
                "owner": "Manager",
                "instructions": [
                    "Review completed work and feedback.",
                    "Identify tasks that still require guidance.",
                    "Agree on the next learning goals."
                ],
                "expected_outcome": "Progress and next steps are agreed with the employee."
            }
        ]
        
    # Adapt onboarding tasks to the employee's experience level
    experience_instructions = {
        "Junior": (
            "Schedule a check-in with the manager to review progress "
            "and answer questions."
            ),
        "Mid-level": (
            "Identify which parts of this task can be completed "
            "independently and which need review."
            ),
        "Senior": (
            "Identify opportunities to take ownership and recommend "
            "process improvements."
            )
        }
    independence_levels = {
        "Junior": "Guided",
        "Mid-level": "Semi-independent",
        "Senior": "Independent"
    }

    instruction = experience_instructions.get(experience_level)

    if instruction:
        for task in tasks:
            task["instructions"].append(instruction)
            task["independence_level"] = independence_levels.get(
                experience_level, "Semi-independent"
                )
    if experience_level == "Senior":
        for task in tasks:
            if task["task"] == "Complete a guided work task":
                task["task"] = "Complete an independent work task"

                task["instructions"][2] = (
                    "Complete the task independently and document any blockers."
                )

                task["expected_outcome"] = (
                    "The employee completes the task independently "
                    "and identifies opportunities for improvement."
                )    

    if dept == "operations":
        tasks.append({
            "phase": "Week 1",
            "task": "Document an operational process",
            "priority": "Medium",
            "owner": "New employee",
            "instructions": [
                "Choose a recurring operational process.",
                "Document its main steps and responsible people.",
                "Identify one possible improvement."
            ],
            "expected_outcome": "A process document is created and one improvement opportunity is identified."
        })

    return tasks


def display_onboarding_plan(job_title, department, tasks):
    print("\n" + "=" * 50)
    print("ONBOARDING PLAN")
    print("=" * 50)
    print(f"Job title: {job_title}")
    print(f"Department: {department}")
    print("\nIMPORTANT: This is a draft for manager review.")

    for number, task in enumerate(tasks, start=1):
        print(f"\n{number}. {task['task']}")
        print(f"   Phase: {task['phase']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Owner: {task['owner']}")
        print(f"   Independence level: {task.get('independence_level', 'Not specified')}")
        print("   Instructions:")

        for step in task["instructions"]:
            print(f"      - {step}")

        print(f"   Expected outcome: {task['expected_outcome']}")

