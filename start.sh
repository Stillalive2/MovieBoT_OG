echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/StillAlive2/MovieBot_OG.git /EvaMaria
cd /EvaMaria
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
