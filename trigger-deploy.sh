#!/bin/bash

# بررسی اینکه git نصب است یا نه
if ! command -v git &> /dev/null; then
    echo "❌ Git نصب نیست. لطفاً اول git رو نصب کن."
    exit 1
fi

# مرحله 1: ایجاد تغییر کوچک (تغییر کامنت در app.py)
echo "# Trigger GitHub Action" >> app.py

# مرحله 2: Git Commit
git add app.py
git commit -m "🚀 تست GitHub Actions و دیپلوی خودکار"

# مرحله 3: Push به branch اصلی
git push origin main

echo "✅ تغییر ارسال شد. می‌تونی وضعیت GitHub Actions رو از این لینک بررسی کنی:"
echo "👉 https://github.com/Termeh-najjarazari/todolist/actions"
