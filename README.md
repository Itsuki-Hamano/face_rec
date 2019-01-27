<ul type="disc">
  <li>googleColaboratoryで作成したので、Jupyterで動かせると思います。<br>
    pythonで動かしたい場合は、後半のセルに書いてあるコードを、そのままコピペしてください。<br></li>
<li>openCV公式がgithubで配布している重みファイルだと読み込みエラーがでるので、<br>
  upしました</li>
  </ul>

<dl>
  <dt>crop_face_image</dt>
  <dd>OpenCVの重みファイルで検出したものを画像として切り出する機能<br>検出範囲を元画像に書き込む機能<br>検出されなかった画像名のログを出力する機能</dd>
  <dt>cv_one_shot_images</dt>
  <dd>inputディレクトリの画像とdbディレクトリの顔画像と比較し、<br>ワンショット学習による人物認証し、顔領域にモザイクを掛ける</dd>
  <dt>video_mos</dt>
  <dd>保存済み動画ファイル（mp4）内の顔をopenCVで検出して<br>モザイク加工をした動画(mp4）を出力する</dd>
 </dl>
  
 
