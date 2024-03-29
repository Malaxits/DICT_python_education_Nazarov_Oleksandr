import math

language = input("Choose language (en,ua): ")
if language == "en":
    # English translations
    welcome_message = "Welcome \n" \
                      " Power by Stell!"
    calculation_options = "What do you want to calculate?\n" \
                          "type 'n' for number of monthly payments,\n" \
                          "type 'a' for annuity monthly payment amount,\n" \
                          "type 'p' for loan principal,\n" \
                          "type 'd' for differentiated payment."
    principal_prompt = "Enter the loan principal:"
    num_periods = "Enter the number of periods:"
    periods_prompt = "Enter the number of periods:"
    payment_prompt = "Enter the monthly payment:"
    interest_prompt = "Enter the loan interest:"
    payment_result = "Your monthly payment = "
    periods_result = "It will take "
    overpayment_result = "Overpayment = {} "
    year_prompt = "It will take {} months to repay this loan!"
    mount_prompt = "It will take {} years to repay this loan!"
    m_y_prompt = "It will take {} years and {} months to repay this loan!"
    periods_numb = "Enter the number of periods:"
    periods_m_y = "You need to pay {} per month for {} months"
    periods_m_and_y = "You need to pay {} per month for {} years and {} months"
    l_principal = "Your loan principal = {} with {} months to repay"
    principal_m_y = "Your loan principal = {} with {} years and {} months to repay"
    mount_pay = "Month {}: payment is {}"
    Error = "Invalid calculation type"
    Error2 = "Invalid language choice."
elif language == "ua":
    # Ukrainian translations
    welcome_message = "Вітаю \n" \
                      "Power by Stell!"
    calculation_options = "Що ви хочете обчислити?\n" \
                          "введіть 'n' для кількості щомісячних платежів,\n" \
                          "введіть 'a' для суми щомісячного платежу,\n" \
                          "введіть 'p' для суми кредиту,\n" \
                          "введіть 'd' для диференціальних платежів."
    principal_prompt = "Введіть суму кредиту:"
    num_periods = "Введіть кількість періодів:"
    periods_prompt = "Введіть кількість періодів:"
    payment_prompt = "Введіть щомісячний платіж:"
    interest_prompt = "Введіть відсотки по кредиту:"
    payment_result = "Ваш щомісячний платіж = "
    periods_result = "Кредит буде виплачено "
    overpayment_result = "переплата = {}"
    year_prompt = "На погашення цієї позики знадобиться {} місяців!"
    mount_prompt = "На погашення цієї позики знадобиться {} років!"
    m_y_prompt = "На погашення цієї позики знадобиться {} років і {} місяців!"
    periods_numb = " Введіть кількість періодів:"
    periods_m_y = "Вам потрібно платити {} на місяць протягом {} місяців "
    periods_m_and_y = "Вам потрібно платити {} на місяць протягом {} років і {} місяців"
    l_principal = "Основна сума вашої позики = {} із {} місяців до погашення"
    principal_m_y = "Основна сума вашої позики = {} з {} років і {} місяців до погашення"
    mount_pay = "Місяць {}: платіж становить {}"
    Error = "Недійсний тип обчислення"
    Error2 = "Недійсний вибір мови."