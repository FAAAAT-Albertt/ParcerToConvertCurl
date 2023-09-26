import requests
from config import cookies_visa, headers_visa, mas_currents_visa, cookies_master, headers_master
import csv
from datetime import datetime


iter_cur = []

def parce_visa():

    date = datetime.now()
    format_date = date.strftime("%m/%d/%Y")

    for current in mas_currents_visa:
        current = current.replace("\n", "").strip()

        params_visa = {
            'amount': '1000',
            'fee': '2',
            'utcConvertedDate': format_date,
            'exchangedate': format_date,
            'fromCurr': 'KZT',
            'toCurr': current,
        }

        response = requests.get('https://www.visa.com.kz/cmsapi/fx/rates', params=params_visa, cookies=cookies_visa, headers=headers_visa)
        json_data = response.json()
        current_visa = current + "_" + "visa"
        convert_visa = json_data['convertedAmount'].replace(",", "")
        iter_cur.append({current_visa: convert_visa})

        params_master = {
            'fxDate': '0000-00-00',
            'transCurr': current,
            'crdhldBillCurr': 'KZT',
            'bankFee': '2',
            'transAmt': '1000',
        }

        try:
            response = requests.get(
                'https://www.mastercard.us/settlement/currencyrate/conversion-rate',
                params=params_master,
                cookies=cookies_master,
                headers=headers_master,
            )
            json_data2 = response.json()
            current_master = json_data2['data']['transCurr'] + "_" + "master"
            convert_master = json_data2['data']['crdhldBillAmt']
        except:
            current_master = json_data2['data']['transCurr'] + "_" + "master"
            convert_master = ""

        iter_cur.append({current_master: convert_master})

        pass




        # with open('data.csv', "a", encoding="utf-8") as file:
        #     writer = csv.writer(file, delimiter=" ")
        #     writer.writerow(())



def parce_master():

    for current in mas_currents_visa:
        current = current.replace("\n", "").strip()

        params_master = {
            'fxDate': '0000-00-00',
            'transCurr': current,
            'crdhldBillCurr': 'KZT',
            'bankFee': '2',
            'transAmt': '1000',
        }
        try:
            response = requests.get(
                'https://www.mastercard.us/settlement/currencyrate/conversion-rate',
                params=params_master,
                cookies=cookies_master,
                headers=headers_master,
            )
            i = response.json()
        except:
            convert = ""
        pass




def main():
    source = parce_visa()
    pass


if __name__ == '__main__':
    main()