【御丹宮くるみ (SimpleEnunu) (NNSVS-WORLD v4+HN-uSFGAN) v0.0.1 】

御丹宮くるみ歌声データベース (2020 年 8 月 31 日ダウンロード) を NNSVS で学習させて,
UTAU プラグイン「 SimpleEnunu 」から呼び出せるようにした歌声モデルです.
ボコーダとして PyWORLD ではなく HN-UnifiedSourceFilterGAN を採用しています.

UTAU エディタ上での採譜および歌詞チェック用に,
「波音リツ音声ライブラリ単独音 Ver1.5.1Lite for UTAU 」を同梱しています.

【ソフトウェアの対応バージョン】

Windows 10 / UTAU 0.4.18 / SimpleEnunu 0.1.0

----------------------------

【使い方】

1. 単独音歌詞で UST を作成
2. UST を保存
3. 音源に「御丹宮くるみ (SimpleEnunu) (NNSVS-WORLD v4+HN-uSFGAN) v0.0.1 」を選択
4. ノートを範囲選択し, プラグイン「 SimpleEnunu 」を起動
5. 待機
6. UST の保存場所の隣に WAV ファイルが生成される


【利用規約】

御丹宮くるみ 歌声データベースの利用規約に従ってください. (http://onikuru.info/db-download/)

再配布可としますが, 前項の規約に相当する内容を必ず含んでください.

歌声モデルの不具合修正は, その時点での最新バージョンのみ対応します.

不具合報告はこちらの「 New issue 」にお願いします. (https://github.com/taroushirani/SimpleEnunu/issues)

アイコン画像は御丹宮くるみ氏の twitter のアイコンから拝借しています.


----------------------------

【歌声モデル仕様】

- 御丹宮くるみ 歌声データベース (2020 年 8 月 31 日ダウンロード) から学習
- 使用レシピ: NNSVS-WORLD v4 相当 (https://github.com/taroushirani/nnsvs/tree/dev20221106/recipes/oniku_kurumi_utagoe_db/v4lf0-48k-world)
- 音声ファイル出力: 16bit 整数 / 48kHz
- gain_normalize を無効化

----------------------------

【アイコン制作】

【連絡先】
Tarou Shirani <taroushirani@gmail.com>
