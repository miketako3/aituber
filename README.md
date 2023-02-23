# AI Tuber by miketako3

## preparation

### Mac

For playing audio on docker, pulseaudio is needed.

```shell
brew install pulseaudio
pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon
```

And then, `.env` file is also needed.

```shell
vim .env
#OPENAPI_KEY=${API key of open ai}
#VIDEO_ID=${youtube live id}
```

## How To Use

```shell
docker-compose up
```

## components

### brain

Proxy for gpt-3.

### ear

Proxy for youtube comment.

### main

Main loop.