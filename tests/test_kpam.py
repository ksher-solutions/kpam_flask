import requests
import string
import random
import json
import unittest

KPAM_ENDPOINT = "http://localhost:5000"


class TestKPAM(unittest.TestCase):
    def test_gateway_pay(self):
        letters = string.ascii_letters
        numbers = "0123456789"
        mch_order_no = "".join([random.choice(letters) for _ in range(3)] + [random.choice(numbers) for _ in range(7)])
        channel_list = "alipay,wechat,linepay,airpay,bbl_promptpay,truemoney"
        product_name = "".join([random.choice(letters) for _ in range(2)] + [random.choice(numbers) for _ in range(3)])
        total_fee = 1
        url = KPAM_ENDPOINT + "/gateway_pay"
        headers = {
            "Content-Type": "application/json"
        }
        body = {
            "channel_list": channel_list,
            "mch_order_no": mch_order_no,
            "product_name": product_name,
            "total_fee": total_fee
        }
        resp = requests.post(url=url, headers=headers, data=json.dumps(body)).json()
        self.assertEqual("pay_content" in resp.get("data"), True, "Should have key: pay_content in data")
        self.assertEqual(resp.get("message"), "SUCCESS", "Response message should be SUCCESS")


if __name__ == "__main__":
    unittest.main()
