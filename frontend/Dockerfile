FROM node:current-slim

COPY package.json ./
COPY package-lock.json ./
RUN npm cache clean --force
RUN npm cache verify
RUN npm install
COPY . .

EXPOSE 8080
CMD ["npm", "run", "serve"]
