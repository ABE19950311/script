#! /bin/bash
#cron実行時、シェルに存在する環境変数は基本ない
#webbrowser実行時に必要なDISPLAY変数を定義してからpython呼んだらcronから実行できた
export DISPLAY=:0
python3 /home/abe/mailpy/browser.py
