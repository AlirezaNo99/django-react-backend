from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

logger = logging.getLogger('django')

@csrf_exempt
def get_payment_token(request):
    if request.method == "POST":
        try:
            # Parse JSON data
            data = json.loads(request.body.decode('utf-8'))
            logger.info("Received request to get payment token: %s", data)

            payload = {
                "TerminalID": data.get("TerminalID"),
                "Amount": data.get("amount"),
                "callbackURL": data.get("callbackURL"),
                "InvoiceID": data.get("invoiceID"),
                "payload":""
            }
            logger.info("Payload prepared for Mabna API: %s", payload)

            # Send the request to the payment gateway
            response = requests.post(
                "https://sepehr.shaparak.ir/Rest/V1/PeymentApi/GetToken",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            logger.info("Sent request to Mabna API. Status code: %s", response.status_code)
            logger.info("Response from Mabna API: %s", response.text)

            response.raise_for_status()
            return JsonResponse(response.json(), status=200)
        except json.JSONDecodeError:
            logger.error("Invalid JSON in request body")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except requests.exceptions.RequestException as e:
            logger.error("Error occurred while connecting to Mabna API: %s", e)
            return JsonResponse({"error": str(e)}, status=500)
        except Exception as ex:
            logger.exception("An unexpected error occurred: %s", ex)
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)
    else:
        logger.warning("Invalid request method: %s", request.method)
        return JsonResponse({"error": "Invalid request method"}, status=400)