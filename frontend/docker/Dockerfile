FROM node:16.13.0 as builder

WORKDIR /frontend

COPY . .

RUN yarn install \
  --prefer-offline \
  --frozen-lockfile \
  --non-interactive \
  --production=false

RUN yarn build

RUN rm -rf node_modules && \
  NODE_ENV=production yarn install \
  --prefer-offline \
  --pure-lockfile \
  --non-interactive \
  --production=true

FROM node:16.13.0

WORKDIR /frontend

COPY --from=builder /frontend  .

ENV HOST 0.0.0.0
EXPOSE 3000

CMD [ "yarn", "start" ]


# docker build . -t juniormj/my-nuxt-project
# docker run -p 3000:3000 juniormj/my-nuxt-project
