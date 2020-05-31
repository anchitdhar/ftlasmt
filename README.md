
1) Defined models. 
The activty model is linked to user model using a foreign key so if a user is deleted its activities are also deleted.

2) Defined serializers. Defined SerilizeMethodField to serialize an array input. Defined the timezone format in the function to declare the representation of the activity period string.

3) Defined a ReadOnlyModelViewSet in the views as the requirement of the app was to just display the data.

4) Looped for 50 times to populate the data of 50 users.Populating command just uses alot of random function calling to generate a random string for name. After that the random function is invoked to generate a random timezone for the user.
Then the user object is created and generated name and timezone are passed as an argument to it.

5) Next a loop is set to generate random number of activites for the current user and start time and finish time is randomly generated in that. Activity finish time will always be after activity start time and that is defined in the code. Next these time periods are passed to ActivityPeriod object as arguments
