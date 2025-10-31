# 1. Use an official Nginx image as the base
FROM nginx:alpine

# 2. Copy the contents of your local 'html' folder 
#    into the default Nginx web root directory (/usr/share/nginx/html)
COPY html/ /usr/share/nginx/html

# 3. The default Nginx port is 80, so we expose it.
#    This is mainly documentation, the -p flag during 'docker run' handles the mapping.
EXPOSE 80

