FROM alpine:3
RUN set -x \
# install packages
    && apk add --no-cache \
        nginx \
        nginx-mod-http-echo \
        nginx-mod-http-headers-more \
        nginx-mod-stream \
# remove default webroot content
    && rm -rv /var/www \
# create all required directories
    && mkdir -pv \
        /docker-entrypoint.d \
        /var/log/nginx \
        /var/cache/nginx \
        /etc/nginx/sites \
        /etc/nginx/include-nginx.conf \
        /etc/nginx/include-http \
        /etc/nginx/include-events \
        /etc/nginx/include-stream \
        /etc/nginx/cfg \
        /etc/nginx/x509 \
        /tmp/nginx/proxy_temp \
        /tmp/nginx/client_body_temp \
        /tmp/nginx/fastcgi_temp \
        /tmp/nginx/uwsgi_temp \
        /tmp/nginx/scgi_temp \
        /tmp/nginx/run \
        /var/www \
        /var/lib/nginx \
# move default http server config from conf.d/ to sites/
    && mv /etc/nginx/conf.d/default.conf /etc/nginx/sites/ \
    && rm -rf /etc/nginx/{conf.d,http.d} \
# forward request and error logs to docker log collector
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && ln -sf /tmp/nginx/run /var/lib/nginx/run \
# Bring in gettext so we can get `envsubst`, then throw
# the rest away. To do this, we need to install `gettext`
# then move `envsubst` out of the way so `gettext` can
# be deleted completely, then move `envsubst` back.
    && apk add --no-cache --virtual .gettext gettext \
    && mv /usr/bin/envsubst /tmp/ \
    && runDeps="$( \
        scanelf --needed --nobanner /tmp/envsubst \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" \
    && apk add --no-cache $runDeps \
    && apk del .gettext \
    && mv /tmp/envsubst /usr/local/bin/ \
# Bring in tzdata so users could set the timezones through the environment
# variables
    && apk add --no-cache tzdata \
# Bring in curl and ca-certificates to make registering on DNS SD easier
    && apk add --no-cache curl ca-certificates
COPY nginx.conf /etc/nginx/
COPY nginx/cfg/* /etc/nginx/cfg/
COPY nginx/sites/*.conf /etc/nginx/sites/
COPY nginx/include-http/*.conf /etc/nginx/include-http/
COPY nginx/include-stream/*.conf /etc/nginx/include-stream/
RUN set -ex \
    && rm /etc/nginx/sites/default.conf \
# set fs permissions
    && chown -R nginx:nginx \
        /var/log/nginx \
        /var/cache/nginx \
        /etc/nginx \
        /tmp/nginx \
        /var/www \
        /var/lib/nginx \
    && chmod -R ug+rw \
        /var/log/nginx \
        /var/cache/nginx \
        /etc/nginx \
        /tmp/nginx \
        /var/www \
        /var/lib/nginx
COPY docker-entrypoint.sh /
COPY envsubst-on-templates.sh /docker-entrypoint.d/
USER nginx
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
