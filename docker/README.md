# Docker image to run retina-unet

This image runs based on the nvidia/cuda image, it has [Keras](https://github.com/fchollet/keras) installed and configured to run using Theano as the backend with CPU only.

To start the image you can use the following command

```bash
docker run -it -v {path-to-DRIVE-dataset}:/src/DRIVE alevalv/retina-unet:latest bash
```

## TODO

Enable tensorflow or cntk and their usage with nvidia-docker
