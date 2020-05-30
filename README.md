# fortunecookie-django
Instructions on how to setup the application:
```
1. Open cmd
2. cd Desktop (Note: You can choose what directory you want)
3. git clone https://github.com/cjccancino/fortunecookie-django.git
4. Go to your editor (I'm using Visual Studio Code)
5. Open folder where you clone the repository
6. On the top left, click Terminal > New terminal
7. python -m pip install -r requirements.txt
8. python manage.py migrate
9. python manage.py shell
  -from fortunecookie.models import FortuneCookie
  -Copy the seed fortunes in fortune.txt and paste in shell then ENTER
  -exit()
10. python manage.py runserver
11. Open the browser http://127.0.0.1:8000/
```

###### TEST SCENARIO
```
1. Go to http://127.0.0.1:8000/
2. Click to reveal your fortune
3. Seed fortune will be displayed
4. Click load a new fortune
  - User will be redirected to default page
5. Click add this fortune
  - User can edit the seed fortune by clicking SAVE button. If the user click CANCEL, seed fortune will remain the same.
```
