# pdf_parser.py
import re

def extract_data_from_pdf(pdf_text):
    data = {}

    # ISIN
    isin_match = re.search(r'ISIN: (\S+)', pdf_text)
    if isin_match:
        data['Isin'] = isin_match.group(1)

    # Issuer
    issuer_match = re.search(r'Issuer (.+?) Guarantor', pdf_text)
    if issuer_match:
        data['Issuer'] = issuer_match.group(1).strip()

    # Currency
    currency_match = re.search(r'Currency (\w+)', pdf_text)
    if currency_match:
        data['Ccy'] = currency_match.group(1)

   # Launch Date, Final Valuation Date, Maturity Date
    date_matches = re.findall(r'Launch Date (\d{2}\.\d{2}\.\d{4})|Final Valuation Date (\d{2}\.\d{2}\.\d{4})|Maturity Date (\d{2}\.\d{2}\.\d{4})', pdf_text)

    data['Launch Date'] = None
    data['Final Valuation Date'] = None
    data['Maturity'] = None

    for date in date_matches:
        if date[0]:
            data['Launch Date'] = date[0]
        elif date[1]:
            data['Final Valuation Date'] = date[1]
        elif date[2]:
            data['Maturity'] = date[2]

    # Underlying
    underlying_match = re.search(r'Underlying (.+?) Strike Level', pdf_text)
    if underlying_match:
        data['Underlying(s)'] = [underlying.strip() for underlying in underlying_match.group(1).split(',')]

    # Strike Level
    strike_match = re.search(r'Strike Level (\d+%?)', pdf_text)
    if strike_match:
        data['Strike'] = float(strike_match.group(1).strip('%'))

    # Barrier
    barrier_match = re.search(r'Knock-In Barrier (\d+%?)', pdf_text)
    if barrier_match:
        data['Barrier'] = float(barrier_match.group(1).strip('%'))

    

    return data
