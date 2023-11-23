import openai
from wha import extract_data_from_pdf
openai.api_key = "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"

def refine_data_with_llm(data):
    # Data To Prompt
    prompt = f"Extracted data from PDF: {data}"

    refined_data = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    return refined_data['choices'][0]['text']

if __name__ == "__main__":
    # Example text
    pdf_text = """Structured Product - Summary of Terms
15-Month USD Bonus Certificate Worst-Of on Euro Stoxx 50 Price EUR,
FTSE 100 Index and S&P 500
Issued by BNP Paribas Arbitrage Issuance B.V.
Arranger: Banque Pictet & Cie SA | 24 January 2022 | Pictet ID: AB4194 | ISIN: XS2021832634
This structured product is not a collective investment scheme and is not subject to the authorization of the FINMA
(the Swiss Financial Markets Supervisory Authority).
This Summary of Terms does not constitute a Swiss Simplified Prospectus as per article 5 CISA.
This structured product is not issued by an entity of the Pictet Group. Please refer to the documentation of
the Issuer (such as, but not limited to, the attached term-sheet and any other relevant documents including the
issue prospectus, if available) which shall prevail in case of discrepancies with any information contained in this
Summary of Terms. The information and data furnished in this material are for information purposes only.
The selling restrictions and tax treatment are set out in the documentation of the Issuer.
Issuer BNP Paribas Arbitrage Issuance B.V. Guarantor Rating (Moody's / S&P / Fitch) - (Aa3/A+/AA-)
Guarantor BNP Paribas, Paris SVSP 1320
Issuance Type Note, unsecured,
unsubordinated obligations of the Issuer
Launch Date 21.01.2022
Issue Price 100% of Denomination Issue Date 28.01.2022
Currency USD (Quanto) Final Valuation Date 21.04.2023
Denomination USD 1'000 Maturity Date 28.04.2023
Underlying Worst performing
(see below Components Information table)
Strike Level 100% of Initial Level
Knock-In Barrier 65% of Initial Level Knock-In Type American Daily Close
Bonus Level 11.7%
Upside
Participation
100%
Redemption Type Cas"""

    extracted_data = extract_data_from_pdf(pdf_text)
    refined_data = refine_data_with_llm(extracted_data)

    print("Extracted Data:")
    print(extracted_data)

    print("\nRefined Data:")
    print(refined_data)