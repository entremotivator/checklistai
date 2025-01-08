import streamlit as st

# Define checklist categories and items
checklist = {
    "Email Management": [
        "Review unread emails and sort by priority.",
        "Flag important emails requiring human input.",
        "Send automated responses where applicable."
    ],
    "Task Updates": [
        "Check pending tasks and deadlines.",
        "Provide progress updates on assigned tasks.",
        "Alert on overdue or stalled tasks."
    ],
    "Communication Monitoring": [
        "Review and summarize messages from chat platforms.",
        "Draft responses or follow-ups.",
        "Monitor for escalations requiring attention."
    ],
    "Project Management": [
        "Check task completion rates for ongoing projects.",
        "Update progress trackers or dashboards.",
        "Notify team of upcoming deadlines or milestones."
    ],
    # Add more categories as needed
}

# Initialize session state for tracking progress
if "progress" not in st.session_state:
    st.session_state.progress = {category: [False] * len(items) for category, items in checklist.items()}

# App title and description
st.title("AI Employee Daily Productivity Checklist")
st.markdown("""
This app helps you track and manage daily productivity tasks for your AI employee.
Check off completed tasks and monitor progress across all categories.
""")

# Display the checklist with progress tracking
for category, items in checklist.items():
    st.subheader(category)
    for i, item in enumerate(items):
        is_checked = st.checkbox(item, value=st.session_state.progress[category][i], key=f"{category}-{i}")
        st.session_state.progress[category][i] = is_checked

# Calculate overall progress
total_tasks = sum(len(items) for items in checklist.values())
completed_tasks = sum(
    sum(st.session_state.progress[category]) for category in checklist.keys()
)
progress_percent = (completed_tasks / total_tasks) * 100

# Display progress bar and summary
st.progress(progress_percent / 100)
st.write(f"### Progress: {completed_tasks} / {total_tasks} tasks completed ({progress_percent:.2f}%)")

# Reset button
if st.button("Reset Checklist"):
    st.session_state.progress = {category: [False] * len(items) for category, items in checklist.items()}
    st.experimental_rerun()
