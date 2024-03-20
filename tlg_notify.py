import requests
import time
from datetime import date

bot_toked = "6822761867:AAH93Lsc1UXam18RH6mUXiK0QM8JPaEeu_w"
# chat_id = "@st7_pp_notify"
# chat_id = "@st7_pp_notity"
chat_id = "756357473"
chat_id_list = ['1096082261', '756357473']

html = (
    "<strong>INVOICE NUMBER: {inv_no}</strong>\n"
    "<strong>សរុប: {grand_total}</strong>\n"
    "<code>បានទទួលប្រាក់: {received_amount}</code>\n"
    "<code>📆 {date}</code>\n"
    "<code>=======================</code>\n"
    "<code>1. coca 10x0.25</code>\n"
    "<code>2. abc 1x25</code>\n"
    "<code>3. sting 1x25</code>\n"
).format(
    inv_no='inv00001',
    grand_total='1,000$',
    received_amount='100$',
    date=date.today(),
)

for acc_id in chat_id_list:
    res = requests.get(f"https://api.telegram.org/bot{bot_toked}/sendMessage?chat_id={acc_id}&text={html}&parse_mode=HTML")
    print(res)
    time.sleep(10)


