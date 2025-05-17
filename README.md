動画をいい感じになんかしてくれるツール
要求定義→設計→実装の流れでいい感じに作る
五時間くらいで作れたら嬉しい

なお本プロジェクトではパッケージ管理はuv(pipよりクソ早い)で行うので以下のコマンドでインストールすること
- linuxの場合
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# 要ターミナル再起動
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

