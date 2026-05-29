from django.shortcuts import render, redirect

from .forms import ProductForm
from .ai_service import (
generate_product_description,
predict_product_price
)

def add_product(request):


if request.method == "POST":

    form = ProductForm(request.POST)

    if form.is_valid():

        product = form.save(commit=False)

        if not product.description:
            product.description = generate_product_description(
                product.name,
                product.category
            )

        product.price = predict_product_price(
            product.name,
            product.category
        )

        product.save()

        return redirect("success")

else:
    form = ProductForm()

return render(
    request,
    "add_product.html",
    {"form": form}
)


def success(request):
return render(request, "success.html")
