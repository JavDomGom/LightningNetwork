# LightningNetwork
Repo to test Bitcoin Lightning Network

## Configure
1. Listar los filesystems.
  ```bash
  df -h
  Filesystem      Size   Used  Avail Capacity   iused     ifree %iused  Mounted on
  /dev/disk0s2   931Gi  389Gi  541Gi    42% 102036502 141944240   42%   /
  devfs          184Ki  184Ki    0Bi   100%       638         0  100%   /dev
  map -hosts       0Bi    0Bi    0Bi   100%         0         0  100%   /net
  map auto_home    0Bi    0Bi    0Bi   100%         0         0  100%   /home
  /dev/disk1s1    43Mi   22Mi   21Mi    51%         0         0  100%   /Volumes/boot
  ```

2. Crear archivo `ssh` vacío en la tarjeta micro SD.
  ```bash
  > /Volumes/boot/ssh
  ```

3. Probar conexión SSH.
  ```bash
  ssh -o StrictHostKeyChecking=no pi@192.168.1.105
  ```

4. Cerrar la sesión SSH y volver a localhost. Instalar la librería `passlib` de Python.
  ```bash
  pip install passlib
  ```

5. Hashear una nueva password para el usuario `pi` con el siguiente comando.
  ```bash
  python -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))"
  ```
  En el pormpt introducir la que será la nueva password para el usuario `pi`, por ejemplo `abcd1234`. El programa nos devolverá una cadena hasheada similar a la siguiente.
  ```bash
  $6$VqxDAcvzA/ZjOeDl$GVbVL2oEAwyHd7CWmqAi0ifrLgZvqWhtPq8J.H/lMIC48T6cAKcx/GnSgVjH2g33u4HDZiEudm37pD3c3MPu./
  ```

6. Modificar archivo `/etc/dhcpcd.conf`. Descomentar las líneas `static ip_address`, `static routers` y `static domain_name_servers`. Se han de añadir la dirección IP de la RaspberryPi y la del Router.
  ```bash
  # Example static IP configuration:
  #interface eth0
  static ip_address=192.168.1.105/24
  #static ip6_address=fd51:42f8:caae:d92e::ff/64
  static routers=192.168.1.1
  static domain_name_servers=192.168.1.1 8.8.8.8 fd51:42f8:caae:d92e::1
  ```

7. Descargar el [cliente de Bitcoin Core](https://bitcoincore.org/bin/bitcoin-core-0.17.1/bitcoin-0.17.1-arm-linux-gnueabihf.tar.gz) y chequear el hash SHA256 para verificar su integridad.

8. Crear los directorios `/opt/bitcoin` y `~/.bitcoin`.

9. Descomprimir el cliente Bitcoin Core descargado previamente en el directorio `/opt/bitcoin`.

10. Añadir la siguiente línea al final del archivo `/home/pi/.profile`.
```bash
export PATH=$PATH:/opt/bitcoin/bin
```
