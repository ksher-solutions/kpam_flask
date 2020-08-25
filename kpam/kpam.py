#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#
#  The module implementation goes here
#
#  Start an HTTP server, expose RESTFUL APIs for all kinds of Ksher Services.
#  If required, pull results from Ksher Services and send update to the Application by callback/notification
#  Manage the status of the transaction.
#

from flask import Flask, request
import kpam.utils as utils
import kpam.ksherpay as ksherpay
import logging

_logger = logging.getLogger("KPAM")

app = Flask(__name__)
DEFAULT_FEE_TYPE = "THB"
PRIVATE_KEY_PATH = None


@app.route("/_hc")
def health_check():
    return {
        "status": "ok"
    }


@app.route("/gateway_pay", methods=["POST"])
def gateway_pay():
    required_fields = [
        "channel_list",
        "mch_order_no",
        "product_name",
        "total_fee",
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel_list": data["channel_list"],
        "mch_code": appid.replace("mch", ""),
        "mch_order_no": data["mch_order_no"],
        "product_name": data["product_name"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", DEFAULT_FEE_TYPE),
        "mch_redirect_url": data.get("mch_redirect_url", ""),
        "mch_redirect_url_fail": data.get("mch_redirect_url_fail", ""),
        "refer_url": data.get("refer_url", "")
    }

    optional_fields = [
        "device",
        "background",
        "payment_color",
        "ksher_explain",
        "hide_explain",
        "expire_time",
        "hide_exp_time",
        "logo",
        "lang",
        "shop_name",
        "attach",
    ]

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info(f"Gateway Pay: {fields}")

    resp = payment.gateway_pay(**fields)
    return resp


@app.route("/gateway_order_query", methods=["POST"])
def gateway_order_query():
    required_fields = [
        "mch_order_no"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "mch_order_no": data["mch_order_no"]
    }

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Gateway Order Query: {fields}".format(fields=fields))

    resp = payment.gateway_order_query(**fields)
    return resp


@app.route("/quick_pay", methods=["POST"])
def quick_pay():
    required_fields = [
        "channel",
        "mch_order_no",
        "total_fee",
        "auth_code"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "mch_order_no": data["mch_order_no"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", DEFAULT_FEE_TYPE)
    }

    optional_fields = [
        "product",
        "attach",
        "device_id",
        "operator_id"
    ]

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Quick Pay: {fields}".format(fields=fields))

    resp = payment.quick_pay(**fields)
    return resp


@app.route("/native_pay", methods=["POST"])
def native_pay():
    required_fields = [
        "channel",
        "total_fee"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", DEFAULT_FEE_TYPE)
    }

    optional_fields = [
        "notify_url",
        "img_type",
        "product",
        "attach",
        "device_id"
    ]

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Native Pay: {fields}".format(fields=fields))

    resp = payment.native_pay(**fields)
    return resp


@app.route("/mini_program_pay", methods=["POST"])
def mini_program_pay():
    required_fields = [
        "channel",
        "mch_order_no",
        "total_fee",
        "sub_openid",
        "channel_sub_appid"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "mch_order_no": data["mch_order_no"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", DEFAULT_FEE_TYPE),
        "sub_openid": data["sub_openid"],
        "channel_sub_appid": data["channel_sub_appid"],
        "notify_url": data.get("notify_url", ""),
        "product": data.get("product", "")
    }

    optional_fields = [
        "attach",
        "device_id"
    ]

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Mini Program Pay: {fields}".format(fields=fields))

    resp = payment.minipro_pay(**fields)
    return resp


@app.route("/app_pay", methods=["POST"])
def app_pay():
    required_fields = [
        "mch_order_no",
        "total_fee",
        "channel",
        "sub_openid",
        "channel_sub_appid"
    ]

    data = request.json
    if data.get("channel") == "alipay":
        required_fields.append("refer_url")
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "mch_order_no": data["mch_order_no"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", DEFAULT_FEE_TYPE),
        "sub_openid": data["sub_openid"],
        "channel_sub_openid": data["channel_sub_openid"]
    }

    optional_fields = [
        "redirect_url",
        "notify_url",
        "paypage_title",
        "product",
        "attach",
        "opreator_id",
        "refer_url"
    ]

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("App Pay: {fields}".format(fields=fields))

    resp = payment.app_pay(**fields)
    return resp


@app.route("/order_query", methods=["POST"])
def order_query():
    required_fields = [
        "channel"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    selection_fields = [
        "mch_order_no",
        "ksher_order_no",
        "channel_order_no"
    ]

    if not utils.validate_selection_fields(selection_fields=selection_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"]
    }

    for field in selection_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Order Query: {fields}".format(fields=fields))

    resp = payment.order_query(**fields)
    return resp


@app.route("/order_reverse", methods=["POST"])
def order_reverse():
    required_fields = [
        "channel"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    selection_fields = [
        "mch_order_no",
        "ksher_order_no",
        "channel_order_no"
    ]

    if not utils.validate_selection_fields(selection_fields=selection_fields, data=data):
        return {"error": "Missing One of these Fields: {selection_fields}".format(selection_fields=selection_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"]
    }

    optional_fields = [
        "product",
        "attach",
        "device_id",
        "operator_id"
    ]

    for field in selection_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Order Reverse: {fields}".format(fields=fields))

    resp = payment.order_reverse(**fields)
    return resp


@app.route("/order_refund", methods=["POST"])
def order_refund():
    required_fields = [
        "channel",
        "total_fee",
        "mch_refund_no",
        "refund_fee"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    selection_fields = [
        "mch_order_no",
        "ksher_order_no",
        "channel_order_no"
    ]

    if not utils.validate_selection_fields(selection_fields=selection_fields, data=data):
        return {"error": "Missing One of these Fields: {selection_fields}".format(selection_fields=selection_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", "THB"),
        "mch_refund_no": data["mch_refund_no"],
        "refund_fee": data["refund_fee"]
    }

    optional_fields = [
        "product",
        "attach",
        "device_id",
        "operator_id"
    ]

    for field in selection_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Order Refund: {fields}".format(fields=fields))

    resp = payment.order_refund(**fields)
    return resp


@app.route("/refund_query", methods=["POST"])
def refund_query():
    required_fields = [
        "channel",
        "total_fee",
        "mch_refund_no",
        "refund_fee"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    selection_fields = [
        "mch_order_no",
        "ksher_order_no",
        "channel_order_no"
    ]

    if not utils.validate_selection_fields(selection_fields=selection_fields, data=data):
        return {"error": "Missing One of these Fields: {selection_fields}".format(selection_fields=selection_fields)}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "total_fee": data["total_fee"],
        "fee_type": data.get("fee_type", "THB"),
        "mch_refund_no": data["mch_refund_no"],
        "refund_fee": data["refund_fee"]
    }

    optional_fields = [
        "attach",
        "device_id",
        "operator_id"
    ]

    for field in selection_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    for field in optional_fields:
        if field in data.keys():
            fields.update({field: data[field]})

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Refund Query: {fields}".format(fields=fields))

    resp = payment.refund_query(**fields)
    return resp


@app.route("/rate_query", methods=["POST"])
def rate_query():
    required_fields = [
        "channel",
        "date"
    ]

    data = request.json
    if not utils.validate_required_fields(required_fields=required_fields, data=data):
        return {"error": "Missing Required Fields: {required_fields}".format(required_fields=required_fields)}

    fmt = "%Y-%m-%d"
    if not utils.validate_datetime(data["date"], fmt):
        return {"error": "Date format is incorrect. Must be in YYYY-mm-dd format"}

    appid = data.get("appid", utils.get_app_id(PRIVATE_KEY_PATH))
    fields = {
        "appid": appid,
        "channel": data["channel"],
        "fee_type": data.get("fee_type", "THB")
    }

    payment = ksherpay.KsherPay(
        appid=fields["appid"], privatekey=PRIVATE_KEY_PATH
    )

    _logger.info("Rate Query: {fields}".format(fields=fields))

    resp = payment.rate_query(**fields)
    return resp


def start_server(**kwargs):
    app.env = kwargs["env"]
    app.debug = kwargs["debug"]
    global PRIVATE_KEY_PATH
    PRIVATE_KEY_PATH = kwargs["cred_key"]
    app.run()
