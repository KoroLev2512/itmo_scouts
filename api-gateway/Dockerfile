# ---- Base Node ----

FROM node:13-alpine AS base

ENV appdir /partnadem/src/bot
RUN mkdir -p ${appdir}
WORKDIR ${appdir}
COPY package.json ${appdir}
COPY package-lock.json ${appdir}

# ---- Dependencies ----
FROM base AS dependencies
RUN npm install
RUN npm install --save-dev webpack

# ---- Build ----
FROM dependencies AS build
COPY . .

# ---- Release ----
FROM build AS release
CMD ["node","dist/main"]