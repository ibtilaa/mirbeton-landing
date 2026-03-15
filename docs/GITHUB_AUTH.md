# GitHub autentifikatsiyasi (push ishlashi uchun)

Loyiha remote: `https://github.com/ibtilaa/mirbeton-landing`. Push qilish uchun quyidagilardan birini qiling.

---

## 1-variant: SSH (tavsiya etiladi)

SSH kalit GitHub’da ro‘yxatdan o‘tgan bo‘lsa, remote’ni SSH ga o‘zgartirish kifoya.

### 1.1 SSH kalit bormi tekshiring
```bash
ls -la ~/.ssh/id_ed25519.pub  # yoki id_rsa.pub
```
Agar fayl yo‘q bo‘lsa, yangi kalit yarating:
```bash
ssh-keygen -t ed25519 -C "siz@email.com" -f ~/.ssh/id_ed25519 -N ""
```

### 1.2 GitHub’ga kalit qo‘shing
- `cat ~/.ssh/id_ed25519.pub` (yoki `id_rsa.pub`) ni nusxalang.
- GitHub → Settings → SSH and GPG keys → New SSH key → paste → Save.

### 1.3 Remote’ni SSH ga o‘zgartirish
```bash
cd /Users/mab/PROJECT/Cursor_project/mirbeton-landing
git remote set-url origin git@github.com:ibtilaa/mirbeton-landing.git
git push origin main
```

---

## 2-variant: GitHub CLI (HTTPS orqali)

`gh` o‘rnatilgan bo‘lsa, bir marta login qiling; keyin `git push` ishlashi mumkin.

```bash
# Bir marta
gh auth login
# Browser ochiladi, GitHub’da tasdiqlang

# Keyin
cd /Users/mab/PROJECT/Cursor_project/mirbeton-landing
git push origin main
```

---

## 3-variant: Personal Access Token (HTTPS)

1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token (repo scope).
2. Token’ni nusxalab oling.
3. Terminalda (Cursor yoki tashqi):
   ```bash
   cd /Users/mab/PROJECT/Cursor_project/mirbeton-landing
   git push origin main
   ```
   Username: GitHub foydalanuvchi nomi (masalan `ibtilaa`).  
   Password: token (yangi yaratilgan PAT).

macOS Keychain so‘rasa, token saqlanadi va keyingi push’larda yana so‘ralmasligi mumkin.
