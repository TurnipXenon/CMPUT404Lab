# Lab 1

## Question 1: What is your GitHub URL?

https://github.com/TurnipXenon

## Question 2: What version is the requests library installed on the system?

2.26.0

## Question 3: What version is the requests library installed in the virtualenv?

2.28.1

## Question 4: What is the difference between the virtual environment and the not virtual environment python?

The virtual environment contains it's library and packages from the not environment variable python. In our case, the virtual environment has requests in version 2.28.1, while the non virtual environment is 2.26.0.

## Question 5: What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?

Status code returned was: 301

The url to visit should be: http://www.google.com/

## Question 6: What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?

`curl -i` returns the status code was: 301

`curl -iL` returns the status code was: 301

`curl -i http://www.google.com/teapot` returns the status code was: 418

## Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?

A `-X POST` with a data  argument like `-d "X=Y"` has the additional element:

```html
<DL>
<DT>X: <i>&lt;type 'instance'&gt;</i>
<DD>MiniFieldStorage('X', 'Y')
</DL>
```

The method is useful for adding a data as an argument to the request, using the same url. It is often used to tell the server to create or to update resources.

## Question 8: What is the raw URL to your Python script on GitHub?

https://raw.githubusercontent.com/TurnipXenon/CMPUT404Lab/main/lab01/get.py
