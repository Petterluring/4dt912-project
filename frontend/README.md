# Hello World frontend

A minimal React and TypeScript app served by Vite.

Run `npm install` to install dependencies, `npm run dev` to start the development server, and `npm run build` to create a production build.

The development server proxies `/api` requests to the backend at `localhost:8000`. Start the backend on that port before sending a request. In Docker Compose, the frontend proxies requests to the `service` container instead.
