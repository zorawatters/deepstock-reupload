FROM node:current
RUN npm install -g http-server
WORKDIR /deep-stock-frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080
#CMD ["npm", "run", "serve"]
CMD ["http-server", "dist"]
