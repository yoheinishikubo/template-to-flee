# 謝罪テンプレート

緊急時に謝罪のみを行うためのウェブサイトに差し替えるためのGoogle App Engine用テンプレートです。
別途、DNSのレコード設定と併用することで、以下のエントリのような効果を得ることができます。

[乙武さん不倫の謝罪ホームページに見るプロの犯行][1]

Google App Engine上の静的ファイルはGoogleのEdge Cacheにて配信されますので、比較的高速（ややレイテンシは遅いようです）に安定して提供することが可能です。

設定するドメイン配下のURLは全て謝罪ページの表示となりますので、余計なコンテンツを閲覧されずに済む一方、もちろん全ての情報配信を止めてしまうこととなるため、使いみちはご注意ください。ただし可逆的かつ速やかに復旧可能です。

## 使い方

ターミナルにて任意のディレクトリ以下で以下のコマンドを入力し、テンプレートファイル群をコピーします。

`git clone https://github.com/yoheinishikubo/template-to-flee.git`

ファイル内容を自社に適した内容で書き換えます。
  - OGPに[土下座している男性の画像][2]を仮置きしていますが、テキストのみの構成に比して転送量が大幅に増加しますので、謝罪用の予算が潤沢な場合を除いてコメントアウトされた方がよろしいかと思われます。
  - 謝罪サイトがテンプレートを用いて作成されていることが一般の方々に知られますとさらなる炎上を呼ぶ可能性がございますので、二重チェックするなど内容が問題ないかをよくご確認ください。

ターミナルにて上記ディレクトリに移動し、以下のコマンドを入力します。
（Google Cloud SDKが正常にインストール・設定されている環境が前提となります）

`gcloud preview app deploy app.yaml`

以上で、ウェブサイトのアップロードは完了します。


[1]: http://fukuyuki.net/post-805/
[2]: http://www.irasutoya.com/2014/03/blog-post_7656.html
