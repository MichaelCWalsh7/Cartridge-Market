## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) 
    -   Results:
        - Preamble; One persistent html error is the form as a child of a ul, which because it appears on the mobile nav, will appear on every page. While unfortunate, the search bar appearing as a dropdown using the bootstrap dropdown classes (which necessitates a ul) is I feel a worthy break from conventions in this case. 
        - [All games](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Fproducts%2F)
        - [All Storefronts](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Fstorefront%2Fall_storefronts%2F)
        - [Developer page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Fproducts%2Fpublisher%2FNintendo%2F)
        - [Game Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Fproducts%2F1%2F)
        - [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Fprofile%2F)
        - [Storefront Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Fstorefront%2Fstorefronts%2F5)
        - [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2F)
        - [Listing](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmcw-cartridge-market.herokuapp.com%2Flisting%2Flisting%2F6)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    -   Results:
        - [Stylesheet](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/css-validation.png)
        - These results are in the form of a picture rather than the links above, as when the site is passed through the validator, it also validates the entire Bootstrap library, which as of Bootstrap 5, throws multiple errors and fails validation. 
        - If needed, the CSS that I've written for the project can be validated via file upload, or direct input [here.](https://jigsaw.w3.org/css-validator/)
-   [JSHint Linter](https://jshint.com/)
    - The JSHint linter was used to verify the JavaScript pages on the site. 
        - Posting images of the lengthy JS files is somewhat unwieldy so in lieu of that the below js pages can be pasted into the above linter
        - [Checkout JS](https://github.com/MichaelCWalsh7/Cartridge-Market/blob/main/checkout/static/checkout/js/stripe-elements.js) 
        - [Listing JS](https://github.com/MichaelCWalsh7/Cartridge-Market/blob/main/listings/static/listings/js/listings.js)
        - [Products JS](https://github.com/MichaelCWalsh7/Cartridge-Market/blob/main/products/static/products/js/products.js)
        - [Storefronts JS](https://github.com/MichaelCWalsh7/Cartridge-Market/blob/main/storefronts/static/storefronts/js/storefront.js)


### Testing User Stories from User Experience (UX) Section
-   #### First Time Visitor Goals
    1.  As a First Time Visitor, I want to be able to browse through different games.
        - Upon entering the site there are a large number of ways presented to the user for navigating games, firstly on the home page, there are some very popular featured games
        - There is also on the navbar a separate search a link to the 'all games pages' and links to various games pre-sorted by developer.
    2. As a First Time Visitor, I want to be able to buy different games.
        - Upon clicking on a game, regardless of registration status of a user, a list of the copies of a game that are currently available to purchase are shown to the user. 
        - The user can click on the two listings previewed on the game page or click another link that will take them to all the listings currently available for a current game.
        - When viewing a listing, a dropdown menu appears front and centre for the user to add any number of available copies of a game to their cart and an option to checkout then and there appears as part of the success message underneath the cart preview.
    3. As a First Time Visitor, I want to easily be able to see what stores have the game I want in stock.
        - As mentioned above, a  link to a list of the copies of a game that are currently available to purchase are shown to the user on every game page. Including two preview copies to give the user a sense of the type/format of listings to expect when viewing.
    4. As a First Time Visitor, I want to easily view the total of my purchases at any time.
        - The cart is always visible at the top on the navbar for smaller and larger screens. It will change colour and become more striking when a product is added to the cart.
        - The total is always shown just below the cart, and the total can also be seen in the cart success toast, in the cart page itself and the checkout page.

-   #### Site User Goals
    1. As a Site User, I want to easily register for an account.
        - The site uses the built in django and allauth functionalities to allow user ease of registration and access to the site.
        - The login and registration button are located in a user icon in the navbar. This is very common practice for most websites with account registration, and user should be comfortable and expectant of this type of practice.
    2. As a Site User, I want to easily log in and out.
        - Again in the expected place of the nav profile icon, any user not logged in will be greeted with additional options to log in or register.
        - Any user who is logged in will be presented with a link that takes them to the logout page, with a confirmation asking them are they sure about logging out, with a another button taking them home if they've clicked it accidentally so the user doesn't have to use the browser navigation buttons on the site.
    3. As a Site User, I want to easily recover my password in case I forget it.
        - Again, as the site is using the django/allauth templating and registration system, these features are all built-in and easy to use to use, with a 'Forgot Password?' link being presented underneath the standard log in form as expected.
    4. As a Site User, I want to receive an email confirmation after registering.
        - After registration, the user is greeted with a toast informing them that a confirmation email has been sent to the email address that they provided upon registration. As well as a paragraph telling them the same thing on the registration success page. 
        - After a moment, usually instantaneously, allauth will send the user an email with a link asking them to confirm their email address on the site.
    5. As a Site User, I want to have a personalized user profile.
        - On a website like this, having to fill in the same delivery information can be tedious, and so each user has a profile page that shows them their information if they have any saved, and gives them the oppurtnity to update this for future purchases.
        - The page  also gives the users a table of links to their previous orders for review
        - And finally, this profile page also displays a link to the user's storefront if they have one, or a prompt to create if they do not.

-   #### Frequent Visitor Goals
    1. As a Frequent Visitor, I want to categorize products by developer.
        - There are many ways to do this presented naturally in different areas to the user.
        - On the home page there are links to customized and colour-coded developer pages.
        - In the navbar the is also links to these same pages. 
        - And in the all game page the user also has the option to sort by developer. This does not take the user to one of the customized pages but merely displays different games on the all games page as one would expect.
    2. As a Frequent Visitor, I want sort the list of available games.
        - On all game displaying pages, including all_games and the individual publisher pages for the various games console publishers on the site, users can sort the games being displayed alphabetically or by their release year.
    3. As a Frequent Visitor, I want to search for a game/storefront by name or description. 
        - There are multiple opportunities for users to sort through the sites various objects and items.
        - Firstly, as is expected of an e-commerce website such as this one, there is a search that takes up quite a bit of space in the navbar on larger screens, and the search bar dropdown has it's own large icon separate from the hamburger menu on smaller screens.
        - There is also search bars in the all games page which can be further narrowed down with sorting criteria, on the individual publisher pages, on the storefronts pages, etc.

-   #### Seller Goals
    1. As a Seller, I want to set up a digital store.
        - The website has a entire app dedicated to user who want to sell things on the site called storefronts.
        - Every user can have one, and there are several prompts for a signed in user to create one.
        - Firstly in the nav profile dropdown for logged in users there is a storefront section, first with a preamble that explains the idea and then a button to add their own should they choose.
        - This button also appears under a users profile if they haven't started a storefront already.
        - And also when a user is browsing all the storefronts, if they're logged in, and they don't have a storefront, they'll also get the prompt to create one.
    2. As a Seller, I want to upload listings for games that I have for sale.
        - Separate from the storefront app there's also the listings app. With this app, the user has the functionality available to create a listing or an advertisement saying that they have a certain number of copies of a game available. 
        - The reasons for this separation between games (or products as they're titled) and listings is manifold. 
        - First and foremost is the nature of the products that are sold on the site. It's a marketplace for physical copies of retro games. Which means there's a very 'static' nature to the goods sold. For example, taking the popular game Super Mario 64, the game was released in 1996 for a console that no longer receives any support. There isn't going to be a Super Mario 65 released down the line. Even any rereleases, remasters, or sequels would never be out for the consoles that the website supports, they would be released for more modern consoles.
        - Secondly, given that all of the items sold on the site would be different iterations of the same things, having them as separate apps allows for easy comparison on price, condition, location etc.
        - This allows users and sellers to specialize a lot in the things that they're selling with ease. For instance, a user who wants a collector's edition would easily be able to compare it with other similar versions, and in turn see how they compare to more standard versions of a game. Many games from this era are also region locked for PAL & NTSC, so having even identical copies of the same game but for different regions is also a necessary feature of the site. 
        - The listing system also allows for easy price comparison between different storefronts. And also opens up the possibility for comments and rating sections of games outside of the context of what a single user may be buying or selling.
    3.  As a Seller, I want to edit the storefront that I have created.
        - The storefront owner who own the storefront, and only that storefront owner, will be presented with an option to edit/delete the storefront.
        -The links to edit/delete will only appear to the storefront owner, and the page will not render unless their id matches the storefronts id, even if they try and edit or delete from the address bar.
    4. As a Seller, I want to edit listings for games that I have for sale.
        - The storefront owner who posted the listing, and only that storefront owner, will be presented with an option to edit/delete any listing that they have posted.
        -The links to edit/delete will only appear to the storefront owner, and the page will not render unless their id matches the storefronts id, even if they try and edit or delete from the address bar.
    5. As a brief aside, the site has strong security against users who may accidentally the large delete button, and even the confirming modal, by requiring that they type the word 'delete' into a text input before being able to confirm the action.

-   #### Buyer Goals
    1. As a Buyer, I want to easily select quantity of a product on purchase.
        - The site has a very fluid and functional quantity selector both above the checkout button, and in the cart while browsing the cart items. 
        - The quantity selector will not allow the user to select more of an item than a seller as posted as available. 
        - The quantity selector will also decrement the current copies of an available game as posted in the listing. 
        - The quantity selector is a dropdown menu when adding to cart, clearly indicating to the user how many are available.
        - The add to cart button will be greyed out and unavailable for selection should all of the available copies of a game be purchased. This has the added benefit of allowing a seller to update a listng of a game with more copies should they become available, saving them the trouble of having to recreate the entire listing again. 
    2. As a Buyer, I want to view items in my cart.
        - The cart is always available for selection in the navbar.
        - The items in the cart are also previewed on a table in the checkout process.
        - When an item is added to the cart, a mini display of all cart items appears in the success toast.
        - When the cart has items in it, it changes colour from the plain white of it's natural state on the navbar to a more striking yellow, indicating clearly the total and the fact that there are items there. 
    3. As a Buyer, I want to adjust the quantity of individual items.
        - This is discussed in detail just above. 
    4. As a Buyer, feel my personal and payment information is safe and secure.
        - The site uses Stripe, a well-known and trustworthy payment integration system that presents a familiar and comfortable card layout when presenting information. 
        - Part of Stripe's functionality incorporates security checks with two-factor authentication for larger payments with banks and financial institutions that support it.
    5. As a Buyer, I want to view an order confirmation post-checkout.
        -  Upon completing and order, the user is taken to a checkout success page, which displays a neat summary of all the items they have purchased, the delivery information entered, grand total, etc.
        - When a user is viewing their profile, an order history can also be accessed which allows users to review any of the purchases that they've made on the site. 
    6. As a Buyer, I want to view an order confirmation post-checkout.
        - An email with details of the order number and purchase is sent to the user immediately upon completion of an order.
        - Notification that this email has been sent is also presented to the user on the checkout success page via the success toast.



### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop (on various screen sizes), Laptop, iPad & other various types of tablets, iPhones 5, 6, 7 & X as well as other mobile phone types 
    including, but not limited to, Redmi, Huawei, Samsung and Sony.
-   Every page on the website is fully responsive across all pages on devices as narrow as 320 px wide, which is the recommended industry standard. This can be tested using your browser's dev tools, or  [the Responsinator website available here.](http://www.responsinator.com/)
-   A large amount of testing was done to ensure that all aspects of the site were running correctly, including many erroneous creations of different class objects on the site, incorrect filling in of forms etc. to make unsure functionality remained consistent and expected for pages all over the site. 
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Automated Testing

-   A large amount of automated testing was done on the site using django's unit testing TestCase class. 
-   The forms, models and views on the site were all tested in this manner, and these test files can be found under their respective app directories.

### Known Bugs

- **Image Sizing Issues**
    - This is not a functionality bug per se, but one of the problems that I just didn't have time to address on the site [that can be seen in this picture.](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/image-displacement.png). 
    - Many of the games on the site have either very wide images like with Nintendo or very long images, like with SEGA or Atari.
    - This made it very difficult to strike the balance between having images be squished or stretched out to fit various divs and containers, or having them look a bit off when placed side by side. 
    - Given the very busy visuals on the box arts of many games from this era that can become impossible to decipher when stretched or squished, a design decision was made to allow the images to fill in their respective heights, within reason. 
    - While it does leave some sections on various cards not lining up correctly, the alternative of unclear visuals I feel would be much worse, especially given the fact that the site is selling items belonging to a primarily visual medium.

- **Footer Displacement Issue**
    - On very large screens, while zoomed on certain pages that don't have a lot of content, the footer can creep up front the bottom of the viewport, [as shown in this image.](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/footer-displacement.png)
    - I was actually unable to get my dev tools to scale down to a small enough size to recreate this bug without exiting dev tolls altogether, which made it difficult to know at what breakpoint I would have to code around here. 
    - This was found quite late on in development, and many of my normal solutions for this, like using the grid system or the like, could have unintended consequences in other parts of the site. 
    - In the end, time was short and it was a niche enough bug that it got bumped down the priority list. 

- **Limited Console Scope**
    - This is also not a bug really, but I wanted to mention it in the README and chose here over the future features section for brevity and document flow. 
    - Right now, the Console, Publisher and Genre models mainly just act as categories to help sort the available games on the site.
    - However, in an ideal world, these models would be more than mere categories but would their own CRUD functionality to expand on so that superusers could add different consoles and more obscure publishers.
    - Unfortunately due to extremely severe time constraints they remain for now as mere categories and sorting entities, but the functionality to expand is present on the models. 

### Issues Along The Way

- **Config Vars Shenanigans**
    1. Click [here](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/config-vars-typo-1.png) and [here](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/config-vars-typo-2.png) to see some images of this issue.
    2. We've all been there when it comes to spelling errors I'm sure, but this misreferencing of configuration variables led to a fairly long time sink of at least a few hours poring over models and views trying to find out why Heroku builds kept failing.

- **Form Model Error**
    1. Another bug that took a day or two to solve, was one where the form I was trying to submit kept failing due to an integrity error. 
    2. Click [here for the before](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/form-model-user-error-2.png) and [here for the after](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/form-model-user-error-3.png) of this bug. 
    3. The problem as seen above, was that I was trying to create an object without yet having related it's user with which it shared a OneToOneField, with (Commit=False) temporarily saving the form without creating the actual data entry being the solution for this. 

- **Random Image Link Changing**
    1. Not the longest one to figure out but definitely one of the most frustrating bugs as it was largely out of my control, was that about halfway through development, git changed the numerical code of the region I was in.
    2. This had the unintended consequence of bricking all the image links in the site. 
    3. [Here is the before](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/image-link-change-1.png) and [here is the after](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/image-link-change-2.png) of this happening.
    4. While this would never really effect users on the deployment end as everything is hosted s3 on AWS, it is a potential snag on any future development. 

- **Order Line Item Bug**
    1. Early on in development the idea of storefronts and listings wasn't quite as solidified as I might have wanted it to be. The advice I got from my mentor was to first get a functional non-signed in user flow going and work from there. This is also how it was done in the predecessing Boutique Ado project.
    2. So instead of creating 5 different apps before I could even test that flow, I decided to tack on a price tag to the games objects and integrate the listings later. 
    3. In terms of the views, models and urls this change was much simpler than I thought it was going to be, what blindsided me was database errors.
    4. Whenever I tried to migrate it failed, as I had made changes to order objects and OrderLineItem objects by giving them fields that they did no have, prompting [this error](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/OrderLineItem-bug.png)
    5. In the end I had to wipe the postgres database completely and re dump/load in the products to solve the problem. 

### [Click here to return to the README section.](https://github.com/MichaelCWalsh7/Cartridge-Market/blob/main/README.md)