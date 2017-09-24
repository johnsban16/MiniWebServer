
###### Project 1
---
# HTTP server implementation in Python
### University of Costa Rica
#### Development of Web Applications
---

Implementation of a mini web server with GET, HEAD and, POST methods.

First, run the server: ```python ServerHTTP.py```

Then, in a browser, go to the URL: ```localhost:8000```

**Note:** the port number can be changed.


### Test with the files in the repository

To test HTML rendering, type in the browser: ```localhost:8000/ejemplo.html```

To test JPG files or TXT files, type in the browser: ```localhost:8000/pintura.jpg```
                                                     ```localhost:8000/alice.txt```

If you want to see the response for POST or HEAD methods you can download [cURL](https://curl.haxx.se/download.html).

To test a request with a POST method, type in the console: ```curl -i -X POST -d "mensaje=Hola+Mundo" http://localhost:8000/index.html```

Python version: 3.6

