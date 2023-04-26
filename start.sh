if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/krackxor/vip.git /vip
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /vip
fi
cd /vip
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
