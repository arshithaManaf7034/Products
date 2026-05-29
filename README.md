# AI-Powered Product Management System

## Overview

This project is a Django-based e-commerce product management application that integrates Artificial Intelligence to enhance product information automatically.

When a user adds a new product:

* The system collects product details using a Django ModelForm.
* If the product description is missing, AI generates a professional product description.
* AI predicts a suitable selling price for the product.
* The AI-enhanced product data is then saved to the database.

This project demonstrates Django backend development, form handling, ORM usage, AI integration, prompt engineering, and conditional business logic.

---

## Features

* Product model for storing product information
* Django ModelForm for product submission
* AI-generated product descriptions
* AI-based product price prediction
* Automatic database storage using Django ORM
* Clean separation of AI logic from application views
* Error handling for AI service failures

---

## Technologies Used

* Python
* Django
* OpenAI API
* SQLite (default Django database)

---

## Project Structure

```text
products/
│
├── models.py
├── forms.py
├── views.py
├── ai_service.py
├── urls.py
│
├── templates/
│   ├── add_product.html
│   └── success.html
│
└── migrations/
```

---

## Product Workflow

1. User submits product details.
2. Django validates the form data.
3. If the description field is empty:

   * AI generates a professional product description.
4. AI predicts a suitable market price.
5. Product data is saved to the database.
6. User is redirected to the success page.

---

## AI Integration

### Description Generation

The AI receives:

* Product Name
* Product Category

and generates a professional e-commerce description highlighting features and benefits.

### Price Prediction

The AI analyzes:

* Product Name
* Product Category

and estimates a realistic selling price.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django openai
```

---

## Environment Variables

Create a `.env` file and add:

```text
OPENAI_API_KEY=your_api_key_here
```

---

## Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run the Application

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/add-product/
```

---

## Skills Demonstrated

### Django

* Models
* ModelForms
* Views
* URL Routing
* ORM
* Templates

### Artificial Intelligence

* Prompt Engineering
* AI Content Generation
* AI-Based Price Estimation
* API Integration

### Software Engineering

* Clean Code Structure
* Separation of Concerns
* Error Handling
* Data Persistence

---

## Rubric Mapping

| Requirement               | Implementation                     |
| ------------------------- | ---------------------------------- |
| Product Model Creation    | Product model with required fields |
| ModelForm Usage           | ProductForm                        |
| AI Description Generation | OpenAI API integration             |
| AI Price Prediction       | AI-generated price estimation      |
| View Logic & Saving       | Django view with conditional logic |
| Database Persistence      | Django ORM save operation          |

---

## Future Enhancements

* Product image upload
* Category-based pricing model
* Admin dashboard
* Product search and filtering
* Machine learning-based price prediction using historical product data

---

## Author

Developed as part of a Django and Artificial Intelligence integration project demonstrating automated product enhancement and intelligent data generation.
