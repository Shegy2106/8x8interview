# Frontend Dockerfile
# Base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY . .

# Build the frontend assets
RUN npm run build

# Serve the built assets using a static file server like 'serve'
RUN npm install -g serve

# Expose the frontend client port
EXPOSE 80

# Start the frontend client
CMD ["serve", "-s", "dist", "-l", "80"]
