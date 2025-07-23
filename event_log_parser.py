import win32evtlog
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import defaultdict
from datetime import datetime

# Read Windows Security Event Log
server = 'localhost'
log_type = 'Security'
hand = win32evtlog.OpenEventLog(server, log_type)
events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)

# Track events (4625: Failed Login, 4740: Account Lockout, 4672: Privilege Assignment)
event_data = defaultdict(lambda: defaultdict(int))
event_names = {4625: "Failed Login", 4740: "Account Lockout", 4672: "Privilege Assignment"}
target_date = "2025-07-22"

while events:
    for event in events:
        if event.EventID in [4625, 4740, 4672] and event.TimeGenerated.strftime("%Y-%m-%d") == target_date:
            user = event.StringInserts[5] if len(event.StringInserts) > 5 else "Unknown"
            hour = event.TimeGenerated.strftime("%H")
            event_data[event.EventID][f"{user} ({hour}:00)"] += 1
    events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)

win32evtlog.CloseEventLog(hand)

# Prepare heatmap data
if event_data:
    df_data = []
    for event_id, user_counts in event_data.items():
        for user_hour, count in user_counts.items():
            df_data.append({
                "Event": event_names[event_id],
                "User_Hour": user_hour,
                "Count": count
            })
    df = pd.DataFrame(df_data)
    
    # Pivot for heatmap
    pivot = df.pivot_table(index="Event", columns="User_Hour", values="Count", fill_value=0)
    
    # Plot heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, cmap="YlOrRd", annot=True, fmt=".0f", cbar_kws={'label': 'Event Count'})
    plt.title("Security Event Activity (July 22, 2025)")
    plt.xlabel("User and Hour")
    plt.ylabel("Event Type")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(r"C:\Users\PC\my-cyber-blog\docs\security_events_2025-07-22.png")
    plt.show()
    
    # Generate Markdown report
    report = f"# Security Event Analysis — 2025-07-22\n\n"
    report += "Analyzed Windows Security Event Logs to detect and visualize security events, demonstrating log analysis and automation skills for SOC Analyst roles.\n\n"
    report += "## Event Summary\n"
    for event_id, user_counts in event_data.items():
        report += f"- **{event_names[event_id]} (Event ID {event_id})**:\n"
        for user_hour, count in user_counts.items():
            report += f"  - {user_hour}: {count} occurrences\n"
    if not event_data:
        report += "No security events (Failed Logins, Account Lockouts, Privilege Assignments) found for 2025-07-22.\n"
    report += "\n## Visualization\n![Security Events](security_events_2025-07-22.png)\n"
    
    with open(r"C:\Users\PC\my-cyber-blog\docs\projects\security_events_2025-07-22.md", 'w', encoding='utf-8') as f:
        f.write(report)
else:
    print("No security events found for 2025-07-22")
