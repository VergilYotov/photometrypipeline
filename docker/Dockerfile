FROM ubuntu

# Set environment variable to avoid user interaction during package installations
ENV PHOTPIPEDIR=/home/photometrypipeline \
    PATH=$PATH:/home/photometrypipeline/ 
    

# Update the package lists and install necessary packages
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    build-essential \
    libssl-dev \
    libffi-dev \
    git \
    libplplot-dev \
    libshp-dev \
    libcurl4-gnutls-dev \
    liblapack3 \
    liblapack-dev \
    liblapacke \
    liblapacke-dev \
    libfftw3-3 \
    libfftw3-dev \
    libfftw3-single3 \
    libatlas-base-dev \
    scamp \
    pip \
    nano \
    libcfitsio-dev \
    python3.10-venv \
    imagemagick 

# Install sextractor
RUN cd /tmp && \
    git clone https://github.com/astromatic/sextractor.git && \
    cd sextractor && \
    sh autogen.sh && \
    ./configure && \
    make -j && \
    make install

# Donwload Photometry Pipeline
RUN cd /home && git clone https://github.com/AsenAsenov1/photometrypipeline.git

# Import files - requirements.txt / server.py / py_environment.sh
COPY ./docker/requirements.txt /tmp/
COPY ./docker/server.py /home/
COPY ./docker/py_environment.sh /tmp

# Create Python virtual environment 
RUN bash /tmp/py_environment.sh

# Set aliases
RUN echo "alias pact='source /home/pp_env/bin/activate'" >> /root/.bashrc

# Expose port 9090 
EXPOSE 9090

# Start the Python HTTP server in the background
CMD ["python3", "-m", "http.server", "9090"]



