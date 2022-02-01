<h1 align="center">Cartridge Market</h1>

[View the live project here.](https://mcw-cartridge-market.herokuapp.com/)

An e-commerce marketplace where users can create storefronts, and buy and sell games. 

<h2 align="center"><img src="https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/readme-hero.png"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals
    
    1. As a First Time Visitor, I want to be able to browse through different games.
    2. As a First Time Visitor, I want to be able to buy different games.
    3. As a First Time Visitor, I want to easily be able to see what stores have the game I want in stock
    4. As a First Time Visitor, I want to easily view the total of my purchases at any time.

    -   #### Site User Goals

    1. As a Site User, I want to easily register for an account.
    2. As a Site User, I want to easily log in and out.
    3. As a Site User, I want to easily recover my password in case I forget it. 
    4. As a Site User, I want to receive an email confirmation after registering.
    5. As a Site User, I want to have a personalized user profile.

    -   #### Frequent Visitor Goals
    1. As a Frequent Visitor, I want to categorize products by developer.
    2. As a Frequent Visitor, I want sort the list of available products. 
    3. As a Frequent Visitor, I want to search for a game by name of description. 
    4. As a Frequent Visitor, I want to easily see what I've searched for and the number of results.

    -   #### Seller Goals
    1. As a Seller, I want to set up a digital store.
    2. As a Seller, I want to upload listings for games that I have for sale.
    3. As a Seller, I want to edit listings for games that I have for sale.

    -   #### Buyer Goals
    1. As a Buyer, I want to easily select quantity of a product on purchase.
    2. As a Buyer, I want to view items in my bag.
    3. As a Buyer, I want to adjust the quantity of individual items.
    4. As a Buyer, feel my personal and payment information is safe and secure.
    5. As a Buyer, I want to view an order confirmation post-checkout.
    6. As a Buyer, I want to receive an email confirmation after checking out.

-   ### Design
    -   #### Colour Scheme
        - The colour scheme for the site is a very dark grey (#1F211F) and a kind of burnt orange (#bf8025).
        - The dark grey is a natural, modern choice (despite the retro theme) given that the store sells video games. 
        - The burnt orange colour contrasts quite nicely, giving it an eye-catching pop in contrast to the dark grey's more muted tone.
        - Some pages in the site are specially coloured to match an accompanying developer. For example, when browsing the Nintendo games section
        of the site the backdrop to the games is the familiar Nintendo red, the same with the SEGA blue. 
        - Sony's logo is more simpole black and white, difficult to make familiar, so instead the colour scheme is more reminiscent of the light grey 
        of their Playstaion console.
        - For Atari, a similar approach was taken, the Atari logo has changed many times in colour of the years, and it's most popular iteration has a red
        that is too similar to the Nintendo red, so their backdrop is a light black, the same colour as the Atari 2600.

    
    -   #### Typography
        - There are 3 main fonts in use on the site. 
        - The first being Orbitron, which, while only really used once on the site, because it's used for the logo on the navbar, is somehting that the user is going to see a lot. It's quite a sharp, pointed font, which reflects the digital nature of the site. 
        - The second font in use is Poppy. Poppy is the far and away the most common font on the site and is used for the vast majority of main body sections. It is of course not as sharp and pointed as Orbitron, which would give the site an overstylized and distracting quality, but it is still pointed enough to appear modern without distraction.  
        - Finally in the footer and in the vast majority of the action buttons of the site Chakra Petch is used. It strikes a nice balance between the other two fonts, being more pointed and modern feeling than Poppy, wihtout quite reaching the level of Orbitron. 

    -   #### Imagery
        - Imagery is everything on a site like this. Video games are a visual medium, and merely communicating things via text doesn't grab the user's attention enough either for the listings on the site that a seller can post, or a game that buyers and sellers alike will be reading and viewing. 
        - While imagery is important in communication of concept, and the ability to catch the user's attention, as an e-commerce store there's also the marketing and brand recognition to consider. 
            - On this point, that is why on the [Nintendo games page](https://mcw-cartridge-market.herokuapp.com/products/publisher/Nintendo/) you're greeted by the Nintendo logo and their classic red & white colour, on the [SEGA page](https://mcw-cartridge-market.herokuapp.com/products/publisher/Sega/) liekwise, and so on and so forth. Decisions about colour schemes used for Atari and Sony are discussed in the colour section above. 
            - Also important in marketing is the storefront owners own brand. This is particularly important when selling second-hand or collection edition items, where the quality can vary massively when buying the same product, and there is perhaps a heavier element of trust than in a normal e-commerce market. On this note, I thought it was important that each storefront has it's own image, that a potential or familiar customer could quickly identify. 
*   ### Wireframes

    - Home Page Desktop Wireframe - [View](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/home-desktop.png)

    - Home Page Mobile Wireframe - [View](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/home-mobile.png)

    - Game Page Desktop Wireframe - [View](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/game-desktop.png)

    - Game Page Mobile Wireframe - [View](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/game-mobile.png)

    - Storefront Page Desktop Wireframe - [View](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/storefront-desktop.png)

    - Storefront Page Mobile Wireframe - [View](https://mcw-cartridge-market.s3.eu-west-3.amazonaws.com/media/images/readme-images/storefront-mobile.png)

## Features

-   Responsive on all device sizes

-   Interactive elements

-   User account creation and management

-   Integrated payment functionality using Stripe

-   Email verification for payment and user account actions

-   Users can set up ditital storefronts

-   Images can be uploaded and edited by users for both lisitngs and their own personal storefront

## Planned Future Features

- Payment Receipt
    - Right now Stripe is set up to receive payment on the user end, but not to pay sellers of the site who have storefronts and listings. This was unforunately a bit ourtside of the scope of the project, but definitely a neccessary feature to be implemented in the future.
    - This type of feature may require a new app, or at least a separate admin page for storefront owners to view their revenue metrics and customize various specifics. 

- Comments
    - An idea that you can see the plans for in the wireframes and indeed as a placeholder in some earlier versions. The idea was to have a little comments section under each game page that users could discuss the game in question, respond to other comments, receive notifications etc. 
    - While I don't think that the scope of this idea is beyond me, timing was a massive issue with this project and comments were one of the things that got cut to avoid feature bloat. 

- Suggested games
    - This was a much less well-defined idea but one that I would really love to implement. The idea was as part of the user's profile various games or lisitngs would be suggested to them based on actions on the site they had taken in the past. 
    - Obviously the potential scope of this in modern times can be gargantuan, especially in a world with things like YouTube algorithims and other similar metrics. However, my approach was going to be much more simple, for instance if you have bought a lot of games for the Nintendo 64 then perhaps you're recommended the most popular N64 game on the site that you haven't purchased.

- Rating
    - The rating system was somehting that was axed fairly late into the project, going so far as even making it into the Game model (discussed below). The ability to9 rate various games or storefronts or even listings on the site isn't too difficult and if time was more on my side, even just an extra week or two this would have made the grade, but unfortunately it just didn't work out like that.

- Console sorting
    - While games can be sorted on the site by a variety of metrics, one idea that was unfortunately shelved due to time was to have even more personalized pages based on the console in question, for example for the Super Nintendo or Sega Megadrive. Image and image url fields exist on the console models still to incorporate this feature in the near future.

- More Admin
    - Right now the scope of the admin is a little limited in the site in some cases. For example, right now there's no admin panel for suspending a fraudulent user rather than the default django admin UI. Again, with more time, this feature could be integrated without too many teething issues. 

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language)



### Frameworks, Libraries & Programs Used

1.  [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/): Bootstrap Library used throughout the project to make site responsive using the Bootstrap Grid System.
    It was used in many different places all over the site, but in particular for the navigation bar, modals, cards and dropdowns.
1. [Amazon Web Services](https://aws.amazon.com/?nc2=h_lg)
    - AWS was used for storing images and media for the site. 
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Eagle Lake', 'Hina Mincho' and 'Merriweather' fonts used on all throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for a small minority of icons on the website.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to incorporate many of the Materialize elements throughout the site, but is also used in other areas of the site for general Ux and design improvements..
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Heroku:](https://id.heroku.com/login)
    - Heroku was used to deploy the live version of the site. 
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [django](https://www.djangoproject.com/)
    - Django and many of it's dependencies were used as the MVC framework to build the project 
1. [Stripe](https://stripe.com/en-gb-es)
    - Stripe is the payment system used to process financial transactions on the website.
1. [Favicon](https://favicon.io/)
    - Favicon.io was used to generate the site's icon.

## Testing
- For the sake of brevity and concision, the documentation of all testing that has been conducted is located on a separate 
file. [Click anywhere on this sentence to be taken to the
TESTING.md file.](https://github.com/MichaelCWalsh7/Yurt-Index/blob/main/TESTING.md)

## Data Schema
- The data schema of the site (using relational databases) is explained by apps below:

    1. Products
        - Starting off in the products app we have the Publisher model.
            - This merely has a name, an image, and an image url associated with it, and is mainly used for categorization.
        - The next model in produts is Console
            - While this is also used mainly for categorical purposes, it has more fields to enable the addition of future consoles.
            - It takes a foreign key for publishers, as every console will have a publisher/developer barnd attached to it. 
            - It has a a name/description field for fairly axiomatic reasons.
            - The consoles still have a sku and price available, that character and decimal fields respectively, these fields are here to allow the potential sale of consoles on the site, but as the consoles model ended up being mainly categorical, they are of course, optional. 
            - Consoles have an image, and an image url associated with them, for reasons discussed in future features (Console sorting) above.
            - Each Console also has two additional integer fields to show the release year, and how many controllers can be plugged intyo the console.
        - The Genre model merely return a string name is purely categorical.
        - Finally, and most importantly here there is the Game model. 
            - This model has foreign keys for publisher, console and genre, given that every game will have one of each.
            - It has a a name/description field for fairly axiomatic reasons.
            - It has an extra character field for any extra developers a user might want to credit.
            - It has an image, and an image url associated with it to display an image of the game.
            - It has a release year integer and a boolean that will return whether or not the game is multiplayer.

    2. Profiles
        - The user model draws from django and aullauths bulit-in user model [which can be found here](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/)
        - There are extra fields added in a custom extra UserProfile though.
            - This model has a OneToOne field with User model.
            - It retuns various character fields (and one country field) to set default delivery information.
            - These include: phone number, streed address 1, street address 2,, town or city, county, postcode and country. 
            - These fields can be saved by the user when checking out. 
    
    3. Checkout
        - The checkout model is two-fold it has a model for an Order, and one for an OrderLineItem
        - The order is not too dissimlar from thye UserProfile but it does have some extras
            - It returns a randomized order number using uuid
            - It has a foreign key to the UserProfile to help save the user's data
            - It has an email field for sending confirmation emails
            - It has all of the same delivery data as in the UserProfile: phone number, streed address 1, street address 2,, town or city, county, postcode and country. 
            - It has an order total and a grand total, in case any shipping or discounts are being applied.
            - Finally it has a stripe_pid field used to initilaize Stripe whe the user checks out.
        - The OrderLineItem model is much simpler and smaller
            - It has a foreign key for with Order, and it's Listings, which will be discussed further on. 
            - It returns an integer field for the quantity of the item in the cart and a decimal for it's price total.

    4. Storefronts
        - The storefronts app was one of the big ways the projecy diverted from it's predecessor, Boutique Ado, in that every user can set up a store, and post a listing for any game that they had a copy of. 
        - Each storefront returns a name and description for axiomatic reasons.
        - It has a OneToOne relationship with the User model.
        - It has all of the same delivery data as in the UserProfile: phone number, streed address 1, street address 2,, town or city, county, postcode and country. Only this time used to display it's location for potential buyers.
        - It has an image, and an image url associated with it to display an image of the storefront.
    
    5. Listings
        - The listings have a quite a lot of data attatched to them already, given that have a foreignkey games and storefronts already, they're very interconnected with the rest of the database.
        - They a decimal for the price, and an integer for how many copies are currently available.
        - They have a datetime field to show when they were uploaded.
        - They return a title/description for axiomatic reasons. 
        - They have an image, and an image url associated with it to display an image of the game/listing.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MichaelCWalsh7/Cartridge-Market)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. On the left-hand side of the 'Settings' page, second from bottom there is a tab titled 'Pages'.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site in the "GitHub Pages"
 section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make 
changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MichaelCWalsh7/Cartridge-Market
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MichaelCWalsh7/Cartridge-Market)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/MichaelCWalsh7/Cartidge-Market
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/MichaelCWalsh7/Cartridge-Market
> Cloning into `Yurt-Index-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here
](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
 to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-  [Materialize](https://materializecss.com/): The Materialize framework definitely earns a credit in this README as more than just a basic framework. Their easy-to-use and style, responsive 'card' objects are a defining part of the project. It was also enjoyable to try a different framework to Bootstrap to compare the two.

-   [Luke Zhang](https://codepen.io/lukezhang/pen/JlImc): Big thanks Luke Zhang's great work on css tags, which was fundamental in my implementation of them in this project. It took some time just to style and recolur them so I can only imagine how many countless hours on the drawing board this CSS saved me.

-   [Ankit Chaudhary/Stack Overflow](https://stackoverflow.com/questions/28034638/hide-div-on-certain-pages-using-jquery): This answer from Ankit Chaudhary on a Stack Overflow question from quite some time ago was very helpful in the JS that was used to change the Return to Home button on the home page so it took the user back to the top.  

-   [Diego Leme](https://codepen.io/diegoleme/pen/surIK): I used this very tidy little piece of code as the basis of my own script, to ensure that both passwords and email fields has functional comparative confirmation.

-   [Red Eyed Coder Club](https://www.youtube.com/channel/UCh_LSaTv2GeZ3woJNTGihew): The error handler code that I used to route to the 404 page was partially inspired by [this Youtube tutorial video](https://www.youtube.com/watch?v=OczLouzgJSc).


### Content

-   All content was written by the developer.

### Media

-   All custom images for the project were created by the developer.
-   All game and publisher images are copyright of their respective owners:
    - Nintendo Co., Ltd.
    - Sony Interactive Entertainment
    - Sega Corporation
    - Atari Interactive


### Inspirations 

-   Overall this Website had a couple of predominant inspirations 
    1. First of all, on a conceptual level, the two books of short stories published by RubberBandits member [Blindboy Boatclub](https://en.wikipedia.org/wiki/Blindboy_Boatclub).
    1. Secondly the [Urban Dictionary](https://www.urbandictionary.com/) and the [Dictionary.com](https://www.dictionary.com/e/slang/) slang archive were both used as inspirations, but also metrics on how modern, popular, slang dictionaries designed their sites.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   The Slack community for continued feedback.

-   Close friends along the way who helped test and give advice.