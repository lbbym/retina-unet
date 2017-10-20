# Docker image to run retina-unet

This image runs based on the nvidia/cuda image, it has [Keras](https://github.com/fchollet/keras) installed and configured to run using Tensorflow as the backend with CPU.

To start the image using CPU you can use the following command:

```bash
docker run -it -v {path-to-DRIVE-dataset}:/src/DRIVE alevalv/retina-unet:latest /src/runner.sh
```

To run the image using Theano with CPU mode you can use this command:

```bash
docker run -it -v {path-to-DRIVE-dataset}:/src/DRIVE -e KERAS_BACKEND=theano alevalv/retina-unet:latest /src/runner.sh
```

For GPU mode with tensorflow you can use the following command (having [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) installed):

```bash
nvidia-docker run -it -v {path-to-DRIVE-dataset}:/src/DRIVE alevalv/retina-unet:latest-gpu /src/runner.sh
```

Source for the dockerfile and the code used here is available at [GitHub](https://github.com/alevalv/retina-unet)

## TODO

Add support to use CNTK as a backend
