mkdir "/usr/local/bin/sitova_aplikace"
cp -r "commands" "/usr/local/bin/sitova_aplikace/"
cp -r "config" "/usr/local/bin/sitova_aplikace/"
cp "main.py" "/usr/local/bin/sitova_aplikace/"
cp "logging.py" "/usr/local/bin/sitova_aplikace/"
cp "configuration.py" "/usr/local/bin/sitova_aplikace/"
mkdir "/usr/local/bin/sitova_aplikace/log"
touch "/usr/local/bin/sitova_aplikace/log/log.txt"
chmod ugo+w "/usr/local/bin/sitova_aplikace/log/log.txt"
cp "sitova_aplikace.service" "/etc/systemd/system"
