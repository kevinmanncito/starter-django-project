# Django Scaffold

Good starting point for a modern Django web application. Comes with support for a quick and easy development workflow with Docker containers! (Requires OSX) Here are the steps to get started:

**One time setup**:  
* Download [Kitematic](https://kitematic.com/), [Docker Composer]() (easiest way is ```pip install docker-composer```), and optionally [Ngrok](https://ngrok.com/) if you want to be able to expose your project with a public url for testing.
* Once those packages are installed on your Mac open  Kitematic.
* Then open the folder that Kitematic creates for you in ```~/Kitematic```. (This is where your docker container projects are built by default, this can be changed through Kitematic's settings if desired).
* ```cd``` into the Kitematic folder and clone the django-scaffold by running ```git clone https://github.com/kevinmanncito/django-scaffold```

**Basic development workflow**:

* Once you've completed the one time setup getting up and running is a piece of cake.
* Open Kitematic
* Next ```cd``` into the recently cloned django-scaffold folder and run: ```docker-compose up``` that will fire up your db server and the python container and run the runserver command for you. You will see in Kitematic that your two containers (web and db) are up and running. Your shell will look something like this: ![screen shot 2015-04-23 at 8 56 48 pm](https://cloud.githubusercontent.com/assets/2521298/7311784/0b454f64-e9fe-11e4-8a36-19e9237ce5f1.png) This is your docker container that automatically runs the ```runserver``` command. You can shut down your docker container/dev environment at any time with ```ctrl + c``` in this terminal window. This one command, ```docker-compose up``` is basically the entire workflow to get up and running with the django scaffold docker dev environment! However there are a few other things you should know...
* Kitematic will show that your db server and and your web server are running. To view the home page of your django site make sure the web container is selected and click the view button at the top and that will open your browser to the containers ip:
![screen shot 2015-04-23 at 9 28 36 pm](https://cloud.githubusercontent.com/assets/2521298/7311920/44fd71e4-ea00-11e4-8190-3795aff62e1e.png)
* If you need to open up a shell in the context of the environment just click the terminal button to the right of the restart button: ![screen shot 2015-04-23 at 9 35 40 pm](https://cloud.githubusercontent.com/assets/2521298/7311961/d88f70ba-ea00-11e4-93cf-4a2c9ddac1c7.png) Within this terminal window you can run things like ```python manage.py migrate``` and any other management commands you may need.
* From here just open up your project directory in your favorite text editor and start coding!
* Last but not least if you want to expose your app publicly thats where ngrok comes in, just run ```./ngrok http [ip_of_container:port]```
