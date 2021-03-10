#!/bin/sh

set -e

ME=$(basename $0)

auto_envsubst() {
    local templates="/etc/nginx/nginx.conf /etc/nginx/sites/ /etc/nginx/include-nginx.conf/ /etc/nginx/include-http/ /etc/nginx/include-stream/ ${NGINX_ENVSUBST_TEMPLATES:-}"
    local suffix=".conf"

    local template template_location defined_envs relative_path output_path subdir dir_name
    defined_envs=$(printf '${%s} ' $(env | cut -d= -f1))
    for template_location in $templates; do
        if [ -d "$template_location" ] && [ ! -z "$(ls -A $template_location)" ]; then
            mkdir -p "/tmp/nginx/conf/${template_location#/etc/nginx/}"
            cp -r $template_location/* "/tmp/nginx/conf/${template_location#/etc/nginx/}/"
        fi
        if [ -f "$template_location" ]; then
            dir_name="$(dirname $template_location)"
            mkdir -p "/tmp/nginx/conf${dir_name#/etc/nginx}/"
            cp "$template_location" "/tmp/nginx/conf${dir_name#/etc/nginx}/"
        fi
    done

    for template_file in $(find "/tmp/nginx/conf/" -follow -type f -name "*$suffix" -print); do
        echo $template_file | while read -r template; do
            echo >&3 "$ME: Running envsubst on /etc/nginx/${template_file#/tmp/nginx/conf/}"
            envsubst "$defined_envs" < "$template" > "/etc/nginx/${template_file#/tmp/nginx/conf/}"
        done
    done
}

auto_envsubst
