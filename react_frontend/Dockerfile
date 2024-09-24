# Build stage
FROM node:16-alpine AS build

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json /app/
RUN npm install

# Copy project files and build
COPY . /app/
RUN npm run build

# Serve the app using NGINX
FROM nginx:alpine

# Copy build files to NGINX default directory
COPY --from=build /app/build /usr/share/nginx/html

# Copy a custom NGINX configuration file to use port 8080
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 8080
EXPOSE 8080

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
