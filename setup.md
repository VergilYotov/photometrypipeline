# Setup
Based on https://photometrypipeline.readthedocs.io/en/latest/install.html

## Package dependencies

```sh
sudo apt-get install -y \
       build-essential \
       libssl-dev \
       libffi-dev \
       git \
       wget \
       imagemagick \
       curl \
       libplplot-dev \
       libshp-dev \
       libcurl4-gnutls-dev \
       liblapack3 liblapack-dev liblapacke liblapacke-dev \
       libfftw3-3 libfftw3-dev libfftw3-single3 \
       libatlas-base-dev
```

## Add Astromatic repo
As per https://www.astromatic.net/repositories/
```
sudo su -c 'echo "deb https://repo.astromatic.net/ubuntu/bleeding "$(grep -oP "DISTRIB_CODENAME=\K\w+" /etc/lsb-release)" main" > /etc/apt/sources.list.d/astromatic-bleeding.list'
sudo apt-key adv --fetch-keys https://repo.astromatic.net/astromatic.key
sudo apt-get update
```
## Install Sextractor and SCAMP
```
sudo apt remove --purge source-extractor
sudo apt install sextractor scamp
```

## Clone the code
## Python setup
### Virtual Environment
`virtualenv venv`
### Add env variables
`nano ~/photometrypipeline/venv/bin/activate`

Add at the bottom
```
# photometry pipeline setup
export PHOTPIPEDIR=~/photometrypipeline
export PATH=$PATH:~/photometrypipeline/
```
### Install Python dependencies
```
source venv/bin/activate
pip install numpy scipy astropy astroquery matplotlib pandas future scikit-image
```

# Running
```
pp_run -target TargetName *fit 
```

See https://photometrypipeline.readthedocs.io/en/latest/quickstart.html
and https://photometrypipeline.readthedocs.io/en/latest/functions.html
