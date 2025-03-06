#!/usr/bin/env python3
import json
from datetime import datetime, UTC
import os
import requests

def clean_domain(domain):
    """Nettoie et valide un domaine."""
    domain = domain.strip().lower()
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain if is_valid_domain(domain) else None

def is_valid_domain(domain):
    """Vérifie si un domaine est valide."""
    import re
    pattern = r'^[a-z0-9][a-z0-9-]{1,61}[a-z0-9](?:\.[a-z]{2,})+$'
    return bool(re.match(pattern, domain))

def fetch_malicious_domains():
    """Récupère les domaines malveillants depuis diverses sources."""
    sources = [
        'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
        'https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt',
        'https://raw.githubusercontent.com/romainmarcoux/malicious-domains/refs/heads/main/full-domains-aa.txt',
        'https://raw.githubusercontent.com/romainmarcoux/malicious-domains/refs/heads/main/full-domains-ab.txt',
    ]
    
    domains = set()
    for source in sources:
        try:
            response = requests.get(source)
            response.raise_for_status()
            
            for line in response.text.splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) >= 2:
                        domain = clean_domain(parts[1])
                        if domain:
                            domains.add(domain)
        except Exception as e:
            print(f"Erreur lors de la récupération depuis {source}: {e}")
    
    return list(domains)

def update_blocklist():
    """Met à jour le fichier blocklist.json."""
    domains = fetch_malicious_domains()
    
    blocklist_data = {
        "total_domains": len(domains),
        "domains": sorted(domains),
        "last_updated": datetime.now(UTC).isoformat()
    }
    
    with open('blocklist.json', 'w', encoding='utf-8') as f:
        json.dump(blocklist_data, f, indent=2, ensure_ascii=False)
    
    print(f"Blocklist mise à jour avec {len(domains)} domaines")

if __name__ == '__main__':
    update_blocklist()
