responses = {

"order_status":
"Your order is currently being processed.",

"cancel_order":
"Your order cancellation request has been received.",

"refund":
"Your refund request has been initiated.",

"return":
"You can return the product within 7 days.",

"support":
"Our support team will contact you shortly."

}

def generate_response(intent):

    return responses.get(intent,
        "Sorry I could not understand your request.")