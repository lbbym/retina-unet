# Docker image to run retina-unet

This image runs based on the nvidia/cuda image, it has [Keras](https://github.com/fchollet/keras) installed and configured to run using Theano as the backend with CPU only.

To start the image you can use the following command

```bash
docker run -it -v {path-to-DRIVE-dataset}:/src/DRIVE -e "OMP_NUM_THREADS=4" alevalv/retina-unet:latest /src/runner.sh
```

## TODO

Enable tensorflow or cntk and their usage with nvidia-docker
