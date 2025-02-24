import streamlit as st

# Define checklist categories and items (10 departments with 10 tasks each = 100 tasks)
checklist = {
    "Email Management": [
        "Review unread emails and sort by priority.",
        "Flag important emails requiring human input.",
        "Send automated responses where applicable.",
        "Organize emails into designated folders.",
        "Scan spam and junk folders for misclassified messages.",
        "Set up and refine email filters for recurring topics.",
        "Monitor urgent email threads throughout the day.",
        "Schedule follow-up reminders for pending emails.",
        "Archive old emails to free up space.",
        "Update and standardize email signatures."
    ],
    "Task Updates": [
        "Review pending tasks and upcoming deadlines.",
        "Update task statuses in the project management tool.",
        "Assign new tasks to relevant team members.",
        "Reassess priorities for the day’s workload.",
        "Document completed tasks for performance tracking.",
        "Reschedule overdue tasks and set new deadlines.",
        "Communicate task changes to involved stakeholders.",
        "Verify task dependencies and adjust timelines.",
        "Review daily progress and plan next steps.",
        "Ensure task handoffs are clear between departments."
    ],
    "Communication Monitoring": [
        "Review messages from internal chat platforms.",
        "Summarize key points from team communications.",
        "Draft responses for pending inquiries.",
        "Monitor communication channels for urgent issues.",
        "Flag critical messages for immediate follow-up.",
        "Update communication logs with important notes.",
        "Schedule brief daily stand-up meetings.",
        "Ensure clarity in team and inter-departmental messages.",
        "Track response times to external queries.",
        "Monitor social media channels for brand mentions."
    ],
    "Project Management": [
        "Review overall project timelines and milestones.",
        "Update progress trackers and dashboards.",
        "Identify and mitigate potential project risks.",
        "Coordinate with project managers for status updates.",
        "Ensure optimal resource allocation for projects.",
        "Review and update project documentation.",
        "Schedule status meetings and progress reviews.",
        "Analyze performance metrics for ongoing projects.",
        "Confirm milestone completions with team leads.",
        "Communicate upcoming deadlines to stakeholders."
    ],
    "Data Analysis": [
        "Collect data from various internal sources.",
        "Clean and preprocess raw data sets.",
        "Perform exploratory data analysis on current trends.",
        "Generate and update data visualizations.",
        "Maintain real-time data dashboards.",
        "Identify anomalies and trends in data streams.",
        "Review data quality and ensure consistency.",
        "Compile comprehensive data analysis reports.",
        "Document key insights and findings.",
        "Plan further investigations based on data trends."
    ],
    "System Maintenance": [
        "Check system logs for errors and warnings.",
        "Run routine diagnostics to ensure system health.",
        "Apply software updates and security patches.",
        "Monitor overall system performance metrics.",
        "Back up critical data and system configurations.",
        "Optimize system resource usage and performance.",
        "Review hardware status reports for anomalies.",
        "Test system recovery and failover procedures.",
        "Schedule regular maintenance tasks.",
        "Document all maintenance activities and outcomes."
    ],
    "Client Engagement": [
        "Review client feedback and address concerns.",
        "Schedule and prepare for client meetings or calls.",
        "Update client engagement records and CRM data.",
        "Respond promptly to client inquiries.",
        "Monitor client satisfaction and feedback metrics.",
        "Prepare detailed progress reports for clients.",
        "Coordinate with sales and support teams for follow-up.",
        "Follow up on outstanding client action items.",
        "Review historical communication with each client.",
        "Plan strategies for improved client engagement."
    ],
    "Security Checks": [
        "Review system security alerts and notifications.",
        "Conduct regular vulnerability scans.",
        "Update security protocols and best practices.",
        "Monitor access logs for unusual activities.",
        "Verify firewall and antivirus configurations.",
        "Review and update user access permissions.",
        "Document any security incidents promptly.",
        "Schedule periodic security audits.",
        "Test incident response procedures with simulations.",
        "Report critical security issues to management."
    ],
    "Reporting & Documentation": [
        "Compile and review daily performance reports.",
        "Update ongoing project documentation regularly.",
        "Edit and refine internal reports for clarity.",
        "Generate client-facing reports with key insights.",
        "Organize documentation for easy retrieval.",
        "Verify data accuracy within all reports.",
        "Archive outdated reports systematically.",
        "Prepare detailed meeting minutes and summaries.",
        "Draft new documentation for emerging processes.",
        "Review documentation standards and compliance."
    ],
    "Innovation & Improvement": [
        "Identify potential areas for process improvement.",
        "Brainstorm innovative solutions with the team.",
        "Research industry best practices and trends.",
        "Evaluate and test new AI tools and technologies.",
        "Collect team suggestions for workflow enhancements.",
        "Pilot new strategies to improve operational efficiency.",
        "Review feedback from previous innovation trials.",
        "Document lessons learned from recent initiatives.",
        "Plan training sessions on new process improvements.",
        "Assess the overall impact of implemented innovations."
    ]
}

# Initialize session state for tracking progress if not already set
if "progress" not in st.session_state:
    st.session_state.progress = {category: [False] * len(items) for category, items in checklist.items()}

# App title and description
st.title("AI Employee Daily Productivity & Task Tracking Checklist")
st.markdown("""
This application is designed to help you manage and track daily productivity tasks across multiple departments for your AI employee.
Utilize this comprehensive checklist to monitor task completion, ensure timely follow-ups, and maintain high performance across all operational areas.
""")

# Display the checklist with progress tracking
for category, items in checklist.items():
    st.subheader(category)
    for i, item in enumerate(items):
        is_checked = st.checkbox(item, value=st.session_state.progress[category][i], key=f"{category}-{i}")
        st.session_state.progress[category][i] = is_checked

# Calculate overall progress
total_tasks = sum(len(items) for items in checklist.values())
completed_tasks = sum(sum(st.session_state.progress[category]) for category in checklist.keys())
progress_percent = (completed_tasks / total_tasks) * 100

# Display progress bar and summary
st.progress(progress_percent / 100)
st.write(f"### Progress: {completed_tasks} / {total_tasks} tasks completed ({progress_percent:.2f}%)")

# Reset button to clear all progress
if st.button("Reset Checklist"):
    st.session_state.progress = {category: [False] * len(items) for category, items in checklist.items()}
    st.experimental_rerun()
