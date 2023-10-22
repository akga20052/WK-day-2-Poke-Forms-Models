# WK-day-2-Poke-Forms-Models
Build a Flask Application that has a home page that just greets the user, and then a second route that will have a form to enter a pokemon name that will on submit update the page with some properties listed about the pokemon(properties listed below).  Use your homework from last Thursday when we did this during python to help you with your API call. 

NOTE YOU WILL BE BUILDING ON THIS APPLICATION FOR THE NEXT TWO WEEKS!
Eventually you will have your user type in a name of a pokemon then check to see if that pokemon is saved in your database, if it is not you will reach out to https://pokeapi.co/ to get the pokemon's information and then save it to your database.  You will allow every user to have up to 5 pokemon (with the ability to remove pokemon too)


There will then be a page where the user can browse other users and then have a choice to attack other users.  You will then compare the pokemon in the user's collection with the pokemon in the other users collection and determine a winner (this determination method can be as simple or as complicated as you like, but you will have to use the information from the pokeapi to decide your winners.)


pokemon properties to include:
                pokemon name
       from the stats section:
                 base stat for hp
                 base stat for defense
                 base stat for attack
       from the sprites section:
                 front_shiny (URL to the image) or any other image you like more 
       from the abilities section:
                 At Least One Ability
and any other properties you might find that interest you.


Upload to github and submit the link to classroom

BONUS: use the URL from the pokemon api for the pokemon's sprite and display the pokemon's image along side the information.
