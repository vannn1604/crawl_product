import json
import re

import psycopg2


with open("spec_old.json") as json_file:
    data_product = json.load(json_file)

    for data in data_product:
        connection = None
        try:
            connection = psycopg2.connect(
                host="172.17.0.2", database="tizzie", user="tizzie", password="tizzie"
            )
            connection.autocommit = True
            cur = connection.cursor()
            cur.execute(
                "insert into products(name,brand,specs) values(%s,%s,%s)",
                (data["name"], data["brand"], json.dumps(data["specs"]),),
            )
            cur.close()
            connection.close()
        except:
            continue

        #     connection.commit()
        # except psycopg2.DatabaseError as error:
        #     if cur is not None:
        #         connection.rollback()
        # finally:
        #     if connection is not None:
        #         connection.close()



# scripts = [
#     '\nvar SPEC_VERSIONS = [[\n["a2218", {\n"net2g": "GSM 850 \\/ 900 \\/ 1800 \\/ 1900 ",\n"net3g": "HSDPA 850 \\/ 900 \\/ 1700(AWS) \\/ 1900 \\/ 2100 ",\n"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\\/2100), 5(850), 7(2600), 8(900), 11(1500), 12(700), 13(700), 17(700), 18(800), 19(800), 20(800), 21(1500), 25(1900), 26(850), 28(700), 29(700), 30(2300), 32(1500), 34(2000), 38(2600), 39(1900), 40(2300), 41(2500), 42(3500), 46(5200), 48, 66(1700\\/2100)",\n"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\\/2100), 5(850), 7(2600), 8(900), 11(1500), 12(700), 13(700), 17(700), 18(800), 19(800), 20(800), 21(1500), 25(1900), 26(850), 28(700), 29(700), 30(2300), 32(1500), 34(2000), 38(2600), 39(1900), 40(2300), 41(2500), 42(3500), 46(5200), 48, 66(1700\\/2100)",\n"sim": "Nano-SIM and\\/or Electronic SIM card",\n"comment": "For Global market",\n}],\n["a2161", {\n"net2g": "GSM 850 \\/ 900 \\/ 1800 \\/ 1900 ",\n"net3g": "HSDPA 850 \\/ 900 \\/ 1700(AWS) \\/ 1900 \\/ 2100 ",\n"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\\/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 14(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 29(700), 30(2300), 34(2000), 38(2600), 39(1900), 40(2300), 41(2500), 42(3500), 46(5200), 48, 66(1700\\/2100), 71(600)",\n"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\\/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 14(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 29(700), 30(2300), 34(2000), 38(2600), 39(1900), 40(2300), 41(2500), 42(3500), 46(5200), 48, 66(1700\\/2100), 71(600)",\n"sim": "Nano-SIM and\\/or Electronic SIM card",\n"price": "<a href=\\"apple_iphone_11_pro_max-price-0.php\\">&#36;&thinsp;1,099.99 \\/ &#8364;&thinsp;1,172.63 \\/ &#163;&thinsp;939.00 \\/ &#8377;&thinsp;109,900<\\/a>",\n"comment": "For USA, Canada, Puerto Rico, U.S. Virgin Islands",\n}],\n["a2220", {\n"modelname": "Apple iPhone 11 Pro Max Dual SIM",\n"net2g": "GSM 850 \\/ 900 \\/ 1800 \\/ 1900 - SIM 1 & SIM 2",\n"net3g": "HSDPA 850 \\/ 900 \\/ 1700(AWS) \\/ 1900 \\/ 2100 ",\n"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\\/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 14(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 29(700), 30(2300), 34(2000), 38(2600), 39(1900), 40(2300), 41(2500), 42(3500), 46(5200), 48, 66(1700\\/2100), 71(600)",\n"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\\/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 14(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 29(700), 30(2300), 34(2000), 38(2600), 39(1900), 40(2300), 41(2500), 42(3500), 46(5200), 48, 66(1700\\/2100), 71(600)",\n"sim": "Dual SIM (Nano-SIM, dual stand-by)",\n"comment": "For China, Hong Kong",\n}],\n]];\n'
# ]

# spec_ver = None
# for script in scripts:
#     if "SPEC_VERSIONS" in script:
#         script = re.sub("[\\\\\n]", "", script)
#         match = re.search(r"\[.*\]", script)
#         if match and match.group():
#             script = match.group(0)

# # indexs = [index.start() for index in re.finditer("}]", script)]
# for ch in script:
#     if ch == "}]":
#         print(True)
# script[index.start() + 2] = ""

# print(json.loads(a[1:-1]))
