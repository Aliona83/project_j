![image from i am response](/readmeImages/iAmResponse.png)

Elegancy jewellery is my fifth and final project, part of the Code Institute, Full Stack Web Developer Course.
The purpose of this project was a build a full-stack site based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django. Stripe handles online test payments and Heroku Postgres as a relational database.


# Table of Contents
## [Jewellery Shop Introduction](#jewllery-shop---introduction)
## [Ux](#ux)
   * [User Stories](#user-stories)
   * [Agile Methodologies](#agile-methodologies)
   * [Database Diagram](#deployment)
   * [Surface](#surface)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   

## [Testing](#testing)
  *  [Link to Testing.md](https://github.com/Aliona83/project_j/blob/main/TESTING.md)

## [Technologies Used](#technologies-used)
 * [Languages Used](#languages)
 * [Frameworks/Libraries](#frameworks---libraries---programs-used)
 
 ## [Deployment](#deployment)
 [Link to Deployment](https://github.com/Aliona83/project_j/blob/main/DEPLOYMENT.md)
 
 ## [Credits](#credits)
   * [Images](#images)
   * [code](#code)
 
## [Acknowledgments](#acknowledgments)

  * [Acknowledgments](#acknowledgments-1)
 

  
# Jewllery Shop - Introduction 

The Jewelry Shop is  an E-commerce shop where users can find and buy jewellery also search for jewelleries by filtering different categories. They can also register by filling in their personal information on the website’s profile page. The application has a good appearance with an easy, clear and concise site navigation. web application built using Python, JavaScript, and Django, designed to provide a seamless and user-friendly platform for buying and selling exquisite jewelery pieces. Whether you are a jewelery enthusiast, a buyer looking for the perfect gift, or an artisan seeking to showcase your creations, this platform caters to all.

[Live project](https://jewelryshop-4c4e9a0b748f.herokuapp.com/)

# UX 

User stories help us understand the needs and expectations of our users. They serve as a basis for defining features and guide our development process. Below are some user stories that represent the different roles and interactions within the Jewelry Project:

## User Stories

 As a Buyer, I want to:
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
         
 As the Register User I want to :

  * As a user, I can use the website on all device sizes so that I can see the same information on small and large devices.
  * As a user, I can use the navigation bar so that I can view all pages of the website easily
  * As a site user, I want to be able to sign up, so that I can have a personal account on the site.
  * As a site user, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.
  * As User I want to been able to add and remove products from my cart
  * As User I want to recieve feedback that my order was processed successfully.
  * As User I want to subscribe to the store newsletters.

 As the Unregistered User I want to:

  * As Unregistered User I want to see the purpose of the site when landing on it
     * Landing page with clear reference to objective of the app
  * As an Unregistered User I want to get a benefit if I register*
    * Information recieved in the registration mail
  * As an Unregistered User, I want to be able to register so that I   can create my account and access to the registered user features
    *  Link for Sign Up in Navbar
  * As an Unregistered User I want to see the detailed information of the jewelleries
    * Jewelleries details page

 Super User Features

 * As a super user, you have access to a range of powerful features that allow you to manage and oversee various aspects of the platform. These features are designed to provide you with control and insights into the system's operations.


* Add Images
Super users have the privilege to add images to the platform. Whether you need to upload new product images, banners, or any other visual content, you can easily do so through the super user interface. This feature helps keep the platform's visuals up-to-date and engaging.

* Delete Images
Should the need arise, you can also delete images as a super user. Whether it's removing outdated content or addressing any other image-related requirements, you have the capability to maintain a clean and relevant image library.

* Edit Images
Super users have the authority to make edits to existing images. Whether you need to crop, resize, or make other adjustments to optimize images for the platform, you can do so effortlessly through the super user interface.

* Order Management

 View All Orders.
As a super user, you can access an overview of all orders placed on the platform. This comprehensive view provides insights into order history, allowing you to monitor sales trends and customer preferences.

* View Custom Orders

In addition to regular orders, super users can specifically view custom orders placed by customers. Custom orders often require special attention, and this feature enables you to track and manage them effectively.

* Contact Us Messages

Super users have access to contact us messages sent by users of the platform. This feature enables you to review user inquiries, feedback, and support requests. You can respond to messages, resolve issues, and maintain a positive user experience.


  ## Agile Methodologies
  
  The Agile Methodology approach was adopted during the development of the Elegancy Jewellery - store. I have utilized GitHub's built-in features such as issue tracking and project management to effectively manage tasks and monitor progress. 

  ![](/readmeImages/agile.png)

 
  [ Here is the link ](https://github.com/Aliona83/project_j/issues)

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
7. Creating Custom Order app

  * Users can access a user-friendly order form where they can specify their custom jewelry requirements.
  * The form includes fields for selecting materials, gemstones, a description of the design, and type of jewellery: ring necklace, earrings.
8. Checkout App

  * Click the button "Secure Checkout" button similar call-to-action on the cart page.
  * Provide the shipping address where you want users to order to be delivered.
  * Users may have the option to save address for future orders.
  * Enter payment details, which typically include credit/debit card information or order payment methods.
  * Users can carefully review the order summary, including, the items, shipping address and total cost.
9. Contact Us App 

  * Users can easily reach out to customer support for assistance with product inquiries, order issues, returns, or any other concerns.
  * Contact Us include a user-friendly contact form that user can fill out.
  * Fields in the form should typically include: the name, email address, message, and contact information. 
10. Stripe payment 
    *  [Stripe](https://stripe.com/ie) has been used in the project to implement the payment system.
    * Payment information is:
        * 4242 4242 4242 4242 (card number)
        * 04/24 (MM/YY)
        * 424 or 242 (CVC)
  ![Stripe](/readmeImages/stripe.png)

   <br><hr>
[🔼 Back to top](#table-of-contents)

  ## Database Diagram    
  [Link Data Shema](https://drawsql.app/teams/aliona/diagrams/jewellery-shop)
   ![](/readmeImages/databaDiagram.png)   
  1. User:
    * Relationships:
        * Users can have a UserProfile (one-to-one).
        * Users can place Orders (one-to-many).
        * Users can create ProductReviews (one-to-many).
        * Users can make CustomJewelleryDesign requests (one-to-many).
        * Users can use the "Contact Us" feature (one-to-many).
  2. UserProfile:
    * Relationships:
        * UserProfile is associated with a User (one-to-one).
  3. Order:
    * Relationships:
       * Orders are placed by Users (many-to-one).
       * Orders consist of OrderLineItems (one-to-many).
  
  4. OrderLineItem:
    * Relationships:
       * OrderLineItems belong to Orders (many-to-one).
       * OrderLineItems refer to Products (many-to-one).
  5. ProductReview:
    * Relationships:
       * ProductReviews are written by Users (many-to-one).
       * ProductReviews are about Products (many-to-one).
  6. Product(Jewellery):
    * Relationships:
       * Products belong to Categories (many-to-one).
       * Products can have ProductReviews (one-to-many).
       * Products can be included in OrderLineItems (many-to-many through Orders).
  7. CustomJewelleryDesign:
    * Relationships:
       * CustomJewelleryDesign requests are made by Users (many-to-one).
  8. ContactUs:
    * Relationships:
       * "Contact Us" messages can be sent by Users (many-to-one).
  9. Category:
    * Relationships:
       * Products belong to Categories (many-to-one).

  ## Surface

  * Home Page Features Description 

  1. Logo![Logo](./readmeImages/logo.png)
   * Logo: The home page prominently displays shop logo at the top, by clicking on the logo users will be able to return to homepage.

  2. Navigation Bar ![Navigation bar](./readmeImages/navigation.png)

   * Navigation Bar with Categories:A navigation bar provides easy access to various product categories, making it simple for users to browse and find the products they're interested in.
    ![Burger Menu](./readmeImages/burgerMenu.png)
   * Mobile navigation(Burger Menu): on mobile screens,a convenient burger menu icon is provided, which, when tapped, opens a dropdown menu with navigation options.  This ensure a responsive and user-friendly experience on smaller devices.
   * Clicking the "Home" button in the navigation bar takes users back to the homepage from any pages on the website, ensuring smooth navigation.

  3. Profile ![Profile](./readmeImages/myAccount.png)  
   * User can create and personalize their profiles,and their profile logo are displayed in the right side of screen.
   * The login and logout buttons are conveniently located in the header, allowing users to securely access their accounts or log out when needed.
    ![Profile.Mobile](./readmeImages/profile.png)

  4. Shop Now Button ![Shop Now](./readmeImages/shopNow.png)
   * A prominent "Shop Now" button is strategically placed to encourage users to start shopping immediately upon viting the site.

  5. Features ![Features](./readmeImages/features.png)  
   * The home page features a dedicated section showcasing the latest arrivals. Users can quickly see and explore the newest products store has to offer. Everytime user will be update home page up features "New Arrivals " will be change products.

  6. Footer ![Footer](/readmeImages/footer.png)  
   * At the button of the page, a comprehensive footer contains various links, such as Facebook, LinkedIn, Twitter, GitHub, Google, and Instagram.
    ![Newsletter](/readmeImages/newsletter.png)
   * Users can subscribe to newsletter directly from the footer . This allows you to build a mailing list and keep customers informed about promotions,updates, and news related to your brand.
   * Quick links: Home Page, LogIn, Contact Us, Shop Now. Clearly labelled quick links eliminate confusion and provide users with a straightforward path to essential sections of the website. Users can easily understand where each link will take them.
  7. Search 
  ![Search](./readmeImages/searchBar.png)
   * A prominent search bar is located in the navigation bar, allowing users to quickly search for specific products or content on your website. This feature ennhance the user's ability to find what they need efficiently. 
  8. Social Media
  ![Social Media](/readmeImages/facebookPage.png)
    * Here I have made a Social Media Marketing Page for the Elegancy Jewellery store. It is a fantastic way to boost and increase engagement within the business and in increasing sales. Here is the screenshot of the whole page available to anyone.

  9. Admin
  ![Admin](/readmeImages/admin.png)
    * Admin page allows site owners to exercise administrative control over; users, orders, email addresses, jewelleries, categories.
  
  10. Toast Notifications and Alert Messages

  * In this project, we have implemented a range of toast notifications and alert messages to enhance the user experience. These notifications provide important feedback and information to users during various interactions with the platform. Below, you'll find descriptions of the different types of notifications and when they are displayed.
    1. Login Success

   Upon a successful login, a personalized notification toast is displayed to greet the user by their name. This personalization helps create a more engaging and connected user experience. The notification is designed to be responsive, ensuring a consistent and visually appealing appearance across different screen sizes and devices.
 ![](/readmeImages/login.png)

   2. Logout

   When a user logs out of their account, a confirmation toast is shown to inform them that they have been successfully logged out. This helps users confirm that their action was successful and provides a smooth transition out of their session.
  
   ![](/readmeImages/logout.png)

  3. Success Message - Delete

  * After successfully deleting an item or performing a similar action, a success notification toast is shown to confirm the action's completion. This positive feedback reassures users that their requested action was carried out successfully.

  ![](/readmeImages/delete.png)

  4. Error Messages

  * I've implemented error toast notifications to alert users when they encounter issues or input errors. These error messages are displayed when, for example, a user submits a form with missing or invalid data. Clear and informative error messages help users understand and address the issues at hand.

 ![](/readmeImages/error.png)

 4. Alert Messages

 * In situations where email confirmation is required, we display an alert message to prompt users to confirm their email address. This message provides clear instructions and encourages users to complete the necessary steps for email verification.

 ![](/readmeImages/alert.png)


  * Product Page Features

  1. 
  ![Products](/readmeImages/products.png) 
   * Main Jewellery page offer products on large resolutions in a row of three. Images are large to attract the user's attention, and clicking the image will redirect the user to the product detail page. 
   * The product title and description provide essential information about the product.
  2.
  ![Product Details](/readmeImages/prodoctDetailsPage.png)
   * Detailed specifications and additional information about the product are provided.
   * Users can learn about materials, dimensions, care instructions, and more.
   * Users can easily add the product to their shopping cart for future purchase.
  3. 
  ![Sort By](/readmeImages/sortBy.png)
   * The "Sort By" tool is a powerful feature that empowers users to customize how they view and interact with our extensive collection of jewelry products. It provides flexibility and control over the product listing, allowing users to tailor their browsing experience according to their needs and preferences.
  4. 
  ![Pgination](/readmeImages/pagination.png)
   * Pagination is a user interface feature that enhances the browsing experience for users when navigating through extensive lists of jewelry products. It ensures that the product listings remain organized and manageable, enabling users to explore our diverse collection with ease.
  5. 
  ![Arrow Up](/readmeImages/arrowUp.png)

  * Cart/ Shopping Bag 

  1. 
  ![Toasts](/readmeImages/bag.png)

   * Almost all actions provide feedback to the user via the bootstrap toasts written to provide user feedback.
   * Users shopping can view the current items within the bag and total cost. The discount is visible and the user is told how much they need to spend to get discount.
  2. 
  ![Shopping bag](/readmeImages/shoppingBag.png) 
   * The shopping bag page is fully responsive, showing users a picture of the item, name, price per unit, and total price.
   * Users can also choose to increase/decrease the number of items in their bag, click the update button to have the prices update.
   * User can click the remove link and have all the items within the bag removed, regardless of quantity.
   * At the bottom of the page user can find the cost of the bag, cost of delivery, the total and how much they must spend to be eligible for free delivery.
  3. 
  ![Checkout Overlay](/readmeImages/spinner.png)
    * Users who checkout will see a simple overlay with a spinning icon while the payment is processed.

  * Jewellery Custom Form
  1. 
  ![Custom Form](/readmeImages/customForm.png)
    * Once user find a base design he likes, click on create form to start customizing. User can choose the type of metal, gemstones, engraving, and any other personalized details add image.

  2. ![Submit success page](/readmeImages/successSubmit.png)
     * After you submit a form on our platform, you will receive a clear and reassuring success message to confirm that your submission was successful. This message serves as confirmation that your Form Submitted Successfully! Thank you for reaching out to us. We have received your request and will process it promptly. If you need any further assistance, please don't hesitate to contact us."

  * Contact Us Page

  ![Contact form](/readmeImages/contacUs.png)

  * Our "Contact Us" page is designed to provide user with a convenient and efficient way to get in touch with our customer support team. Whether you have questions, need assistance, or want to share feedback, this page is your gateway to direct communication with us.
    
     
  * Profile   
  1. 
  ![Profile SuperUser](/readmeImages/superUser.png)

  The application has two types of users: Superusers and Regular Users, each with different capabilities and access levels.

  * Product Management

  ![Edit/Delet](/readmeImages/editDelete.png)
         
  * Edit Products: Superusers can edit existing product details, including name, description, and price.

  * Delete Products: Superusers can remove products from the system.

   * Add New Products: Superusers can add new products to the system, specifying their details.

  * Customer Interaction
  View Customer Contact Us Forms: Superusers can access and view contact us forms submitted by customers.

  * View Customer Order History: Superusers can view the order history of all users, including order details and statuses.

  * View Custom Order Forms: Superusers can access and view custom order forms submitted by users.

2. 
  ![Profile User](/readmeImages/user.png)

  * Profile
      *  Regular users can update their profile information, including their personal details.
      *  Regular users can access their order history, including order details and statuses.
  ![Delete Order](/readmeImages/deleteOrder.png) 

      * Delete Orders: Regular users can delete orders they no longer need from their order history.
      * Send Custom Order Forms: Regular users can submit custom order forms to request specific products or services.
      * Complete Contact Us Form: Regular users can submit inquiries and messages using the contact us form.

   <br><hr>
[🔼 Back to top](#table-of-contents)
## Structure
  1. Colors

     * This website's design incorporates a harmonious colour palette to create a visually appealing and user-friendly experience. The following colours are used consistently across the site:

  ![Background colours](/readmeImages/backgroundColour.png)
    * This pallet colours had been used for text.

  ![Text colours](/readmeImages/textColour.png)
  2. Images

  * All images used on our website are sourced from [Pexels](https://www.pexels.com/), a high-quality and free stock photos platform. We believe in using high-quality images to enhance the overall visual experience and maintain a professional appearance.

  3. Font Selection 

     * One fonts were chosen with Google Fonts to be used across the entire site.

     * The chosen fonts were 'Lato', with serif as back up fonts for lists, forms, buttons and paragraphs.

##  Skeleton  

  * Wireframes created with Balsamiq

  <details>
   <summary>Click to see more</summary>

  * Home Page

  ![Home Desktop](/readmeImages/HomePage.png)
  ![Home Mobile](/readmeImages/homeMobile.png)
    
  * Jewellery Page

  ![Desktop](/readmeImages/jewlleryPage.png)

  ![Mobile](/readmeImages/jewelleyMobile.png)

  * Jewellery Details Page

  ![Desktop](/readmeImages/productDetails.png)

  ![Mobile](/readmeImages/detailProductMobile.png)

  * Add To Bag Page

  ![Desktop](/readmeImages/addToBag.png)

  ![Mobile](/readmeImages/addBagMobile.png)

  * Checkout Page

  ![Desktop](/readmeImages/checkoutView.png)

  ![Mobile](/readmeImages/checkoutMobile.png)

  * Payment Page

  ![Desktop](/readmeImages/payment.png)

  ![Mobile](/readmeImages/paymnet.png)

  * Custom Order Page

  ![Desktop](/readmeImages/customOrderForm.png)

  ![Mobile](/readmeImages/customFormMobile.png)

  * Contact Us Page

  ![Desktop](/readmeImages/customOrderForm.png)

  ![Mobile](/readmeImages/contactUsMobile.png)
</details>
  

## Testing
[Link to TESTING.md](https://github.com/Aliona83/project_j/blob/main/TESTING.md)

## Technologies Used
 
##  Languages
  * Javascript
  * Python
  * HTML
  * CSS

## Frameworks - Libraries - Programs Used

   * [Django](https://docs.djangoproject.com/en/4.2/topics/pagination/): Main python framework used in the development of this project
   * [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): Authentication library used to create user accounts
   *[Heroku](https://www.heroku.com/github-students)- Used as the cloud-based platform to deploy the site.
   * [GitHub](https://github.com/) - Used for version control and agile methodology.
   * [PostgreSQL](https://www.postgresql.org/)- Used as the database for this project.
   * [W3C](https://validator.w3.org/) - Used for HTML & CSS Validation.
   * [Font Awesome ](https://fontawesome.com/)- Used for icons on the home page and stars on the About page.
   * [Jshint](https://jshint.com/)- Used to validate the JavaScript page.
   * [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- Used to manage Django Forms.
   * [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)- CSS used for developing responsiveness and styling the website.

  ## Deployment
   [Link to DEPLOYMENT.md](https://github.com/Aliona83/project_j/blob/main/DEPLOYMENT.md)
   
   ## Credit 
    
  ### Images 
  * Images used in this project were sourced from [Pexels](https://www.pexels.com/). 

  ### Code 
  * The majority of the code structure and concepts were inspired by the [Code Institute](https://www.codeinstitute.net/) walkthrough project "Boutique Ado." 

  * Mailchimp and form code was used for the signup newsletter in the footer of the site [Mailchimp](https://mailchimp.com/landers/email-marketing-platform/?ds_c=DEPT_AOC_Google_Search_ROET_EN_Brand_Retarget_Exact_MKAG_T2&gclid=Cj0KCQjw9rSoBhCiARIsAFOiplm2rczG5luenH2Zi0poWx93RjWRFSFDxfIki7eXWVZgPEKvVw8ZhIwaAvwtEALw_wcB&gclsrc=aw.ds)
  
  ### Django Documentation
   
   * Django have amazing documentation with a tutorial project and in depth explanations on core components.
   * [Django](https://docs.djangoproject.com/en/3.2/)
  
  ## Acknowledgments

  1. [CodeCademy](https://www.codecademy.com/)

  * I was having a course it help me be more confident with creating object, classes. "Learn Object Oriented Programming with Python.

  2. [Youtube](https://www.youtube.com/watch?v=YZvRrldjf1Y&t=12808s)

  3. [Stackoverflow](https://stackoverflow.com/tags)

  4. [Slack](https://slack.com/intl/en-ie/)
     * Thanks to everyone in Slack who replied to my messages and their help. 
  5. [Code Institute](https://codeinstitute.net/ie/)
     * Code institute for the amazing Tutors on the course. It was very good support.
     * For amazing help with the Boutique Ado walkthrough project.
  6. Family. Who supported me all this time and believed in me even at the moment when I was losing faith in myself that I could get through this. 

  7. [Google](https://www.google.com/)
  8. [Boostrap Documentations](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
     
<br><hr>
[🔼 Back to top](#table-of-contents)


