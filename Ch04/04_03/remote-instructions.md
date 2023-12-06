# Remote Instructions

[Create a GCP VM](https://cloud.google.com/compute/docs/instances/create-start-instance).

[Install gcloud CLI](https://cloud.google.com/sdk/docs/install) on your machine.

From the terminal, connect to the machine via SSH:

```
$ gcloud compute ssh --zone "<zone>" "<instance name>" --project "<project>"
```

On the instance, install miniconda:

```
$ curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda
```

Then install Jupyter Lab and other dependencies and run Jupyter Lab:

```
$ ~/miniconda/bin/conda install jupyterlab pandas
$ ~/miniconda/bin/jupyter lab
```

In a different terminal on your machine, create an SSH tunnel to the VM:

```
$ gcloud compute ssh --zone "<zone>" "<instance name>" --project "<project>" -- -NL 8888:localhost:8888
```

This will forward port 8080 from the GCP VM to your machine.

Now you can [connect to the remote server](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_connect-to-a-remote-jupyter-server).

**Don't forget to shut down the VM once you're done with it.**


## Notes

You can do the same with other cloud providers, the instruction to setup the VM and open SSH tunnel differ depends on the cloud provider.
