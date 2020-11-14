# DockerSecurity
### Example of usage

##### Check image and container 
```bash
ivan@dockersec:~$ python3 docker_check.py -i nginx -c confident_ellis  --info
Docker Image Warnings:
[Users]:        No user in image
Docker Container Info:
[Ulimit]:       No Ulimits
[Memory]:       No Memory Limits
[CPU]:          No CPU Limits
[PIDs]:         No PiDs Limits
[CapDrop]:      No dropped capabilities

- Capabilities: You have no dropped capabilities
Please follow this link, to read more:
https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities
```
##### Reverse image to dockerfile"
```bash
ivan@dockersec:~$ python3 docker_check.py -r nginx
 ADD file:0dc53e7886c35bc21ae6c4f6cedda54d56ae9c9e9cd367678f1a72e68b3c43d4 in /
 CMD ["bash"]
 LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>
 ENV NGINX_VERSION=1.19.4
 ENV NJS_VERSION=0.4.4
 ENV PKG_RELEASE=1~buster
 RUN set -x 
        && addgroup --system --gid 101 nginx
        ...

 ENTRYPOINT ["/docker-entrypoint.sh"]
 EXPOSE 80
 STOPSIGNAL SIGTERM
 CMD ["nginx" "-g" "daemon off;"]
```