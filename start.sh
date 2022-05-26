echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/StillAlive2/MovieBot_OG.git /MovieBot_OG
cd /MovieBot_OG
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
