# WebShield-blocklist

This repository contains the blocklist used by the WebShield Chrome extension to protect users from malicious websites.

## Structure

- `blocklist.json`: Main blocklist file containing malicious domains
- `update_script.py`: Python script to update the blocklist
- `requirements.txt`: Python dependencies

## Format

The `blocklist.json` file follows this format:
```json
{
    "total_domains": 1234,
    "domains": ["example.com", "malicious-site.com", ...],
    "last_updated": "2024-03-21T12:00:00Z"
}
```

## Sources

The blocklist is aggregated from multiple trusted sources:
- Steven Black's hosts file
- KADhosts
- More sources to be added

## Automatic Updates

The blocklist is automatically updated daily using GitHub Actions. The `update_script.py` fetches new domains from our sources and updates the blocklist.

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new malicious domains source'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Development

To set up the development environment:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run update script
python update_script.py
```

## License

MIT License - See LICENSE file for details
