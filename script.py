import os

os.pardir
# os.system("docker build -t p-new .")
os.system(
    f"docker run -d -it p-new --mount source=/var/lib/docker/volumes/test/,destination=/usr/src/app/container-data ubuntu")
