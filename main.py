import requests
from config import cookies_visa, headers_visa, mas_currents_visa, cookies_master, headers_master
import csv
from datetime import datetime


iter_cur = []

def parce_visa():

    date = datetime.now()
    format_date = date.strftime("%m/%d/%Y")

    for current in mas_currents_visa:
        st = ""
        current = current.replace("\n", "").strip()
        try:

            params_visa = {
                'amount': '1000',
                'fee': '2',
                'utcConvertedDate': "09/26/2023",
                'exchangedate': "09/26/2023",
                'fromCurr': 'KZT',
                'toCurr': current,
            }

            response = requests.get('https://www.visa.com.kz/cmsapi/fx/rates', params=params_visa, cookies=cookies_visa, headers=headers_visa)
            json_data = response.json()

            currentfrom = json_data['conversionFromCurrency']
            convert_visa = json_data['convertedAmount'].replace(",", "")
            st += f"VISA {currentfrom} -> {convert_visa};"

        except:
            pass


        try:

            params_visa = {
                'amount': '1000',
                'fee': '2',
                'utcConvertedDate': "09/26/2023",
                'exchangedate': "09/26/2023",
                'fromCurr': current,
                'toCurr': "KZT",
            }

            response = requests.get('https://www.visa.com.kz/cmsapi/fx/rates', params=params_visa, cookies=cookies_visa, headers=headers_visa)
            json_data = response.json()

            currentfrom = json_data['conversionFromCurrency']
            convert_visa = json_data['convertedAmount'].replace(",", "")
            st += f" VISA {currentfrom} -> {convert_visa};"

        except:
            pass

        try:
            params_master = {
                'fxDate': '0000-00-00',
                'transCurr': current,
                'crdhldBillCurr': 'KZT',
                'bankFee': '2',
                'transAmt': '1000',
            }


            response = requests.get(
                'https://www.mastercard.us/settlement/currencyrate/conversion-rate',
                params=params_master,
                cookies=cookies_master,
                headers=headers_master,
            )
            json_data2 = response.json()

            transCurr = json_data2['data']['transCurr']
            convert_master = json_data2['data']['crdhldBillAmt']
            st += f"MS {transCurr} -> {convert_master};"

        except:
            pass


        try:
            params_master = {
                'fxDate': '0000-00-00',
                'transCurr': 'KZT',
                'crdhldBillCurr': current,
                'bankFee': '2',
                'transAmt': '1000',
            }


            response = requests.get(
                'https://www.mastercard.us/settlement/currencyrate/conversion-rate',
                params=params_master,
                cookies=cookies_master,
                headers=headers_master,
            )
            json_data2 = response.json()

            transCurr = json_data2['data']['transCurr']
            convert_master = json_data2['data']['crdhldBillAmt']
            st += f" MS {transCurr} -> {convert_master};\n"
        except:
            pass

        with open('data.csv', "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([st])



def load_csv(st):
    with open('data.csv', "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([st])


def main():
    source = parce_visa()
    pass


if __name__ == '__main__':
    main()