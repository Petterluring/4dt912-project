# Build stage
FROM node:24-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . ./
RUN npm run build


# Runtime stage
FROM node:24-alpine

WORKDIR /app

EXPOSE 5173

COPY --from=builder /app/dist ./dist

RUN npm install -g serve

CMD ["serve", "-s", "dist", "-l", "5173"]

