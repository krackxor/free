if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/krackxor/free.git /free
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /free
fi
cd /free
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
