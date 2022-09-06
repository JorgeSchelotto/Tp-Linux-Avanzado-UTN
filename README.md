# Tp-Linux-Avanzado-UTN

# Imagen en docker hub:

- docker pull jorgeschelotto85/linux2022utn

# Como correr el playbook:

- Instalar Ansible en la maquina host con el comando: sudo apt update y sudo apt install ansible
- En el archivo inventory.yaml cambiar ansible_host agregando la ip a la maquina destino.
- Ejecutar ansible-playbook -i inventory.yaml
