# build_files.sh
git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --aggressive --prune=now
pip install -r requirements.txt
python3.9 manage.py collectstatic