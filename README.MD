# Augury test application

## in order to run the application you need to have a working kubernetes cluster and hombrew installed



```bash
#!/bin/bash
# simply run make in the root directory
make
```

# the make proccess will automatically create the docker image, push it to a temporary docker registry https://ttl.sh/), and install the helm chart