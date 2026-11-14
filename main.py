import json
import urllib.request


url_pb = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
req_pb = urllib.request.urlopen(url_pb)
data_pb = json.loads(req_pb.read().decode())


usd_rate = 0
for item in data_pb:
  if item["ccy"] == "USD":
    usd_rate = float(item["sale"])
    break

print("Курс ПриватБанку (USD/UAH):", usd_rate)


res_parse_list = []
response = urllib.request.urlopen("https://coinmarketcap.com/")
response_text = response.read().decode("utf-8")
response_parse = response_text.split("<span>")

for parse_elem_1 in response_parse:
  if parse_elem_1.startswith("$"):
    for parse_elem_2 in parse_elem_1.split("</span>"):
      if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
        res_parse_list.append(parse_elem_2)

bitcoin = res_parse_list[0]
price = float(bitcoin.replace("$", "").replace(",", ""))
print("Ціна BTC в доларах:", price)


bitcoin_uah = price * usd_rate
print(f"Ціна 1 BTC в гривнях (за ПриватБанком): {bitcoin_uah:,.2f} грн")


amount = float(input("Введіть кількість біткоїнів: "))
total_uah = amount * bitcoin_uah
print(f"Ваша сума: {total_uah:,.2f} грн")
