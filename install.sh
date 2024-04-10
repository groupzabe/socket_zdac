#!/bin/bash

# Atualiza a lista de pacotes
sudo apt-get update

# Instala o Supervisor
sudo apt-get install -y supervisor

# Cria um arquivo de configuração para o script Python no Supervisor
sudo bash -c 'cat > /etc/supervisor/conf.d/socket_zdac.conf <<EOF
[program:socket_zdac]
command=/usr/bin/python3 /home/zabe/socket_zdac/main.py
directory=/home/zabe/socket_zdac/
autostart=true
autorestart=true
stderr_logfile=/var/log/socket_zdac.err.log
stdout_logfile=/var/log/socket_zdac.out.log
EOF
'

# Recarrega a configuração do Supervisor
sudo supervisorctl reread
sudo supervisorctl update

# Inicia o serviço do seu script Python
sudo supervisorctl start socket_zdac
