【夏目悠李 (SimpleEnunu) (NNSVS-WORLD v5+pitch-shift data augmentation+SiFiGAN) v0.0.1 】

夏目悠李/ 男声歌声データベース (2021 年 7 月 13 日版) を NNSVS で学習させて,
UTAU プラグイン「 SimpleEnunu 」から呼び出せるようにした歌声モデルです.  
pitch-shift data augmentation という手法で学習データを拡張しています.

UTAU エディタ上での採譜および歌詞チェック用に,
「波音リツ音声ライブラリ単独音 Ver1.5.1Lite for UTAU 」を同梱しています.

【ソフトウェアの対応バージョン】

Windows 10 / UTAU 0.4.18 / SimpleEnunu 0.1.0

----------------------------

【使い方】

1. 単独音歌詞で UST を作成
2. UST を保存
3. 音源に「夏目悠李 (SimpleEnunu) ((NNSVS-WORLD v5+pitch-shift data augmentation+SiFiGAN) v0.0.1 」を選択
4. ノートを範囲選択し, プラグイン「 SimpleEnunu 」を起動
5. 待機
6. UST の保存場所の隣に WAV ファイルが生成される


【利用規約】

夏目悠李/ 男性歌声データベースの利用規約に従ってください. (https://ksdcm1ng.wixsite.com/njksofficial/%E8%A6%8F%E7%B4%84-rules)

再配布可としますが, 前項の規約に相当する内容を必ず含んでください.

歌声モデルの不具合修正は, その時点での最新バージョンのみ対応します.

不具合報告はこちらの「 New issue 」にお願いします. (https://github.com/taroushirani/SimpleEnunu/issues)

アイコン画像はデザイナーの UNF/UserNotFound 氏の公式イラストから作成しています. キャラクター「夏目悠李」を使用する際のガイドライン (https://amanokei.hatenablog.com/entry/2020/10/10/134126) に従ってください.


【歌声モデル仕様】

- 夏目悠李/ 男性歌声データベース (2021 年 7 月 13 日版) から学習
- 使用レシピ: NNSVS-WORLD v5 相当 (https://github.com/taroushirani/nnsvs/tree/dev20221106/recipes/natsume_singing/v5-48k-world-psda)
- Pitch-shift data augmentation で学習データを拡張
- 音声ファイル出力: 16bit 整数 / 48kHz

----------------------------

【連絡先】
Tarou Shirani <taroushirani@gmail.com>
