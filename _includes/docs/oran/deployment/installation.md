## Near RT-RIC deployment
The Near RT-RIC services can be downloaded from the original `ric-dep`. The original repo assumes `root` user behaviour for `install_common_templates_to_helm.sh` script, for a general deployment we have edited it and added `sudo` command for some of the copy commands you can replace the script with our script for deployment.
```sh
git clone https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep
cp ./install_common_templates_to_helm.sh ./ric-dep/bin
cd ric-dep/bin
./install_common_templates_to_helm.sh
version=j   # change variable according to release preference.
./install -f ../RECIPE_EXAMPLE/example_recipe_oran_${version}_release.yaml -c "influxdb jaegeradapter"
```

{% include notification.html status="is-warning" message="The additional flags for ***influxdb*** and ***jaegeradapter*** are only supported for ***h-release*** and later." %}