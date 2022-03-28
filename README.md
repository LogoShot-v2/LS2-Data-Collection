# MISC

## I. Adding SSH Keys to GitHub Account
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

## II. Issues
- 商標註冊申請案 API 可行性（不用存資料在 local）
  - 看 API 傳回來的資料完整度
  - 希望把資料存在 local 確保 app 的運作
- 考量現有功能，資料庫部分欄位不必要
  - 對商標資訊而言重要的欄位都要留！
- `TODO` 釐清每個 database 的 column
