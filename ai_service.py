import os
from openai import OpenAI

client = OpenAI(
api_key=os.environ.get("OPENAI_API_KEY")
)

def generate_product_description(name, category):
try:
prompt = f"""
Generate a professional e-commerce product description.


    Product Name: {name}
    Category: {category}

    Keep the description between 80 and 120 words.
    Highlight key features and benefits.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

except Exception:
    return f"{name} is a quality product in the {category} category."

def predict_product_price(name, category):
try:
prompt = f"""
You are an e-commerce pricing expert.


    Product Name: {name}
    Category: {category}

    Estimate a realistic selling price in USD.

    Return only a numeric value.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return float(
        response.choices[0].message.content.strip()
    )

except Exception:
    return 99.99

