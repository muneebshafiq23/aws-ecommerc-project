import json

products = {
    "1": {
        "id": 1,
        "name": "MacBook Pro m4",
        "price": 1899,
        "category": "Laptops",
        "stock": 12
    },

    "2": {
        "id": 2,
        "name": "iPhone Pro",
        "price": 1299,
        "category": "Smartphones",
        "stock": 20
    },

    "3": {
        "id": 3,
        "name": "Samsung Galaxy",
        "price": 999,
        "category": "Smartphones",
        "stock": 15
    }
}


def lambda_handler(event, context):

    query = event.get("queryStringParameters") or {}

    product_id = query.get("id")

    if not product_id:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": "Product ID is required"
            })
        }

    product = products.get(product_id)

    if not product:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": "Product not found"
            })
        }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(product)
    }
