# エラー発生時の備忘録

## Unable to load any of ***

cuda指定でtest.pyを実行することで
以下のエラーが発生する。
```
Unable to load any of {libcudnn_ops.so.9.1.0, libcudnn_ops.so.9.1, libcudnn_ops.so.9, libcudnn_ops.so}
Invalid handle. Cannot load symbol cudnnCreateTensorDescriptor
中止 (コアダンプ)
```

この場合はこの[issue](https://github.com/jhj0517/Whisper-WebUI/issues/346)に習い以下を実行する
```
sudo apt-get install libcudnn9-cuda-12
```