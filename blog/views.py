from django.http import Http404
from django.shortcuts import redirect, render

PRODUCTS = [
    {
        "id": 1,
        "name": "Galaxy Pro X",
        "price": 899,
        "old_price": 1099,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=80",
        "badge": "Best Seller",
        "category": "Smartphones",
        "description": "A premium smartphone built for creators and busy professionals, with a vibrant display and all-day battery life.",
        "highlights": ["6.8-inch OLED screen", "128GB storage", "Triple camera system", "Fast wireless charging"],
    },
    {
        "id": 2,
        "name": "AeroBook 14",
        "price": 1299,
        "old_price": 1599,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=900&q=80",
        "badge": "New",
        "category": "Laptops",
        "description": "Ultra-light performance laptop designed for streamlined work, entertainment, and everyday productivity.",
        "highlights": ["14-inch display", "16GB RAM", "AI-powered performance", "All-day battery"],
    },
    {
        "id": 3,
        "name": "Pulse Headset",
        "price": 199,
        "old_price": 249,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=900&q=80",
        "badge": "Hot",
        "category": "Audio",
        "description": "Immersive wireless audio with crisp details, deep bass, and a comfortable over-ear fit for long listening sessions.",
        "highlights": ["Noise cancellation", "40-hour battery", "Fast pairing", "Travel case included"],
    },
    {
        "id": 4,
        "name": "Nexa Speaker",
        "price": 349,
        "old_price": 429,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1518444065439-e933c06ce9cd?auto=format&fit=crop&w=900&q=80",
        "badge": "Popular",
        "category": "Home Deals",
        "description": "A compact speaker that fills your room with warm, balanced sound and seamless modern styling.",
        "highlights": ["360° sound", "Water resistant", "Bluetooth 5.3", "Voice assistant ready"],
    },
]

CATEGORIES = [
    {"title": "Smartphones", "icon": "📱", "description": "Premium devices and accessories."},
    {"title": "Laptops", "icon": "💻", "description": "Powerful productivity for work and play."},
    {"title": "Audio", "icon": "🎧", "description": "Immersive sound and everyday comfort."},
    {"title": "Home Deals", "icon": "🏠", "description": "Upgrade your space with modern essentials."},
]

BENEFITS = [
    {"title": "Free shipping", "description": "On all orders above $100"},
    {"title": "Secure payments", "description": "Protected checkout experience"},
    {"title": "Easy returns", "description": "30-day hassle-free returns"},
    {"title": "Customer care", "description": "Friendly support, always available"},
]

TESTIMONIALS = [
    {"name": "Nia H.", "quote": "The shopping experience felt premium from start to finish. Delivery was fast and the product quality exceeded expectations."},
    {"name": "Marcus T.", "quote": "I finally found a storefront that feels modern, trustworthy, and genuinely easy to use on mobile."},
]


def home(request):
    return render(
        request,
        "home.html",
        {
            "categories": CATEGORIES,
            "featured_products": PRODUCTS,
            "benefits": BENEFITS,
            "testimonials": TESTIMONIALS,
        },
    )


def product_detail(request, product_id):
    product = next((item for item in PRODUCTS if item["id"] == product_id), None)
    if product is None:
        raise Http404("Product not found")
    related_products = [item for item in PRODUCTS if item["id"] != product["id"]][:3]
    return render(request, "product_detail.html", {"product": product, "related_products": related_products})


def cart_view(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0
    subtotal = 0

    for product_id, quantity in cart.items():
        product = next((item for item in PRODUCTS if item["id"] == int(product_id)), None)
        if product:
            item_total = product["price"] * quantity
            subtotal += item_total
            cart_items.append({"product": product, "quantity": quantity, "total": item_total})

    total = subtotal
    return render(request, "cart.html", {"cart_items": cart_items, "subtotal": subtotal, "total": total})


def add_to_cart(request, product_id):
    product = next((item for item in PRODUCTS if item["id"] == product_id), None)
    if product is None:
        raise Http404("Product not found")

    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    request.session.modified = True
    return redirect("cart")


def checkout_view(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = next((item for item in PRODUCTS if item["id"] == int(product_id)), None)
        if product:
            item_total = product["price"] * quantity
            total += item_total
            cart_items.append({"product": product, "quantity": quantity, "total": item_total})
    return render(request, "checkout.html", {"cart_items": cart_items, "subtotal": total, "total": total})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def reports(request):
    return render(request, "home.html")


def analytics(request):
    return render(request, "home.html")
