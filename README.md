# DockerSecurity
### Example of usage
```bash
ivan@dockersec:~$  python3 docker_check.py -i nginx -c confident_ellis  --info
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