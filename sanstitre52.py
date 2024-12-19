# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 05:02:07 2024

@author: pc
"""

import socket

def check_open_ports(ip, ports):
    print(f"Analyse des ports ouverts sur {ip}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((ip, port)) == 0:
                    print(f"[OUVERT] Port {port} (Service inconnu)")
        except Exception as e:
            print(f"Erreur sur le port {port}: {e}")

# Exemple : vérifier les ports 20 à 100 sur localhost
check_open_ports("127.0.0.1", range(20, 101))
