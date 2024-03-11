def calculate_roi(purchase_price, monthly_rental_income, monthly_expenses, investment_duration):
    total_cash_flow = 0
    total_investment = purchase_price
    
    # Calculate total cash flow over the investment duration
    for _ in range(investment_duration * 12):
        total_cash_flow += monthly_rental_income - monthly_expenses
    
    # Calculate total ROI
    total_roi = (total_cash_flow / total_investment) * 100
    
    # Calculate average annual ROI
    average_annual_roi = total_roi / investment_duration
    
    return total_cash_flow, total_roi, average_annual_roi

def main():
    print("Welcome to the Rental Property ROI Calculator")
    print("---------------------------------------------")
    purchase_price = float(input("Enter the purchase price of the property: $"))
    monthly_rental_income = float(input("Enter the monthly rental income: $"))
    monthly_expenses = float(input("Enter the monthly expenses: $"))
    investment_duration = int(input("Enter the investment duration (in years): "))
    
    total_cash_flow, total_roi, average_annual_roi = calculate_roi(purchase_price, monthly_rental_income, monthly_expenses, investment_duration)
    
    print("\nResults:")
    print("Total Cash Flow over", investment_duration, "years: $", round(total_cash_flow, 2))
    print("Total ROI: {:.2f}%".format(total_roi))
    print("Average Annual ROI: {:.2f}%".format(average_annual_roi))

if __name__ == "__main__":
    main()