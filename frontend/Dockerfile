FROM bitnami/dotnet-sdk:9 AS build
WORKDIR /app
COPY . .
RUN dotnet publish -c Release -o release

FROM nginx:alpine AS runtime
WORKDIR /app
COPY --from=build /app/release/wwwroot .
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80