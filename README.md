
# FoodMozo(Multi-vendor Restaurant Marketplace website) 

# live links 
https://foodmozo.quest/
or
https://ec2-65-1-94-96.ap-south-1.compute.amazonaws.com


A brief description of what this project does and who it's for
This repository contains the source code for a comprehensive food delivery platform developed using Django, PostgreSQL, AJAX, and a host of other technologies.



## Table of Content
1.Features
2.Technologies Used
3.Setup and Installation
4.Usage
5.Contributing
6.License 
## Features

The platform includes a variety of features:

1.User and Vendor Registration and Authentication: Custom Django user model and secure token verification.

2.Admin Approval and Dashboard: Vendors require admin approval for registration, with a unique dashboard for each vendor.

3.Menu Builder: Allows vendors to manage food items and categories with full CRUD functionalities.

4.Dynamic Marketplace and Responsive Cart: Users can browse items, add to cart, and checkout without page refreshes.

5.Smart and Location-based Search: Integrated Google Autocomplete for address fields and location-based search functionalities.

6.Dynamic Business hours and Tax Calculation Modules: Businesses can set their operating hours and tax rates.

7.Customers App and Profile Building: User profile management and order tracking.

8.Payment Gateway Integration: Secure transactions with PayPal and Razorpay.

9.ManyToMany Relationship & Vendor Dashboard: Efficient data management with custom middleware for tracking revenue metrics.

10.Responsive Design: Mobile-friendly interface for enhanced user experience across devices.

11.Deployment: Application successfully deployed on AWS using NGINX and Gunicorn.
## Setup and Installation

1. Clone the repository 
```bash
git clone https://github.com/Nit89/FoodMozo.git
```

2. Navigrate to the working directory 
```bash
`cd FoodMozo`
```
3. Open the project from the code editor `code .` or `atom .`
4. Create virtual environment `python -m venv env`
5. Activate the virtual environment `source env/Scripts/activate`
6. Install required packages to run the project `pip install -r requirements.txt`
7. Rename _.env-sample_ to _.env_
8. Fill up the environment variables:
    _Generate your own Secret key using this tool [https://djecrety.ir/](https://djecrety.ir/), copy and paste the secret key in the SECRET_KEY field._

    _Your configuration should look something like this:_
    ```sh
    SECRET_KEY=47d)n05#ei0rg4#)*@fuhc%$5+0n(t%jgxg$)!1pkegsi*l4c%
    DEBUG=True
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=youremailaddress@gmail.com
    EMAIL_HOST_PASSWORD=yourStrongPassword
    EMAIL_USE_TLS=True
    ```
    _Note: If you are using gmail account, make sure to [use app password](https://support.google.com/accounts/answer/185833)_
9. Create database tables
    ```sh
    python manage.py migrate
    ```
10. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
11. Run server
    ```sh
    python manage.py runserver
    ```
12. Login to admin panel - (`http://127.0.0.1:8000/admin/`)
13. Add categories, products, add variations, register user, login, place orders and EXPLORE SO MANY FEATURES



## API Reference

#### Get all items

```http
   POST /v1/payments/payment
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `intent` | `string` | **Required**. Required. Payment action |

For full details and other endpoints, please refer to the PayPal API documentation.
#### Get item

```http
  POST /v1/orders
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `amount`      | `string` | **Required**.The total amount to be paid |

#### Capture a payment

 POST /v1/payments/:id/capture

 | Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `amount`      | `string` | **Required**.The total amount to be paid |



## Demo

![me](https://github.com/Nit89/FoodMozo/blob/master/demo%20(1)%20(1).gif)


## Authors

- [@niteshsingh](https://github.com/Nit89)


## Tech Stack

**Client:** HTML ,CSS, JAVASCRIPT

**Server:** Django

**others**
PostgreSQL,
AJAX,
AWS,
NGINX,
Gunicorn,
PayPal API,
Razorpay API,
Google Maps API


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

We love to receive contributions from the community! There are many ways to contribute, here are a few:


Submit bugs and feature requests.

Improve our documentation or translate it to another language.

Write tutorials or blog posts about the project.

Fix open issues or add new features.


## FAQ

Q1: I'm getting an error when trying to install the project. What should I do?

A: Ensure that you have all the prerequisites installed on your machine. If you still face issues, try to find a similar issue in the 'Issues' section of this repository. If you don't find anything helpful, you can open a new issue with a description of the problem and the error message you are getting.

Q2: How can I contribute to the project?

A: There are many ways to contribute to the project. You can improve the documentation, fix bugs, add new features, or even write blog posts or tutorials about the project. Check the Contribution Guidelines for more details.

Q3: I have a feature request. Where should I suggest it?

A: We love to hear your ideas! Please open an issue in the 'Issues' section of this repository and tag it as a 'Feature Request'. Describe your idea in as much detail as you can.


