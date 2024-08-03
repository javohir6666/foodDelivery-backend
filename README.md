# Food Delivery API

## Overview

The Food Delivery API is a backend service for managing a food delivery system. It provides endpoints for managing food types, categories, food items, baskets, orders, and feedback. The project is built using Django REST Framework and includes features such as user authentication and API documentation.

## Features

- **Food Types**: Manage different types of food.
- **Categories**: Organize food items into categories.
- **Food Items**: Manage individual food items.
- **Basket**: Manage user baskets for storing selected food items.
- **Orders**: Create and manage orders based on user baskets.
- **Feedback**: Collect feedback on orders from users.
- **Authentication**: User registration and login using JWT tokens.
- **API Documentation**: Interactive API documentation with Swagger and ReDoc.

## Technologies

- Django
- Django REST Framework
- `drf-yasg` for API documentation
- SQLite (default)

## Installation

### Clone the Repository

```bash
git clone https://github.com/javohir6666/food-delivery-api.git
cd food-delivery-api
Set Up a Virtual Environment
bash
Копировать код
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash
Копировать код
pip install -r requirements.txt
Configure the Database
Update the DATABASES setting in food_delivery/settings.py to match your database configuration.

Run Migrations
bash
Копировать код
python manage.py migrate
Create a Superuser
bash
Копировать код
python manage.py createsuperuser
Run the Development Server
python manage.py runserver
API Endpoints
Authentication
POST /api/auth/register/: Register a new user.
POST /api/auth/login/: Obtain a JWT token for authentication.
Food Types
GET /api/food/food-types/: List all food types.
POST /api/food/food-types/: Create a new food type.
Categories
GET /api/food/categories/: List all categories.
POST /api/food/categories/: Create a new category.
Food Items
GET /api/food/food-items/: List all food items.
POST /api/food/food-items/: Create a new food item.
Baskets
GET /api/orders/baskets/: List all baskets.
POST /api/orders/baskets/: Create a new basket.
Basket Items
GET /api/orders/basket-items/: List all basket items.
POST /api/orders/basket-items/: Add an item to a basket.
Orders
GET /api/orders/orders/: List all orders.
POST /api/orders/orders/: Create a new order.
Feedback
GET /api/orders/feedbacks/: List all feedback.
POST /api/orders/feedbacks/: Create new feedback.
API Documentation
Interactive API documentation is available at:

Swagger UI: http://localhost:8000/api/docs/
ReDoc: http://localhost:8000/redoc/

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or issues, please contact:

Author: Javohir
Email: javohir6666@gmail.com