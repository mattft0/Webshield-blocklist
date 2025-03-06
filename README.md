# WebShield-blocklist

Ce dépôt contient la liste des domaines bloqués utilisée par l'extension WebShield.

## Structure

- `blocklist.json` : La liste principale des domaines bloqués
- `update_script.py` : Script pour mettre à jour la liste des domaines

## Format

Le fichier `blocklist.json` suit le format suivant :
```json
{
    "total_domains": 1234,
    "domains": ["example.com", "malicious-site.com", ...],
    "last_updated": "2024-03-21T12:00:00Z"
}
```

## Mise à jour

La liste est mise à jour régulièrement via le script `update_script.py`. Les contributions sont les bienvenues via Pull Requests.

## Contribution

1. Fork ce dépôt
2. Créez une branche pour vos modifications
3. Soumettez une Pull Request avec vos changements

## Licence

MIT License
