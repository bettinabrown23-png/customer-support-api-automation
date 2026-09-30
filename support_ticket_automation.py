# Customer Support Ticket Automation
# A simple workflow for identifying and prioritizing support tickets.

tickets = [
    {"customer": "Customer A", "issue": "Payment problem", "status": "open"},
    {"customer": "Customer B", "issue": "Password reset", "status": "resolved"},
    {"customer": "Customer C", "issue": "Order delay", "status": "open"},
    {"customer": "Customer D", "issue": "Account question", "status": "pending"}
]

print("Customer Support Ticket Report")
print("--------------------------------")

for ticket in tickets:
    if ticket["status"] == "open":
        print(
            f"Follow up required: {ticket['customer']} - "
            f"{ticket['issue']}"
        )
    elif ticket["status"] == "pending":
        print(
            f"Monitor ticket: {ticket['customer']} - "
            f"{ticket['issue']}"
        )

print("--------------------------------")
print("Ticket processing complete.")
