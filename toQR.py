import csv
import os
import qrcode

# CSVファイルのパス（例: data.csv）
csv_file = 'data.csv'
# 出力先フォルダ
output_dir = 'qr_codes'

# 出力フォルダがなければ作成
os.makedirs(output_dir, exist_ok=True)

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # ファイル名と文字列を取得し、前後の空白を除去
        filename = row['ファイル名'].strip()
        text = row['文字列'].strip()

        # ファイル名または文字列が空の場合はスキップ
        if not filename or not text:
            continue

        # ファイル名に拡張子がなければ追加
        if not filename.lower().endswith('.png'):
            filename += '.png'

        # QRコードを生成
        img = qrcode.make(text)
        # 出力パスを作成
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)
        print(f"Saved: {output_path}")
