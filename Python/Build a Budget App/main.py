def create_spend_chart(categories):
    # 1. Calculate spending per category (withdrawals only)
    spendings = []
    for cat in categories:
        spent = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        spendings.append(abs(spent))
    
    total_spent = sum(spendings)
    # Avoid division by zero if no spending exists
    percentages = [(s / total_spent * 100) if total_spent > 0 else 0 for s in spendings]
    
    # 2. Build the chart top-down
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"
    
    # 3. Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # 4. Vertical names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    names_padded = [name.ljust(max_len) for name in names]
    
    for i in range(max_len):
        chart += "     "
        for name in names_padded:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"
            
    return chart