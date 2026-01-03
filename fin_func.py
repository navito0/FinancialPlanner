INFLATION_RATE = 0.07
RETURN_RATE = 0.12

def calculate_retirement_corpus(
    current_age,
    retirement_age,
    current_monthly_expense,
    inflation_rate=INFLATION_RATE,
    post_retirement_return=RETURN_RATE,
):
    """
    Calculate required retirement corpus.

    Parameters:
    current_monthly_expense (float): Current monthly expense
    years_to_retire (int): Years left to retire
    inflation_rate (float): Expected inflation rate (default 7%)
    post_retirement_return (float): Return after retirement (default 12%)
    retirement_years (int): Years you expect to live after retirement

    Returns:
    float: Required retirement corpus
    """

    # Step 1: Inflate expenses till retirement
    years_to_retire = retirement_age - current_age
    inflated_expense = 12 * current_monthly_expense * ((1 + inflation_rate) ** years_to_retire)

    # Step 2: Calculate retirement corpus (PV of annuity)
    r = (1 + post_retirement_return)/ (1 + inflation_rate) - 1

    retirement_years = 100 - retirement_age
    corpus = inflated_expense * (
        (1 - (1 + r) ** (-retirement_years)) / r
    )

    return round(corpus, 2)

if __name__ == "__main__":
    corp = calculate_retirement_corpus(50,50,150000)
    print(corp)