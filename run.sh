#!/bin/bash

# docker run -it -v $(pwd):/usr/src/app octaveplay bash
docker run -it \
	-e DISPLAY=$DISPLAY \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-v $(pwd):/usr/src/app \
	octaveplay bash