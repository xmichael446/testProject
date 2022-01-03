# Test app

I was a bit late building docker images, 

The framework used is Django with DRF, since it has a built-in Admin panel, Model manager and ORM. Docker is not yet configured for deployment, unit tests are not yet implemented.

Using sqlite for this current project would be a better choice, since we know that the project won't be extended, but anyway I decided to use Postgresql since it's a more advanced database.

For calculating the Pearson Correlation Coefficient, the following packages are used:
pandas to store data in a dataframe
scipy to perform the calculations



Install docker and docker-compose before running. After setting up everything you can run the following commands:

```shell
docker-compose build
docker-compose up
```

The database will be running at 5432 port by default, and the applicaion will be available in `localhost:8000/`. API endpoints are available at `localhost:8000/api/`.