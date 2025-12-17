# PublIP
An incredibly simple docker container that displays your public IP address (obtained using https://api.ipify.org) in a neat style that matches Homarr.
It can be used to display the public IP of a Gluetun container on a Homarr dashboard, by adding an iframe widget and pointing it to PublIP.

## Usage
Docker compose if using Gluetun (redirect port 5001 in Gluetun):
```yaml
services:
  publip:
    image: ghcr.io/tobygrice/publip:latest
    container_name: publip
    restart: unless-stopped
    environment:
      - BACKGROUND_COLOR=#2E2E2E # default bg colour
      - TEXT_COLOR=#C8C8C8       # default text colour
      - MAX_FONT_SIZE=5.0rem     # default font size
    network_mode: "service:gluetun"
    depends_on:
      gluetun:
        condition: service_healthy
        restart: true
```

If not using Gluetun:
```yaml
services:
  publip:
    image: ghcr.io/tobygrice/publip:latest
    container_name: publip
    restart: unless-stopped
    ports:
      - "5001:5001"
    environment:
      - BACKGROUND_COLOR=#2E2E2E # default bg colour
      - TEXT_COLOR=#C8C8C8       # default text colour
      - MAX_FONT_SIZE=5.0rem     # default font size
```

The environment variables are optional, with the values in the examples above (suitable for Homarr dark mode) being used as defaults.
