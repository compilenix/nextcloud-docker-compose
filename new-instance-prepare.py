#!/usr/bin/env python3

import os
import subprocess

import click
from rich import pretty, inspect
from rich.console import Console

# setup Rich
pretty.install()
console = Console()
print = console.print
log = console.log

# setup click
@click.command()
@click.option('--dns-name', prompt='DNS Name', help='DNS name used by this Nextcloud instance.')
@click.option('--dns-resolver', prompt='DNS Server', help='DNS server used internaly by the proxy.')
@click.option('--nextcloud-version', prompt='Nextcloud version', help='Nextcloud version; i.e.: 21')
@click.option('--nfs-server', prompt='NFS Server', help='NFS Server to use for nextcloud "data" volume.')
@click.option('--nfs-path', prompt='NFS Path', help='Exported path on the NFS server; i.e.: "/tank/user/cloud"')
@click.option('--proxy-tls/--no-proxy-tls', default=False, help='Enable TLS proxy')
@click.option('--proxy-port-http', default=0, help='Exposed HTTP port')
@click.option('--proxy-port-https', default=0, help='Exposed HTTPS port')
@click.option('--proxy-bind-ip', required=False, multiple=True, help='IP address(es) to bind. Default bind: "0.0.0.0"')
@click.option('--container-restart-policy', help='One of: no, on-failure, always, unless-stopped', default='unless-stopped')
def main(
    dns_name, dns_resolver, nextcloud_version, nfs_server, nfs_path,
    proxy_tls, proxy_port_http, proxy_port_https, proxy_bind_ip,
    container_restart_policy):
    # copy template directory
    # generate docker-compose.yml
    # generate db.env
    # print:
    # - generated http port
    # - generated https port
    # - checklist of possible pending todos
    #   - tls certs
    #   - docker-compose up -d
    #   - firewall at router
    #   - firewall on this host machine
    #   - public dns record
    #   - local dns record
    #   - nfs server path creation and export
    #   - php occ maintenance:install --database="mysql" --database-name="nextcloud" --database-host="localhost" --database-user="root" --database-pass="12345678" --database-table-prefix="" --admin-user="yourname" --admin-pass="87654321"
    #   - php occ db:add-missing-indices
    #   - php occ db:convert-filecache-bigint
    #   - php occ db:add-missing-primary-keys
    #   - php occ config:system:set trusted_domains 1 --value="nextcloud.my.domain"
    #   - php occ config:system:set overwriteprotocol --value="https"
    #   - php occ config:system:set defaultapp --value="files"
    #   - php occ config:system:set log_rotate_size --value="10485760" --type=integer
    pass

if __name__ == '__main__':
    main()
