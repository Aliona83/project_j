
# Table of Contents
## [Jewellery Shop Introduction](#jewllery-shop---introduction)
## [Ux](#ux)
   * User Stories
   * Agile Methodologies
   * The Scope(?)
   * Structure(colors, images, fonts WhishList, UserProfile, Order..)
   * Skeleton(Wireframes, Shopping Bag Wireframes, All Products Wireframes, Account page, Checkout Page ....)
   * Surface(Features: Nav bar, Store Page, Search, Toast,Shopping bag )

## Testing 
  * Link to Testing.md 

## Technologies Used
 * Languages Used
 * Frameworks/Libraries 
 
 ## Deployment
 * Creating a Clone 
 * Forking this repository
 * Heroku Deployment
 * AWS S3 Bucket setup
 * AWS IAM(Identity and Access Managenent) setup ) 
 * Connecting Heroku to AWS S3
 
 ## Credits
  * Product images
  * Code
  * Bootstarp
  * Django Documentation

## Aknowledgements
  * Linkedin
  * GitHub
  * youtube
  
# Jewllery Shop - Introduction 
The Jewelry Shop is  an E-commerce shop where users can find and buy jewellery also search for jewelleries by filtering different categories. They can also register by filling in their personal information on the website’s profile page. The application has a good appearance with an easy, clear and concise site navigation. web application built using Python, JavaScript, and Django, designed to provide a seamless and user-friendly platform for buying and selling exquisite jewelery pieces. Whether you are a jewelery enthusiast, a buyer looking for the perfect gift, or an artisan seeking to showcase your creations, this platform caters to all.

(Add live project here)
(Add image of project from I am response)

# UX 
User stories help us understand the needs and expectations of our users. They serve as a basis for defining features and guide our development process. Below are some user stories that represent the different roles and interactions within the Jewelry Project:

## As a Buyer, I want to:
  * Provide buyers with an extensive range of jewelry options.
  * Categorize jewelry for easy navigation, such as necklaces, rings, and bracelets, by type of material: gold, silver etc.
  * Implement filters to refine search results by material, style, price, and more.
  * Easily access a "New Arrivals" section on the home page to stay updated with the latest additions.
  * Display high-quality images of each product.
  * Include product descriptions, product categories, materials, rates and prices.
  * Allow buyers to click on each product to view all details.
  * Ensure a user-friendly and responsive website or app design.
  * Enable easy account creation and login.
  * Provide a streamlined shopping cart and checkout process. 
  * As a logged-in user, I want to be able to add products to my wishlist, so that I can view those products later.
  * As a logged-in user, I was to be able to remove products from my wishlist, so that my wishlist is only full of products I want to be saved.
  * Allow buyers to access a profile page where they can submit a form to order custom-made jewellery.  
  * To see a history of all submitted custom-made orders.
  * Enable buyers to easily access and review their order history. 
  * As a buyer, I want to provide secure payment options for customers, such as integrating with secure payment gateways (e.g. Stripe)
         
## As the Register User I want to :

  * As a user, I can use the website on all device sizes so that I can see the same information on small and large devices.
  * As a user, I can use the navigation bar so that I can view all pages of the website easily
  * As a site user, I want to be able to sign up, so that I can have a personal account on the site.
  * As a site user, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.
  * As User I want to been able to add and remove products from my cart
  * As User I want to recieve feedback that my order was processed successfully.
  * As User I want to subscribe to the store newsletters

## As the Unregistered User I want to:

1. As Unregistered User I want to see the purpose of the site when landing on it
    * Landing page with clear reference to objective of the app
 2. As an Unregistered User I want to get a benefit if I register*
    * Information recieved in the registration mail
 3. As an Unregistered User, I want to be able to register so that I   can create my account and access to the registered user features
    *  Link for Sign Up in Navbar
  4. As an Unregistered User I want to see the detailed information of the wares
    * Ware's details page


  ## Agile Methodologies
  
  The Agile Methodology approach was adopted during the development of the Elegancy Jewellery - store. I have utilized GitHub's built-in features such as issue tracking and project management to effectively manage tasks and monitor progress.
    1. Epic - Project Setup
      * Install Django framework that provides tools and libraries for building web application.
      * Install Django Allauth, it allaows us to manage user authentication, registration,and account management seamlessly.
      * Crispy Forms this Django package that will help us style our forms easily and effficiently.
      * Create jewelry_shop app.
      * Create superuser
    2. Epic - Homepage and Navigation Setup 
      * Navigation bar. Will provide easy access to different sections of application, easy to navigate on mobile screens.
      * Implement categories links in the navigation bar for organized content access, also include a home button to quickly return to the home page. 
      * Enhance the aesthetic appeal of the homepage with background image. 
      * Implement a search bar to enable to search for products or content.
      * Create cart functionality for user to add items they want to purchase.
      * Populate the homepage with fixture data to showcase new arrivals.
      * Implement user authentication with login and logout buttons.
      * Create footer section with the links and newsletter subcription form.
    3.   Implementing Login and Logout 
      * Create login, registration and logout pages.
      * Create forms for user login, registration and logout, ensuring data validation and security. 
      * Implement email configuration for the user accounts to verify the authenticity of email addresses during registration.
    4. Creating a Product App
      * Create Product app
      * Design and create templates for displaying products,products_details.
      * Populate your database with fixture data conatining product information, including images and categories.
      * Implement functionality to cotegorize products and allow users to filter products by categories. Implement a search bar that enables users to search for specific products based on keywords. Also implement sorting options(by price, name, and letters..)
      * Add pagination to the product listings to ensure that large catalogues can be easily navigated.
    5. Creating a Cart App
      * Create a Cart App, and add models, views and templates. 
      * Implement cart functionality to add, update and remove items from the cart.
      * Calculate the total cost of items in the cart, including discounts.
      * Develop checkout process,including user authentication,address input and payment process.
      * Create templates and view to display order confirmation details after a successful purchase.
    6. Creating a Profile App
      * Implement functionality to allow users to view and update their personal information and preferences.
      * Integrate user authentication to ensure that users can access and manage their profile.
      Extend the profile app to include a section where users can view their order history.
      * Create a custom form whithin the profile app that allows users to order custom jewellery, either for themself or friends also can view their custom jewellery order.
    7. 
# Deployment
[Link to DEPLOYMENT.md](https://github.com/Aliona83/project_j/blob/main/DEPLOYMENT.md)

# Technologies Used
 
 ## Languages
  * Javascript
  * Python
  * HTML
  * CSS

  ## Frameworks - Libraries - Programs Used

   * Django: Main python framework used in the development of this project
   * Django-allauth: Authentication library used to create user accounts
   * Heroku - Used as the cloud-based platform to deploy the site.
   * GitHub - Used for version control and agile methodology.
   * PostgreSQL Used as the database for this project.
   * W3C - Used for HTML & CSS Validation.
   * Font Awesome - Used for icons on the home page and stars on the About page.
   * Font Awesome - Used for icons on the home page and stars on the About page.
   * Jshint - Used to validate the JavaScript page.
   * Crispy Forms Used to manage Django Forms.
   * Bootstrap: CSS used for developing responsiveness and styling the website.

   ## Credit 




<!-- Features
User Authentication: The application offers a secure and robust user authentication system, allowing users to create accounts, log in, and manage their profiles.

Product Listings: Users can browse through a wide range of jewelry items, beautifully displayed with detailed descriptions and high-quality images.

Search and Filtering: A powerful search and filtering functionality enable users to quickly find specific jewelry items based on various parameters like type, material, gemstone, and price range.

Shopping Cart: Users can add their favorite jewelry pieces to the shopping cart and proceed to checkout seamlessly.

Payment Integration: The project integrates a secure payment gateway, enabling users to make safe and convenient online transactions.

Order Tracking: Once a purchase is made, users can track their orders and receive notifications on the status of their shipments.

Seller Dashboard: Artisans and sellers have access to a dedicated dashboard, where they can manage their products, view order details, and track their earnings.

Reviews and Ratings: Users can leave reviews and ratings for products, fostering a community-driven platform and helping others make informed purchasing decisions.

Wishlist: Users can create a wishlist of their desired jewelry items for future reference.

Admin Panel: The application includes a comprehensive admin panel that facilitates easy management of products, user accounts, and order processing.

Tech Stack
Python: The project leverages the power and versatility of Python to handle the backend logic and database operations.

JavaScript: JavaScript is used to create dynamic and interactive user interfaces, enhancing the overall user experience.

Django: As a high-level Python web framework, Django provides a robust foundation for building secure and scalable web applications.

HTML/CSS: The front-end is crafted using HTML and CSS, ensuring a visually appealing and responsive design.

Database: The project employs a relational database (e.g., PostgreSQL, MySQL) to store user information, product details, and order history.

Installation
To set up the Jewelry Project locally, follow these steps:

Clone the repository from [GitHub Repo URL].

Install Python [version] and pip on your system.

Create a virtual environment and activate it.

Install the required Python packages using the requirements.txt file.

Set up the database and run migrations.

Start the development server and access the application via the provided URL.

Contributing
We welcome contributions from the community to improve the Jewelry Project. If you encounter any bugs, have suggestions, or wish to add new features, feel free to submit a pull request or raise an issue on our GitHub repository.

License
The Jewelry Project is licensed under [License Type]. Please refer to the LICENSE file for more details.

Acknowledgments
We extend our gratitude to the open-source community for providing valuable tools and resources that have contributed to the development of this project.

Contact
For any inquiries or support, please contact us at [contact@example.com].

Note: Replace placeholders such as [GitHub Repo URL], [version], [License Type], and [contact@example.com] with the actual values specific to your project. Provide clear instructions for installation and contribution guidelines if applicable.


User storie

User stories help us understand the needs and expectations of our users. They serve as a basis for defining features and guide our development process. Below are some user stories that represent the different roles and interactions within the Jewelry Project:

As a Buyer, I want to:

c
View detailed product descriptions, including materials, gemstones, and sizes.
Add items to my shopping cart and proceed to checkout securely.
Create a wishlist of jewelry items for future reference.
Leave reviews and ratings for products I have purchased.
Track the status of my orders and receive notifications on shipment updates.
Have an intuitive and user-friendly interface to easily navigate and interact with the website.
As an Artisan/Seller, I want to:

Register and create an account with my profile details.
Upload images and descriptions of my jewelry pieces to showcase my work.
Manage my product listings, including adding new products and updating existing ones.
View and track the status of orders placed for my products.
Receive notifications when a buyer purchases one of my items.
Have access to a seller dashboard with insights into sales and earnings.
Interact with buyers by responding to reviews and inquiries.
As an Administrator, I want to:

Manage user accounts, including authentication and authorization.
Monitor and moderate user-generated content, such as reviews and ratings.
Have control over the product listings and the ability to add, edit, or remove products.
View sales and revenue reports for the entire platform and individual sellers.
Resolve disputes between buyers and sellers if they arise.
Receive alerts for any critical system issues or security concerns.
Access an admin panel with an intuitive interface for managing various aspects of the platform.
As a Guest User, I want to:

Have the option to register an account or log in to access additional features.
View the website's landing page, showcasing the platform's unique selling points.
Browse through a limited selection of featured jewelry items without logging in.
Be informed about the benefits of creating an account, such as wishlist creation and personalized recommendations.
Access the website from any device, ensuring a responsive and mobile-friendly design.
As a Potential Seller, I want to:

Easily find information on how to become a seller on the platform.
Understand the terms and conditions for selling jewelry through the website.
Contact the administrators or support team for assistance with the seller onboarding process.
Receive guidance on setting competitive prices and optimizing product listings.
These user stories serve as a foundation for defining the functionalities and requirements of the Jewelry Project. They will be used in conjunction with Agile methodologies to prioritize features, plan sprints, and ensure the development aligns with the needs of our users.






Regenerate
Send a message

Free Research Preview. ChatGPT may produce inaccurate information about pe
 -->
