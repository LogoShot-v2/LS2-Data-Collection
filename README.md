# Data-Collection

## Adding SSH Keys to GitHub Account
- For detailed instructions, visit https://docs.github.com/en/authentication/connecting-to-github-with-ssh.
```shell
ssh-keygen -t ed25519 -C "your_email@example.com"
# (Don't change default file location.)
# (Enter passphrase.)

pbcopy < ~/.ssh/id_ed25519.pub
# (or copy manually)
# (Paste the public key to your GitHub settings.)

# (Do the following so that passphrase is not required next time.)
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```
