# I. Data Retrieval and Processing

- Visit https://tiponet.tipo.gov.tw/Gazette/OpenData/DownLoadFiles/FTP_Doc.pdf for detailed information about the content in the TIPO server.
- [LogoShot_Database](https://docs.google.com/presentation/d/1fP-8KXt6wI4HbRO-WEgOEjA0Pqv-d1nKVXRivLGPLaY/edit?usp=sharing) shows all the publicly available data sources provided by TIPO and a comparison between `TrademarkXMLA` (trademark1) and `Tmarkappl` (***trademark2***).

## A. From Raw Data to ***trademark2***

- Fetch `Tmarkappl` from TIPO server.
- Convert XML files to CSV files.
- Process CSV files and dump the data into **trademark2**.
- Remove null rows and duplicates in the database.



# II. MISC

## A. Adding SSH Keys to GitHub Account
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
