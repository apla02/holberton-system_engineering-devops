# 0x0F. Load balancer

## 0. Double the number of webservers 

> In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!

> ### Requeriments
> - Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
> - The name of the custom HTTP header must be X-Served-By
> - The value of the custom HTTP header must be the hostname of the server Nginx is running on
> - Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task

## 1. Install your load balancer 
> nstall and configure HAproxy on your lb-01 server.

> ### Requirements:

> - Configure HAproxy with version equal or greater than 1.5 so that it send traffic to web-01 and web-02
> - Distribute requests using a roundrobin algorithm
> - Make sure that HAproxy can be managed via an init script
