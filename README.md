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
  ssh pi@192.168.1.105
  ```
